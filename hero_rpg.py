#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, name, health, power, death):
        self.name = name
        self.health = health
        self.power = power
        self.death = death
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("There is {} health and {} power remaining to {}.".format(self.health, self.power, self.name))
    def begin_attack(self, enemy):
        enemy.health -= self.power
        print("POW! {} damage is done to {}".format(self.power, enemy.name))
        if enemy.health <= 0:
            print(enemy.death)
            
        
class Hero(Character):
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    
        
        
class Goblin(Character):
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
    
hero = Hero("you", 10, 5, "You died!")
goblin = Goblin("the goblin", 6, 2, "The goblin is vanquished!")

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        # Hero attacks goblin
        hero.begin_attack(goblin)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

    if goblin.alive():
        # Goblin attacks hero
        goblin.begin_attack(hero)

main()
