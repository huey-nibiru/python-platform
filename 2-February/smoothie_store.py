# CREATE A RESTAURANT NAME
name = "Sams Smoothies"

print("Welcome to " + name)

# MAKE A MENU DICTIONARY
menu = { }
menu["Banana Sherbert"] = 10
menu["Orange"] = 11
menu["Celery"] = 9
menu["vanilla"] = 17
menu["Mango Munky"] = 7
menu["Red Apple"] = 3
menu["blue Raspberry"] = 5
menu["green apple"] = 20



print("\n")
print("..........MENU..........")
for flavor in menu:
  price = str(menu[flavor])
  print(flavor + "....$" + price)
print("........................")  
  
  
  
total = 0  
while True:
  choice = input("Select a flavor:")
  if choice in menu:
    price = menu[choice]
    print("That will be $" + str(price))
    total += price
    
    while True:
      more = input("AnYthInG eLSe?")
  
      if more == "n":
        print("OK")
        print("Total is $" + str(total))
        print("Card/Crypto Only.")
        exit(0)
      else:
        
          price = menu[choice]
          print("That will be $" + str(price))
          total += price
        
  
  
  
  
  
  
  
  
  



















