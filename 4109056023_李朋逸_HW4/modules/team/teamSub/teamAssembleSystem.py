class TeamAssembleSystem():
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            print("目前在小隊內的成員為：", self.game.teamList)
            print("輸入1以查詢小隊內成員的詳細資料。")
            print("輸入2以將隊員移出小隊。")
            print("輸入3以將冒險團的成員加入小隊。")
            print("輸入4以計算你小隊的總戰力。")
            print("輸入-1退出")
            n = input()
            if n == "-1":
                break
            elif n == "1":
                self.query()
            elif n == "2":
                self.remove()
            elif n == "3":
                self.join()
            elif n == "4":
                self.analysis()
            else:
                print("輸入不正確，請重新輸入")
    
    def query(self):
        while True:
            print("目前的小隊內的成員為:",self.game.teamList)
            if len(self.game.teamList) == 0:
                print("小隊沒有成員，請加入成員")
                return 
            print("請輸入成員的編號(最左邊為0)，輸入-1退出")
            idx = input()
            if idx == "-1":
                return
            elif idx.isdigit():
                if int(idx) >= len(self.game.teamList):
                    print("成員數小於輸入的數字")
                else:
                    print("===================")
                    print("name:",self.game.teamList[int(idx)].record["name"])
                    print("hp:",self.game.teamList[int(idx)].record["hp"])
                    print("attack:",self.game.teamList[int(idx)].record["attack"])
                    print("defense:",self.game.teamList[int(idx)].record["defense"])  
                    print("===================") 
            else:
                print("輸入不為整數，請重新輸入")
        """TODO: Finish the logic here.
            查詢冒險團中對應index成員的詳細資料。"""
    def remove(self):
        while True:
            print("目前在小隊內的成員為：", self.game.teamList)
            if len(self.game.teamList) == 0:
                print("小隊裡沒有成員請加入成員")
                return
            print("請輸入成員的編號(最左邊為0)，輸入-1退出")
            idx = input()
            if idx == "-1":
                return
            elif idx.isdigit():
                if int(idx) >= len(self.game.teamList):
                    print("成員數小於輸入的數字")
                else:
                    print(self.game.teamList[int(idx)].record["name"],"回到公會休息了")
                    self.game.characterList.append(self.game.teamList[int(idx)])
                    del self.game.teamList[int(idx)]
        """TODO: Finish the logic here.
        將隊員移出小隊。"""
    
    def join(self):
        if len(self.game.teamList) > 4:
            print("隊伍的人員數量過多，請更換隊員在加入新的隊員")
            return
        while True:
            print("冒險團目前的成員有:",self.game.characterList)
            print("請輸入成員的編號(最左邊為0)，輸入-1退出")
            idx = input()
            if idx == "-1":
                break
            if int(idx) >= len(self.game.characterList):
                print("成員數小於輸入的數字")
            else:
                c = self.game.characterList[int(idx)]
                print(c.record["name"],"進入了冒險小隊中")
                self.game.teamList.append(c)
                del self.game.characterList[int(idx)]    
        if len(self.game.teamList) > 4:
            print("隊伍的人員數量過多，請更換隊員在加入新的隊員")
            return
        """TODO: Finish the logic here.
        將冒險團的成員加入小隊。"""
    def analysis(self):
        """計算小隊的總戰力。"""
        hp = 0
        attack = 0
        defense = 0
        for m in self.game.teamList:
            hp += m["hp"]
            attack += m["attack"]
            defense += m["defense"]

        print("====================\nhp: {}\nattack: {}\ndefense: {}\n====================".format(hp, attack, defense))