import random; import math; import time
print("\n--- NPC GENERATOR ---\n")
time.sleep(2)

x = 0 # placeholder
number_of_npcs = 10

number_of_attributes = int(input("How many attributes do you want per NPC (1-5): "))
if number_of_attributes <= 5 and number_of_attributes >= 1:
    x = 1 # buffer
else:
    print("BAD INPUT! RESTART!")
    exit() # kills project

names = ["Alex", "Jordan", "Taylor", "Morgan", "Riley", "Cameron", "Avery", "Casey", "Jamie", "Skyler", "Sam", "Chris", "Drew", "Logan", "Harper", "Ember", "Kai", "Luna", "Noah", "Mila", "Ethan", "Aria", "Zane", "Sage", "Leo", "Nova", "Rex", "Ivy", "Nico", "Finn", "Mango", "Mustard", "67", "Popatlaal"] # names list
attributes = ["strength", "intelligence", "speed", "agility", "charisma", "endurance", "wisdom", "luck", "creativity", "patience", "honesty", "kindness", "confidence", "discipline", "focus", "bravery", "determination", "loyalty", "stealth", "perception", "accuracy", "balance", "resilience", "stamina", "morality", "sigma", "rizzy", "alpha", "Σ"] # attributes list

for i in range(number_of_npcs): # running this loop however amount of characters you wanted
    height = random.randint(40, 70) / 10 # height randomizing
    tuff = random.randint(0,2) # tuff randomizing
    print("NPC " + str(i + 1) + ":\nName: " + random.choice(names))
    for j in range(number_of_attributes): # running this loop however amount of attributes you wanted
        print("Attributes: " + random.choice(attributes))
    print("Height: " + str(height) + "'") # height print
    print("Is tuff?: " + str(bool(tuff))) # tuff print
    time.sleep(1)