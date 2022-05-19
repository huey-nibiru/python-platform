# IDENTITY GENERATOR

import random
import os
import time
import string
from tqdm import tqdm


# Before you begin, create the following files:
# - firstnames.txt (add 5 fake first names to the file)
# - lastnames.txt (add 5 fake last names to the file)
# - jobs.txt (add 5 fake jobs to the file)
# - addresses.txt (add 5 fake addresses to the file)



jobs = []
fnames = []
lnames = []
addresses = []



# SCAN THE FILES TO IMPORT ALL VALUES TO THEIR LIST
def scan_files(fileName, list):
    with open(fileName, "r") as file:
        for content in file:
            content = content.strip("\n")
            content = content.lower()
            list.append(content)


scan_files("firstnames.txt", fnames)
scan_files("lastnames.txt", lnames)
scan_files("jobs.txt", jobs)
scan_files("addresses.txt", addresses)


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



