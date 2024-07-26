from .card import Card

if __name__ == "__main__":
    tmp = Card()
    print(tmp)
    print("name", tmp["name"])
    print("hp", tmp["hp"])
    print("attack", tmp["attack"])
    print("defense", tmp["defense"])