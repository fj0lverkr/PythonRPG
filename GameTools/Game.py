from xml.dom import minidom as md


class GameCell:
    def __init__(self, id, intro, actions=None):
        self.id = id
        self.intro = intro
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
            player_action = input("What will you do?\n")
            if player_action.lower() in ["help", "?", "what do i do?", "help me", "actions", "show actions", "hint", "show hint"]:
                print("\nThese are the available actions:\n")
                actions = ""
                for i, a in enumerate(self.actions):
                    if i < len(self.actions)-1:
                        actions += f"{a['name']}, "
                    else:
                        actions += a["name"]
                print(actions)
                self.run_cell()
            else:
                for a in self.actions:
                    if a['name'].lower() == player_action.lower():
                        self.run_action(a["type"], a["target"])
                print("\nThat didn't work...\n")

    def run_action(self, actiontype, target):
        if actiontype == "game_exit" and target == "self":
            print("\nExiting game by player request...")
            exit()


class Game:
    def __init__(self, data_file):
        self.data = md.parse(data_file)
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
            cell_actions = c.getElementsByTagName("action")
            self.cells[cell_id] = GameCell(cell_id, cell_intro, actions=cell_actions)

    def goto_cell(self, cell_id):
        self.cells[cell_id].run_cell()

    def start_game(self, saved_entry=None):
        # if we have no savefile present (to be implemented), otherwise use the entry from the savefile
        if not saved_entry:
            self.goto_cell(self.params["entry"])


if __name__ == "__main__":
    sample_game = Game("GameData/sample_game.xml")
    sample_game.start_game()
