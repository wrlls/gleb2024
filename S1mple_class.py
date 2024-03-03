"""class Person:

    def say_hello(self):
        print("Hello")


tom = Person()
tom.say_hello()
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.kills = 20

    def set_kills(self, kills):
        self.kills = kills
class Tab:
    def __init__(self):
        self.min_kills = 10
        self.sitter = "no"
        self.broken = False

    def sit(self, person):
        if(self.min_kills < person.kills):
            broke
        self.player = person.name

    def stand(self):
        self.player = "no"

donk = Player("Gleb")
frags = Kills()

Tab.sit(donk)
print(Tab.player)
Tab.stand()
print(Tab.player)
