# HEALTHY VS UNHEALTHY


# 1. create a dictionary of foods
foods = {}
h = "healthy"
unh = "unhealthy"

# 2. add healthy foods 
foods["apple"] = h
foods["carrot"] = h
foods["beet"] = h
foods["ginger"] = h
foods["turnip"] = h



# 3. add unhealthy foods
foods["chips"] = unh
foods["hot dog"] = unh
foods["pudding"] = unh
foods["soda"] = unh



# 4. Count number of healthy foods
num_healthy = 0
num_unhealthy = 0
for f in foods:

    # grab the value of healthy/unhealthy
    health = foods[f]

    # tally healthy food
    if health == "healthy":
        num_healthy += 1

    # tally unhealthy food
    if health == "unhealthy":
        num_unhealthy += 1

# write all the healthy foods to a file
with open("healthy.txt", "w") as file:
    file.write("...Healthy Foods...\n")
    for food in foods:
        if foods[food] == "healthy":
            file.write(food + "\n")

# write all the unhealthy foods to a file
with open("unhealthy.txt", "w") as file:
    file.write("...Unhealthy Foods...\n")
    for food in foods:
        if foods[food] == "unhealthy":
            file.write(food +"\n")


# display the amount of each type of food
print("I have",num_healthy,"healthy foods")
print("I have",num_unhealthy,"unhealthy foods")






   
  















