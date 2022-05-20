# TYPING TEST

import time
import os

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = int(mins // 60)
    mins = int(mins % 60)
    print("Time Lasped = {0}:{1}:{2}".format(hours, mins, sec))


input("Press Enter to start")
start_time = time.time()
file = open("sentence1.txt", "r")
sentence = "I will go to the supermarket to get some food later"
sentence = sentence.split()
typed = []
index=0


while True:
  os.system("clear")
  print(sentence)
  print("Typed:", typed)
  word = input("Type!")
  if word ==  sentence[index]:
    typed.append(word)
    index+=1
  
  if sentence == typed:
    break

end_time = time.time()
time_lasped = end_time - start_time
time_convert(time_lasped)