print("This is my self profile")
gender = "male" # This is a string data type
name = "yousef"
age = 26 #this is an integer data type
interests = ["skateboarding","music", "cars", "video games"]

# a function is a series of 
# commands that come together 
# to make one command

# first define the function 
def self_profile(g,n,a,i):
  print("My name is " + n)
  print("I am a " + g)
  print("I am " + str(a) + " years old")
  print("MY interests include")
  for interests in i:
    print(interests)
  
# now we call the function
self_profile(gender,name,age,interests)
  
