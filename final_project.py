import random; import math; import time
print("--- NPC GENERATOR ---\n")
time.sleep(2)

x = 0 # placeholder
number_of_npcs = int(input("How many NPCS do you want (1-10): "))
if number_of_npcs <= 10 and number_of_npcs >= 1:
    x = 1 # buffer
else:
    print("BAD INPUT! RESTART!")
    exit() # kills project

number_of_attributes = int(input("How many attributes do you want per NPC (1-5): \n"))
if number_of_npcs <= 5 and number_of_npcs >= 1:
    x = 1 # buffer
else:
    print("BAD INPUT! RESTART!")
    exit() # kills project

names = ["Alex", "Jordan", "Taylor", "Morgan", "Riley", "Cameron", "Avery", "Casey", "Jamie", "Skyler", "Sam", "Chris", "Drew", "Logan", "Harper", "Ember", "Kai", "Luna", "Noah", "Mila", "Ethan", "Aria", "Zane", "Sage", "Leo", "Nova", "Rex", "Ivy", "Nico", "Finn", "67 mango", "sigma ohio rizzler", "amogus bum bum bum bumb mu bumb um bababum bum bum"] # names list
attributes = ["strength", "intelligence", "speed", "agility", "charisma", "endurance", "wisdom", "luck", "creativity", "patience", "honesty", "kindness", "confidence", "discipline", "focus", "bravery", "determination", "loyalty", "stealth", "perception", "accuracy", "balance", "resilience", "stamina", "morality", "sigma", "rizzy", "a good boy", "alpha", "Σ", "a duck walked up to a lemonade stand and he said to the man, running the stand, HEY bum bum bum, got any grapes? badabum bum bum bum badum"] # attributes list

for i in range(number_of_npcs): # running this loop however amount of characters you wanted
    height = random.randint(40, 70) / 10 # height randomizing
    tuff = random.randint(0,2) # tuff randomizing
    print("NPC " + str(i + 1) + ":\nName: " + random.choice(names))
    for j in range(number_of_attributes): # running this loop however amount of attributes you wanted
        print("Attributes: " + random.choice(attributes))
    print("Height: " + str(height) + "'") # height print
    print("Is tuff?: " + str(bool(tuff)) + "\n") # tuff print