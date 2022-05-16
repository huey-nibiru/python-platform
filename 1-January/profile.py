# create a variable that holds information for a person. [review data types with class]
name = "yousef"
age = 26 #this is an integer data type
hobbies = ["skateboarding","music", "cars", "video games"]


# create a function that takes in three parameters for the name, age, and interests [review parameters]
def self_profile(n,a,h):
  print("My name is " + n)
  print("I am " + str(a) + " years old")

  # briefly go over the join() method
  print("My hobbies include: " + ", ".join(h))
  
  
# now we call the function to output the results
self_profile(name,age,hobbies)

  
