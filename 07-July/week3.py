"""
Project Name: NFL PLAYER GENERATOR
Concepts: lists, loops, tqdm lib
Homework: add more names, positions, and teams
"""
import os
import time
import random
from tqdm import tqdm

names = ["mark jones", "james amer", "tim duff", "bill waters", "jaden remly"]
positions = ["quarterback", "running back", "linebacker", "center","wide reciever", "tailback"]
teams = ["chiefs", "patriots", "giants", "jets", "titans"]

for i in tqdm(range(100)):
    time.sleep(.1)
    os.system("clear")
    
    print("PLAYER GENERATOR")
    name = random.choice(names)
    position = random.choice(positions)
    team = random.choice(teams)
    speed = random.randint(1,10)
    agility = random.randint(1,10)
    catching = random.randint(1,10)
    
    
    print("Name:", name)
    print("Position:" ,position)
    print("Team:" ,team)
    print("Speed:",speed)
    print("Agility:",agility)
    print("Catching:",catching)