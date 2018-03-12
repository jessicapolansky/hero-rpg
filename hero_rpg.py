#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
        
class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
hero = Hero()
goblin = Goblin()

while goblin.alive() and hero.alive():
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        # Hero attacks goblin
        hero.attack(goblin)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

    if goblin.health > 0:
        # Goblin attacks hero
        goblin.attack(hero)

main()
