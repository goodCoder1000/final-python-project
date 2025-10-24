import random
import math
import time

print("--- NPC GENERATOR ---\n")

number_of_npcs = int(input("How many NPCS do you want (1-10): "))
number_of_attributes = int(input("How many attributes do you want per NPC (1-5): "))

names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Riley", "Cameron",
    "Avery", "Casey", "Jamie", "Skyler", "Sam", "Chris", "Drew",
    "Logan", "Harper", "Ember", "Kai", "Luna", "Noah", "Mila",
    "Ethan", "Aria", "Zane", "Sage", "Leo", "Nova", "Rex", "Ivy",
    "Nico", "Finn", "67 mango", "sigma ohio rizzler", "amogus bum bum bum bumb mu bumb um bababum bum bum"
]

attributes = [
    "strength", "intelligence", "speed", "agility", "charisma",
    "endurance", "wisdom", "luck", "creativity", "patience",
    "honesty", "kindness", "confidence", "discipline", "focus",
    "bravery", "determination", "loyalty", "stealth", "perception",
    "accuracy", "balance", "resilience", "stamina", "morality",
    "sigma", "rizzy", "a good boy", "alpha", "Σ", "a duck walked up to a lemonade stand and he said to the man, running the stand, HEY bum bum bum, got any grapes? badabum bum bum bum badum"
]

float height = random.randint(40, 70) / 10
for i in range(number_of_npcs):
    print("NPC " + str(i + 1) + ":\nName: " + random.choice(names))
    for j in range(number_of_attributes):
        print("Attributes: " + random.choice(attributes))
    print("Height: ", height + "'\n")