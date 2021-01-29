###################################################################################################################################################
#   / _ \| |               | |    # 1. This is the second iteration of the project, which i think was said to be called 'Daft Adventure'          #
#  / /_\ \ |__   ___  _   _| |_   # 2. The aim of the project was to shorten and neaten up the codebase of the first one, whilst also making      #
#  |  _  | '_ \ / _ \| | | | __|  # headway with features that could not be added due to the poor code base of the first iteration.               #
#  | | | | |_) | (_) | |_| | |_   # 3. Basic principles such as classes, lists. json etc will be kept mostly the same, just executed differently  #
#  \_| |_/_.__/ \___/ \__,_|\__|  #                                                                                                               #
###################################################################################################################################################
# errors/notes: in CharCustom player_body and player_trait "might be referenced before assignment" no fix found yet, consult clever person when available

# Import Statements
import winsound
import time
import json
import math
import random
import pprint
from JsonVar import dungeon_descriptions

###############################################################################
# _     _     _                 _   _            _       _     _              #
#| |   (_)   | |          _    | | | |          (_)     | |   | |             #
#| |    _ ___| |_ ___   _| |_  | | | | __ _ _ __ _  __ _| |__ | | ___  ___    #
#| |   | / __| __/ __| |_   _| | | | |/ _` | '__| |/ _` | '_ \| |/ _ \/ __|   #
#| |___| \__ \ |_\__ \   |_|   \ \_/ / (_| | |  | | (_| | |_) | |  __/\__ \   #
#\_____/_|___/\__|___/          \___/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/   #
###############################################################################

## testing fight variables

current_time = 5

damage1 = 100
damage2 = 45

stamina1 = 35
stamina2 = 94

health = 0
health2 = 50

gold = 0

error_reasons = ["not a current option", "incorrect value (int/str)", "incorrect value or out of range"]

combat_options = ["attack the enemy", "flee"]
inventory = []


armour_items = ["Helmet"]


player_trait_types_damage = [10, -10, 20]
player_body_types = ["slim", "Heavy boned", "muscular"]
player_body_types_health = [70, 120, 100]
player_body_types_stamina = [140, 60, 90]
player_trait_types = ["brute", "pacifist", "intellectual"]
player_trait_types_health = [35, 0, -10]
player_trait_types_stamina = [-10, 50, 10]

available_options = []
locations = ["overworld", "dungeon1", "dungeon2", "dungeon3"]
player_location = locations[0]
available_commands_overworld = ["explore", "inventory", "help", "trade", "train"]
unlocked_dungeons = ["dungeon 1"]
####################################
# _____ _                          #
#/  __ \ |                         #
#| /  \/ | __ _ ___ ___  ___  ___  #
#| |   | |/ _` / __/ __|/ _ \/ __| #
#| \__/\ | (_| \__ \__ \  __/\__ \ #
# \____/_|\__,_|___/___/\___||___/ #
####################################

class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage



player_nothing = Weapon("Nothing", 1, 0)
wooden_sword = Weapon("Wooden Sword", 1.5, 15)
stone_sword = Weapon("Stone Sword", 2.75, 30)
iron_sword = Weapon("Iron Sword", 3.3, 60)

# Special items recieved in the boss fights of 2 and 3
boss_2_reward_weapon = Weapon("Bandit Shank", 50, 25.65)


str_inventory = []
item_in_hand = [player_nothing]


class SellableItem:
    def __init__(self, name, sell_price):
        self.name = name
        self.sell_price = sell_price


Doubloon = SellableItem("Doubloon", 40)
Garments = SellableItem("Garments", 25)
Bone = SellableItem("Bone", 10)
Vase = SellableItem("Vase", 20)
China_Vase = SellableItem("China Vase", 55)
Amethyst = SellableItem("Amethyst", 60)
Ruby = SellableItem("Ruby", 75)
Emerald = SellableItem("Emerald", 100)
Diamond = SellableItem("Diamond", 200)


items_d1 = [Doubloon, Garments, Bone, Amethyst]
items_d2 = [China_Vase, Vase, Ruby, Doubloon, Garments, Bone]
items_d3 = [China_Vase, Vase, Ruby, Diamond, Emerald, Doubloon]
item_d1 = items_d1[random.randint(0, 3)]
item_d2 = items_d2[random.randint(0, 5)]
item_d3 = items_d2[random.randint(0, 5)]
inventory_d1 = [item_d1, item_d1]
inventory_d2 = [item_d3, item_d2]
inventory_d3 = [item_d3, item_d3]
enemy_inventories = [inventory_d1, inventory_d2, inventory_d3]


# well, i'm gonna add more stuff later

class Armour:
    def __init__(self, name, price, health_mult):
        self.name = name
        self.price = price
        self.health_mult = health_mult

wooden_armour = Armour("Wooden Armour", 5, 1.025)
chainmail_armour = Armour("Chainmail Armour", 50, 1.25)
iron_armour = Armour("Iron Armour", 220, 1.55)

class Enemy:
    def __init__(self, name, health, damage, stamina):
        self.name = name
        self.damage = damage
        self.health = health
        self.stamina = stamina


class Trader:
    def __init__(self, name, sell_mult, buy_mult):
        self.name = name
        self.sell_mult = sell_mult
        self.buy_mult = buy_mult

dungeon1_trader = Trader("Drake Divide Dividend", 1.05, 1.05)



goblin = Enemy("goblin", 60, 5, 80)
troll = Enemy("troll", 100, 15, 60)
hobbit = Enemy("hobbit", 50, 20, 120)
wizened_wizard = Enemy("wizened wizard", 30, 55, 50)
bandit = Enemy("bandit", 60, 10, 100)
agile_bandit = Enemy("agile bandit", 75, 15, 140)
bulky_bandit = Enemy("bulky bandit", 105, 60, 70)
corrupted_lord = Enemy("CORRUPTED LORD", 250, 100, 500)
boss_1 = Enemy("goblin king", 175, 5, 120)
boss_2 = Enemy("Bandit Camp Leader", 145, 45, 225)
boos_3 = Enemy("Wizard Of The Warp", 250, 59.54385, 100000000000000**2)

dungeon1_enemies = [goblin, troll, hobbit]
dungeon2_enemies = [troll, bandit, bulky_bandit, agile_bandit]
dungeon3_enemies = [bulky_bandit, agile_bandit, wizened_wizard, corrupted_lord]

####################################################
#   ______                _   _                    #
#   |  ___|              | | (_)                   #
#   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___    #
#   |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|   #
#   | | | |_| | | | | (__| |_| | (_) | | | \__ \   #
#   \_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/   #
####################################################
def GameMenuAscii():

    print(" ______   _______  _______ _________   _______  ______            _______  _       _________          _______  _______")
    print("(  __  \ (  ___  )(  ____ \\__   __/  (  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____   ")
    print("| (  \  )| (   ) || (    \/   ) (     | (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/")
    print("| |   ) || (___) || (__       | |     | (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (____ ")
    print("| |   | ||  ___  ||  __)      | |     |  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  ____")
    print("| |   ) || (   ) || (         | |     | (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | ( ")
    print("| (__/  )| )   ( || )         | |     | )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/ ")
    print("(______/ |/     \||/          )_(     |/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/")

    winsound.PlaySound("MenuMusic.wav", winsound.SND_ASYNC) # Plays music

def GameMenu(): # menu of the game. pretty simple. First thing the player sees when entering the game
    GameMenuAscii()
    menu_input = input("\nenter 's' to start 'l' to load last save or 'q' to quit\n")
    while True:
        try:
            if menu_input == "s":
                winsound.PlaySound(None, winsound.SND_PURGE) # plays nothing, and purges (deletes) any music currently playing
                Main()
            elif menu_input == "q":
                break
            else:
                print(f"invalid, {error_reasons[0]}")
        except ValueError:
            print(f"invalid, {error_reasons[1]}")

def Main(): # main game program
    IntroSequence()
    CharCustom()
    MainGameLoop()

def IntroSequence():
    global list
    list = ["Hello there my fellow traveller! \n", "Welcome to a new, exciting and interesting adventure! \n", "On this rather daft, dumb and rather silly exploration of a world of those same qualities, you'll encounter a variety of many, many, many things \n" , "Monsters, idiotic traders, half arsed villagers, it goes on! \n", "But before we can do any of this... \n"]
    for i in list:
        print(i)
        time.sleep(3.15)

def CharCustom():
    global damage1
    global stamina1
    while True:
        player_name = input("Firstly, lets define your name!\n> ")
        print("Excellent! Now for you and how you view yourself")
        player_trait = int(input("Now tell me, are you a brute [0], a pacifist [1] or an intellectual? [2]\n> "))
        player_body = int(input("Now for your body type! Do you see yourself as being slim [0], heavy boned [1] or muscular? [2]\n> "))
        if player_body == 1 or 2 or 3 and player_trait == 1 or 2 or 3:
            health = player_body_types_health[player_body] + player_trait_types_health[player_trait]
            stamina1 = player_body_types_stamina[player_body] + player_trait_types_stamina[player_trait]
            damage1 = player_trait_types_damage[player_trait] + 20
            print(f"health - {health}\nstamina - {stamina1}\ndamage - {damage1}")
            print(f"Thank You.  \n\n From what i can gather from you {player_name}, You're known to be  a {player_body_types[player_body]} {player_trait_types[player_trait]} from the sounds of things... \n Well, time to start your Daftest of all daft adventures!")
            print(f"Well {player_name}. Get ready. Your adventure starts now. You will be thrown into a world of chaos and confusion. If you don't know what to do, simply type Help \n and a helpful message will appear with all the options you can do. \n Good luck! \n \n \n")

            break
        break
def MaxInvSpace():
    if len(inventory) > 20:
        print("you can't pick up anymore weapons!")
        inventory.remove(inventory[60])

def StringInventory(current_inventory):
    str_inventory.clear()
    for i in current_inventory:
        str_inventory.append(i.name)

def CheckInventory():
    global damage, item_in_hand
    inventory_input = input("what would you like to do in your inventory?\n1. drop an item\n2. equip an item\n3. look in your inventory> ")
    if inventory_input == "1":
        StringInventory()
        print(str_inventory)
        drop_input = int(input(f"which item would you like to drop?\n> "))
        inventory.remove(inventory[drop_input-1])
        print(inventory)
    elif inventory_input == "2":
        StringInventory(inventory)
        switch_input = int(input(f"which item would you like to equip?\n{str_inventory}\n> "))
        item_in_hand.clear()
        item_in_hand.append(inventory[switch_input-1])
        print(item_in_hand[0].name)
        damage = damage * item_in_hand[0].damage
        print(damage)
    elif inventory_input == "3":
        for i in inventory:
            print(i.name)
    else:
        print("That ain't an option dear! Try again")


def TradingFunction():
    trading_commands = ["buy", "sell"]
    while True:
        trading_command = input("What would you like to do? You can trade or sell")
        if trading_command == trading_commands[0].lower() or trading_commands[0].capitalize():
            pass

def DungeonMenu():
    dungeon_input = input("choose which dungeon you would like to go to 1, 2 or 3 (once you've unlocked them)\n> ")
    if dungeon_input == 1:
        Dungeon1()
    elif dungeon_input == 2 and "dungeon 2" == unlocked_dungeons:
        Dungeon2()
    elif dungeon_input == 3 and "dungeon 3" == unlocked_dungeons:
        print("haha, peepee poopoo")


def MainGameLoop():
    inventory.append(player_nothing)
    while True:
        player_command = input("what would you like to do\n> ")
        if player_location == locations[0]:
            available_options.append(available_commands_overworld)
            if player_command == available_commands_overworld[0]:
                DungeonMenu()
            elif player_command == available_commands_overworld[1]:
                CheckInventory()
            elif player_command == available_commands_overworld[2]:
                print("Need Help? well. Here are the things commands you can type and do: \n 1. 'Explore' to go to the next room or dungeon (If you've completed the previous dungeon) \n 2.'Inventory' to check your inventory and to swap things \n 3: Trade (if in a trading den) Opens up a trading menu so you can buy and sell stuff, at a higher or lower price \n")
            elif player_command == available_commands_overworld[3]:
                print("wip")
            elif player_command == available_commands_overworld[4]:
                print("wip")

# anything below this is to do with combat.

def MaxHealth():
    global health
    max_health = health + player_trait_types_health + player_body_types_health
    if health > max_health:
        health = max_health

    return max_health

def Die():
    global player_location
    inventory.clear()
    player_location = locations[0]

def Fight(health2, damage2, stamina2, name, dungeon):
    global health1, damage1, stamina1
    combat_options = ["attack the enemy", "flee"]
    while True:
        user_input = int(input(f"you have {len(combat_options)} options, choose from them using their indexes\n{combat_options}\n> "))
        if user_input > len(combat_options) or user_input < 0:
            print("invalid, out of range")
        else:
            if user_input == 0:
                while True:
                    fight_input = int(input("press '0' to attack, '1' to use a heal spell (if you have enough stamina)\n> "))
                    if fight_input == 0:
                        health2 = health2 - damage1
                        health1 = health1 - damage2
                        print(f"you damaged the {name} for {damage1} damage\n{name}'s health - {health2}\nyour health - {health1}")
                        if health1 > 0 and health2 > 0:
                            pass
                        elif health1 <= 0:
                            print("you lost!")
                            Die()
                        elif health2 <= 0:
                            print("you won!")
                            break
                    elif fight_input == 1 and stamina1 > 20:
                        health1 = health1 + 25
                        stamina1 = stamina1 - 20
                        MaxHealth()
                        print(f"you healed 25 health, the {name} damaged you for {damage2}\n{name}'s health - {health2}\nyour health - {health1}")
                        if health1 > 0 and health2 > 0:
                            pass
                        elif health1 <= 0:
                            print("you lost!")
                            Die()
                            health2 = 0
                        elif health2 <= 0:
                            print("you won!")
                            break
                StringInventory(enemy_inventories[dungeon])
                inv_input = int(input(
                    f"congratulations! you won the battle, which of these items would you like to take with you on your travels\n{str_inventory}\n> "))
                if inv_input > len((enemy_inventories[dungeon])) or inv_input < 0:
                    print("invalid, out of range")
                elif len(inventory) >= 20:
                    MaxInvSpace()
                else:
                    inventory.append((enemy_inventories[dungeon])[inv_input])
                    StringInventory(inventory)
                    print(str_inventory, "\n")
                    break
            elif user_input == 1:
                if stamina1 - stamina2 < 0:
                    print(f"the {name} approaches you, you are forced to fight it")
                    while True:
                        fight_input = int(input(f"press '0' to attack, '1' to use a heal spell (required stamina - 20, your stamina - {stamina1}\n> "))
                        if fight_input == 0:
                            health2 = health2 - damage1
                            health1 = health1 - damage2
                            print(f"you damaged the {name} for {damage1} damage\n{name}'s health - {health2}\nyour health - {health1}")
                            if health1 > 0 and health2 > 0:
                                pass
                            elif health1 <= 0:
                                print("you lost!")
                                Die()
                                health2 = 0
                            elif health2 <= 0:
                                print("you won!")
                                health2 = 0
                                break
                        elif fight_input == 1 and stamina1 > 20:
                            health1 = health1 + 25
                            stamina1 = stamina1 - 20
                            MaxHealth()
                            print(f"you healed 25 health, the {name} damaged you for {damage2}\n{name}'s health - {health2}\nyour health - {health1}")
                            if health1 > 0 and health2 > 0:
                                pass
                            elif health1 <= 0:
                                print("you lost!")
                                Die()
                                health2 = 0
                            elif health2 <= 0:
                                print("you won!")
                                health2 = 0
                                break
                    StringInventory(enemy_inventories[dungeon])
                    inv_input = int(input(f"congratulations! you won the battle, which of these items would you like to take with you on your travels\n{str_inventory}\n> "))
                    if inv_input > len((enemy_inventories[dungeon])) or inv_input < 0:
                        print("invalid, out of range")
                    elif len(inventory) >= 20:
                        MaxInvSpace()
                    else:
                        inventory.append((enemy_inventories[dungeon])[inv_input])
                        StringInventory(inventory)
                        print(str_inventory, "\n")
                        break
                elif stamina1 - stamina2 >= 0:
                    print(f"you managed to outrun the {name}! oh how thrilling that must've been\n")

# dungeons

def count_down():
    global current_time
    for i in range(5):
        time.sleep(1)
        print(current_time)
        current_time = current_time - 1

def Dungeon1():
    global gold
    rand1 = random.randint(0, 2)
    rand2 = random.randint(0, 2)
    rand3 = random.randint(0, 2)
    print(dungeon_descriptions[0]) # intro to the dungeon
    time.sleep(3)
    Fight(dungeon1_enemies[rand1].health, dungeon1_enemies[rand1].damage, dungeon1_enemies[rand1].stamina, dungeon1_enemies[rand1].name, 1)
    #Some transitional text. will be done in json soon
    time.sleep(3)
    Fight(dungeon1_enemies[rand2].health, dungeon1_enemies[rand2].damage, dungeon1_enemies[rand2].stamina, dungeon1_enemies[rand2].name, 1)
    #Some transitional text. will be done in json soon
    time.sleep(3)
    Fight(dungeon1_enemies[rand3].health, dungeon1_enemies[rand3].damage, dungeon1_enemies[rand3].stamina, dungeon1_enemies[rand3].name, 1)
    print("\nDialogue introducing the boss 'n crap\n")

    count_down()

    Fight(boss_1.health, boss_1.damage, boss_1.stamina, boss_1.name)
    print("\ncongrats! you completed dungeon 1. You have unlocked trade and found 100 gold in a chest\n")
    unlocked_dungeons.append("Dungeon 2")
    gold = gold + 100

def Dungeon2():
    # gold has already been globalled
    rand1 = random.randint(0, 2)
    rand2 = random.randint(0, 2)
    rand3 = random.randint(0, 2)
    print(dungeon_descriptions[1])
    time.sleep(3)
    Fight(dungeon2_enemies[rand1].health, dungeon2_enemies[rand1].damage, dungeon2_enemies[rand1].stamina, dungeon2_enemies[rand1].name, 1)
    #Some transitional text. will be done in json soon
    time.sleep(3)
    Fight(dungeon2_enemies[rand2].health, dungeon2_enemies[rand2].damage, dungeon2_enemies[rand2].stamina, dungeon2_enemies[rand2].name, 1)
    #Some transitional text. will be done in json soon
    time.sleep(3)
    Fight(dungeon2_enemies[rand3].health, dungeon2_enemies[rand3].damage, dungeon2_enemies[rand3].stamina, dungeon2_enemies[rand3].name, 1)

    count_down()

    Fight(boss_2.health, boss_2.damage, boss_2.stamina, boss_2.name)
    print(f"\n congrats! The ")

# testing
inventory.append(wooden_sword.name)

GameMenu() # puts the player in the menu!

#Fight(goblin.health, goblin.damage, goblin.stamina, goblin.name)
