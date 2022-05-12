# lists are expandable data structures
# that can hold, remove, and modify data


# we can start off with an empty list
# and add more data, or we can pre fill
# data into our list
places = ["USA", "Mexico", "Canada"] #pre fill
places = [] # empty
# you can update a list just like a variable
# the list is now empty.

# can add data using the append method
places.append("USA")
places.append("Mexico")
places.append("Canada")
places.append("Monaco")
print(places)


# i can remove data
places.remove("Monaco")
print(places)

# i can find out the order of my list
# using list index (indices)

# first item of a list is index zero
first = places[0]
print("My first country is " + first)

# last item of a list is index -1
last = places[-1]
print("My last country is " + last)


# if you try to reference an index that doesnt
# exist you will get an error


# to catch errors. we use try - except

try:
  print (places[5]) # there is no fifth index
except:
  print("You dont have a fifth index")








