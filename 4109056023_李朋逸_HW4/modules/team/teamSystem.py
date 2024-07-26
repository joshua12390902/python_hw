"""TODO: Finish the logic here.
import Modules。"""
from .teamSub import gridSystem
from .teamSub import teamAssembleSystem

class TeamSystem():
    def __init__(self, game):
        """TODO: Finish the logic here.
        繼承子系統。"""
        self.gridSystem = gridSystem.GridSystem(game)
        self.teamAssembleSystem = teamAssembleSystem.TeamAssembleSystem(game)
    def start(self):
        while True:
            print("==========組隊模式==========")
            print("輸入1以查詢隊員的詳細資料。")
            print("輸入2以進行組隊")
            print("輸入-1離開組隊模式")
            n = input()
            if n == "-1":
                break
            elif n == "1":
                self.gridSystem.start()
            elif n == "2":
                self.teamAssembleSystem.start()   
            """TODO: Finish the logic here.
            子系統呼叫。"""