class Player:
    def __init__(self,name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
#Creating an object of the class Player
player1 = Player("Alice", 100)
player1.take_damage (20)
print(f"{player1.name}'s health : {player1.health}")