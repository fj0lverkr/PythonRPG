from xml.dom import minidom as md
from os import system, name

def clear_scene():
    # for Windows 
    if name == 'nt': 
        _ = system('cls') 
    # for other os
    else: 
        _ = system('clear')


class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


HELP_STRINGS = ["help", "?", "what do i do?", "help me", "actions", "show actions", "hint", "show hint"]
HELP_PROMPT = f"{ConsoleColors.OKGREEN}\nThese are the available actions:{ConsoleColors.ENDC}\n"
ACTION_FAILED = f"{ConsoleColors.FAIL}\nThat didn't work...{ConsoleColors.ENDC}\n"
EXIT_GAME_MESSAGE = "\nExiting game by player request..."

class GameCell:
    def __init__(self, game, id, intro, prompt, actions=None):
        self.game = game
        self.id = id
        self.intro = intro
        self.prompt = prompt[0].firstChild.nodeValue
        try:
            self.intro_text = self.intro[0].firstChild.nodeValue
        except:
            print(f"GameCell {self.id} has no entry node. Exiting...")
            exit()
        self.actions = []
        if actions:
            for a in actions:
                action = {}
                action["name"] = a.getAttribute("name")
                action["type"] = a.getAttribute("type")
                action["target"] = a.getAttribute("target")
                self.actions.append(action)
                action_aliases = a.getElementsByTagName("alias")
                for aa in action_aliases:
                    action_alias = {}
                    action_alias["name"] = aa.getAttribute("name")
                    action_alias["type"] = a.getAttribute("type")
                    action_alias["target"] = a.getAttribute("target")
                    self.actions.append(action_alias)

    def __str__(self):
        return f"GameCell {self.id}"

    def __repr__(self):
        return f"GameCell {self.id}"

    def run_cell(self):
        print(self.intro_text)
        while True:
            player_action = input(self.prompt)
            if player_action.lower() in HELP_STRINGS:
                clear_scene()
                print(HELP_PROMPT)
                actions = ""
                for i, a in enumerate(self.actions):
                    if i < len(self.actions)-1:
                        actions += f"{a['name']}, "
                    else:
                        actions += a["name"]
                print(ConsoleColors.OKGREEN + actions + ConsoleColors.ENDC)
                self.run_cell()
            else:
                for a in self.actions:
                    if a['name'].lower() == player_action.lower():
                        self.run_action(a["type"], a["target"])
                print(ACTION_FAILED)

    def run_action(self, actiontype, target):
        if actiontype == "game_exit" and target == "self":
            clear_scene()
            print(EXIT_GAME_MESSAGE)
            exit()
        elif actiontype == "goto_cell" and target in self.game.cells:
            clear_scene()
            self.game.goto_cell(target)


class Game:
    def __init__(self, data_file, player=None):
        self.data = md.parse(data_file)
        self.player = player
        self.cells = {}
        self.params = {}
        params = self.data.getElementsByTagName("param")
        for p in params:
            param_name = p.getAttribute("name")
            self.params[param_name] = p.getAttribute("val")
        cells = self.data.getElementsByTagName("cell")
        for c in cells:
            cell_id = c.getAttribute("id")
            cell_intro = c.getElementsByTagName("intro")
            cell_prompt = c.getElementsByTagName("prompt")
            cell_actions = c.getElementsByTagName("action")
            self.cells[cell_id] = GameCell(self, cell_id, cell_intro, cell_prompt, actions=cell_actions)

    def goto_cell(self, cell_id):
        self.cells[cell_id].run_cell()

    def start_game(self, saved_entry=None):
        clear_scene()
        # if we have no savefile present (to be implemented), otherwise use the entry from the savefile
        if not saved_entry:
            self.goto_cell(self.params["entry"])
