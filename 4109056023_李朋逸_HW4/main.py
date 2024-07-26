from modules.card import card
from modules.loot import lootSystem
from modules.team import teamSystem
from modules.battle import battleSystem

class Game():
    def __init__(self):
        self.lootSystem = lootSystem.LootSystem(self)
        self.teamSystem = teamSystem.TeamSystem(self)
        self.battleSystem = battleSystem.BattleSystem(self)
        self.resource = 4
        self.characterList = []
        self.teamList = []
        self.teamLimit = 5
    
    def start(self):
        while True:
            print("==========遊戲主畫面==========")
            print("輸入1進入抽卡系統。")
            print("輸入2進入組隊系統。")
            print("輸入3進入戰鬥系統。")
            print("輸入exit離開遊戲。")
            n = input()
            if n == "1":
                self.lootSystem.start()
            elif n == "2":
                self.teamSystem.start()
            elif n == "3":
                self.battleSystem.start()
            elif n == "exit":
                print("遊戲結束")
                break
            else:
                print("輸入錯誤，請重新輸入")

if __name__ == "__main__":
    game = Game()
    game.start()