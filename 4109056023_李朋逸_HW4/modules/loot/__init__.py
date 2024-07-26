from .lootSystem import LootSystem

if __name__ == "__main__":
    print("test loot system.")

    class tmpGame():
        def __init__(self):
            self.resource = 10
            self.characterList = []
    
    TG = tmpGame()
    LS = LootSystem(TG)
    LS.start()