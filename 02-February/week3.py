"""
Project Name: IDENTITY GENERATOR
Concepts: variables, lists, functions, loops
Homework: add more flavors to the menu
"""

import random
import os
import time
from tqdm import tqdm


jobs = ["baker", "doctor", "programmer", "artist"]
fnames = ["john", "sarah", "jim", "amy"]
lnames = ["davis", "roberts", "henry", "ross"]
addresses = ["12 maple lane", "3 greene drive", "19 todd court"]



def generate_id(f,l,j,a):
  for i in tqdm(range(100)):
    time.sleep(.05)

  first = random.choice(f)
  last = random.choice(l)
  job = random.choice(j)
  adr = random.choice(a)

  os.system("clear")

  print("FIRST NAME: " + first)
  time.sleep(.5)

  print("LAST NAME: " + last)
  time.sleep(.3)

  print("JOB: " + job)
  time.sleep(.1)

  print("ADDRESS: " + adr)



os.system("clear")
generate_id(fnames,lnames,jobs,addresses)



