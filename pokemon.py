import random
import time
import string

class Pokemon:
    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

def newPokemon():
    name = input("Pokemon Name: ")
    type = input("Pokemon Type: ")
    hp = 50
    return string.capwords(name), string.capwords(type), hp

def player1():
    newPoke = newPokemon()
    pokemon = Pokemon(newPoke[0], newPoke[1], newPoke[2])
    return pokemon

def player2():
    newPoke = newPokemon()
    pokemon = Pokemon(newPoke[0], newPoke[1], newPoke[2])
    return pokemon

def rest(playerPoke):
    hp_regenerate = random.randint(1, 10)
    print("\n{} use Rest!\nYour Pokemon recover {} hp!".format(playerPoke, hp_regenerate))

    time.sleep(1)

    return hp_regenerate

def attack(playerPoke, attacking_type, defending_type):
    damage = random.randint(10, 15)
    print("\n{} attack!".format(playerPoke))

    time.sleep(1.5)

    if (attacking_type == "Fire" and defending_type == "Water") or (attacking_type == "Water" and defending_type == "Grass") or (attacking_type == "Grass" and defending_type == "Fire"):
        damage -= 2

    elif (attacking_type == "Water" and defending_type == "Fire") or (attacking_type == "Fire" and defending_type == "Grass") or (attacking_type == "Grass" and defending_type == "Water"):
        damage += 3

    elif attacking_type == defending_type:
        pass

    critical = random.randint(0, 1)
    if critical == 1:
        damage *= 1.5
        print("..\nCritical!")
        time.sleep(1)

    else:
        pass

    print("..\nYour Pokemon dealt {} damage!".format(damage))
    return damage

def Match(turnPlayerPoke, waitPlayerPoke):
    time.sleep(2)
    decide = int(input("What would you like {} to do?\n(1) Rest\n(2) Attack\n".format(turnPlayerPoke.name)))
    if decide == 1:
        hp = rest(turnPlayerPoke.name)
        turnPlayerPoke.hp += hp
        
        time.sleep(2)

        print("\n{} is currently at {} hp".format(turnPlayerPoke.name, turnPlayerPoke.hp))
        print("{} is currently at {} hp".format(waitPlayerPoke.name, waitPlayerPoke.hp))
        
    elif decide == 2:
        damage = attack(turnPlayerPoke.name, turnPlayerPoke.type, waitPlayerPoke.type)
        waitPlayerPoke.hp -= damage

        time.sleep(2)

        print("\n{} is left with {}".format(waitPlayerPoke.name, waitPlayerPoke.hp))
        print("{} is currently at {} hp".format(turnPlayerPoke.name, turnPlayerPoke.hp))

    return "\nEnd of {} turn.".format(turnPlayerPoke.name)

## Match Preparation
print("\nPlayer 1 declare your pokemon!")
player_1 = player1()

time.sleep(0.25)

print("\nPlayer 2 declare your pokemon!")
player_2 = player2()

## Match Start
player_start = random.randint(1, 2)

## Match Ongoing
ongoing = 1
while ongoing:
    if player_1.hp <= 0:
        time.sleep(3)
        print("\nCongratulation Player 2 wins with {}!\n".format(player_2.name))
        break

    elif player_2.hp <= 0:
        time.sleep(3)
        print("\nCongratulation Player 1 wins with {}!\n".format(player_1.name))
        break
    
    else:
        if player_start == 1:
            print("\nPlayer 1 turn!")
            print(Match(player_1, player_2))
            player_start = 2
        elif player_start == 2:
            print("\nPlayer 2 turn!")
            print(Match(player_2, player_1))
            player_start = 1