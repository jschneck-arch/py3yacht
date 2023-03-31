import time
import random

# Introduction
Print("Yacht Rock! The Smoothest Adventure")
print("Youfind yourself transported back to the 1980s, where you shall embark on a musical journey set to the smooth tunes of the Yacht Rock Universe.")
time.sleep(2)
print("Your adventure begins now!")

# Character creation
name = input("whats your name, traverser of the smooth?")
print("welcome aboard the seas of smooth,", name, "!")
time.sleep(1)

# Character sheet
print ("Let's see how sea worthy you are!")
time.sleep(1)
print("Strength (STR): determines your physical power")
print("Dextarity (DEX): determines your speed and agility")
print("Constitution (CON): determines your health and endurance")
print("Charisma (CHA): determines your social skills and charm")
time.sleep(2)

# Ability allocation
abilities = {"STR": 0, "DEX": 0,"CON": 0,"CHA": 0}
points_left = 20
while points_left > 0:
    print("Points left: ", points_left)
    ability = input("Which ability would you like to allocate points to?  Type 'STR, 'DEX, 'CON', or 'CHA' and press Enter.")
    if ability not in abilities:
        print("My apologies, please try again.")
        continue
    points = int(input("How many points would you like to allocate to "+ ability + "?"))
    if points > points_left:
        print("You do not have enough points. Please try again.")
        continue
    abilities[ability] += points
    points_left -= points

# Game setup
inventory = []
current_room = "foyer"
health = abilities["CON"] * 5 

# Game logic and room descriptions
while True:
    if current_room == "foyer":
        print("You are in the foyer of a concert hall. The music is smooth and the crowd is drifting in a sea of good vibes.")
        print("There are two doors in front of you: one to your left an one to your right.")
        print("Where would you like to go?")
        direction = input("Type 'left' or 'right' and press Enter.")
        if direction == "left":
            current_room = "backstage"
        elif direction == "right":
            current_room = "dance floor"
        else:
            print("My apologies, please try again.")
            continue
    elif current_room == "backstage":
        print("You have found your way backstage! There is a Doobie Brothers concert poster on the wall.")
        print("You see a guitar and a drum set. Which one would you like to play?")
        instrument = input("Type 'guitar' or 'drums' and press Enter.")
        if instrument == "guitar":
            print("You picked up the guitar and start playing. The crowd goes wild!")
            inventory.append("guitar pick")
            current_room = "foyer"
        elif instrument == "drums":
            print("You sit down at the drums and start playing. The rhythm is infectious!")
            inventory.append("drumstick")
            current_room = "foyer"
        else:
            print("My apologies, please try again.")
            continue
    elif current_room =="dance floor":
        print("You are on the dance floor! The lights are flashing and the music is smooth.")
        print("You notice a group of pretentious yacht rockers approaching your direction. They look tough and ready for a fight.")
        time.sleep(2)
        print("You must fight them to proceed!")
        time.sleep(2)

# Enemies
    enemies = {
        "Michael McDonald": {"AC": 12, "HP": 20, "STR": 14, "DEX": 10, "CON": 12, "ATTACK": 4, "DAMAGE": 6},
        "Kenny Loggins": {"AC": 14, "HP": 25, "STR": 12, "DEX": 14, "CON": 10, "ATTACK": 3, "DAMAGE": 8},
        "Toto": {"AC": 16, "HP": 30, "STR": 10, "DEX": 12, "CON": 14, "ATTACK": 2, "DAMAGE": 10}
    }

# Character sheet
    print("Here's your character sheet:")
    time.sleep(1)
    print("Name:", name)
    print("Class: Yacht Rocker")
    print("Health:", health)
    print("Inventory:", inventory)
    print("Abilities:")
    for ability, score in abilities.items():
        print(ability + ":", score)
    time.sleep(2)

# Battle
    while True:
# Player turn
        print("Your turn!")
        time.sleep(1)
        print("What do you want to do?")
        action = input("Type 'attack' to attack or 'heal' to restore some health. ")
        if action == "attack":
            enemy = random.choice(list(enemies.keys()))
            print("You attack", enemy, "with your trusty guitar!")
            time.sleep(1)
            roll = random.randint(1, 20)
            attack = roll + abilities["STR"] + 2  # add 2 for proficiency bonus
            if attack >= enemies[enemy]["AC"]:
                damage = random.randint(1, 6) + abilities["STR"]
                enemies[enemy]["HP"] -= damage
                print("You hit", enemy, "for", damage, "damage!")
                time.sleep(1)
                if enemies[enemy]["HP"] <= 0:
                    print(enemy, "is defeated!")
                    del enemies[enemy]
                    time.sleep(1)
                if not enemies:
                    print("You have defeated all enemies! Congratulations!")
                    break
            else:
                print("You missed!")
                time.sleep(1)
        elif action == "heal":
            if "bandage" in inventory:
                health += 5
                inventory.remove("bandage")
                print("You use a bandage to heal for 5 HP. Current health:", health)
                time.sleep(1)
            else:
                print("You don't have a bandage to heal with.")
                time.sleep(1)
        else:
            print("Sorry, I didn't understand that. Please try again.")
            continue

# Enemy turn
        print("Enemy turn!")
        time.sleep(1)
        for enemy, stats in enemies.items():
            print(enemy, "attacks you!")
            time.sleep(1)
            roll = random.randint(1, 20)
            attack = roll + stats["ATTACK"]
            if attack >= abilities["DEX"]:
                damage = random.randint(1, stats["DAMAGE"])
                health -= damage
                print(enemy, "hits you for", damage, "damage! Current health:", health)
                time.sleep(1)
                if health <= 0:
                    print("Game over! You have been defeated.")
                    quit()
            else:
                print(enemy, "misses!")
                time.sleep(1)

elif choice == "3":
    print("Thanks for playing! Goodbye.")
    quit()

else:
    print("Sorry, I didn't understand that. Please try again.")
    continue
