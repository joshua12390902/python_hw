from ..card import card

class LootSystem():
    def __init__(self, game):
        self.game = game
    
    def start(self):
        while True:
            print("==========抽卡模式==========")
            print("你目前擁有的資源有：", self.game.resource)
            if self.game.resource <= 0:
                print("資源不足，離開抽卡模式")
                print("====================")
                break
            n = input("輸入你希望消費的資源(-1退出抽卡模式)：")
            if n == "-1":
                break
            elif n.isdigit():
                n = int(n)
                if n > 0:
                    """TODO: Finish the logic here.
                    假如輸入的資源沒有超過你持有的資源，那麼付出對應的資源並抽對應強度的卡片。
                    否則print('(需要更多資源才能進行這個操作。')。"""
                    if n <= self.game.resource:
                        self.draw(n)
                        self.game.resource -= n
                    else:
                        print('(需要更多資源才能進行這個操作。')
                else:
                    print("至少要花費1點資源才能抽卡，請重新輸入")
            else:
                print("輸入不為整數，請重新輸入")
    
    def draw(self, res):
        c = card.Card(resource = res)
        print("隨著一道光芒顯現……")
        print(c)
        self.game.characterList.append(c)
        print("{}成為冒險團的夥伴了！".format(c["name"]))