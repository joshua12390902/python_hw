from ..card import card
import random
import time

class BattleSystem():
    class Team(card.Card):
        def damage(self, target):
            # self 攻擊 target
            aDice = self["attack"]
            dDice = target["defense"]
            a = 0
            d = 0
            for _ in range(aDice):
                a += random.randint(1, 20)
            for _ in range(dDice):
                d += random.randint(1, 20)
            
            # target受到的傷害為a-d，若a<d則受到傷害為0
            target.hurt(max(a-d, 0))

        def hurt(self, damage):
            self["hp"] = self["hp"] - damage
            print("{} 受到了 {} 點傷害，".format(self["name"], damage, self["hp"]), end = "")

        def __repr__(self):
            return "hp: {}\nattack: {}\ndefense: {}\n====================".format(self["hp"], self["attack"], self["defense"])
        def __str__(self):
            return self.__repr__()

    def __init__(self, game):
        self.stage = 1
        self.game = game
    
    def start(self):
        print("第", self.stage, "關")
        print("====================")
        player = self.getPlayerTeam()
        enemy = self.getEnemyTeam()
        print("你的隊伍:")
        print(player)
        print("對手隊伍:")
        print(enemy)
        while True:
            player.damage(enemy)
            if enemy["hp"] < 0:
                print("你贏的了勝利!")
                self.win()
                break
            print("對手剩下{}點生命".format(enemy["hp"]))
            time.sleep(1)
            enemy.damage(player)
            if player["hp"] < 0:
                print("玩家失敗!")
                break
            print("探險隊剩下{}點生命".format(player["hp"])) 
            time.sleep(1)  
        """TODO: Finish the logic here
        我方的隊伍是getPlayerTeam()回傳回來的一個Team，敵人的隊伍是getEnemyTeam()回傳回來的一個Team
        先印出兩個隊伍個別的資訊，然後開始進行戰鬥
        (1) 我方隊伍先攻擊敵方隊伍，判斷戰勝了沒，還沒的話等待一秒然後到(2)，贏了的話self.win()之後返回主頁面。
        (2) 敵方隊伍攻擊我方隊伍，判斷我方戰敗了沒，還沒的話等待一秒回到(1)，輸了話返回主頁面。"""
        
        
    def getPlayerTeam(self):
        hp = 0
        attack = 0
        defense = 0
        for m in self.game.teamList:
            hp += m["hp"]
            attack += m["attack"]
            defense += m["defense"]
        
        return self.Team(name = "探險隊", hp = hp, attack = attack, defense = defense)
    
    def getEnemyTeam(self):
        # 敵人的數值為指數性成長
        hp = 800+int(400*1.4**self.stage)
        attack = 36+int(8*1.4**self.stage)
        defense = 20+int(8*1.3**self.stage)
        return self.Team(name = "對手", hp = hp, attack = attack, defense = defense)

    def win(self):
        # for m in range(len(self.game.teamList)):
        #     self.game.teamList[m].levelUp()
        for m in self.game.teamList:
            m.levelUp()
        print("獲得{}點資源。".format(self.stage))
        self.game.resource += self.stage   
        self.stage += 1
        