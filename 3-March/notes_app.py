import os,time
# dictionaries hold info with a key and value

#              KEY       VALUE
account1 = {"username":"PY_GUY",
            "password":"python3"}
  
# to show a username we will do this
#print(account1["username"])

# create the menu 
def menu():
  os.system("clear")
  print("User: " + account1["username"])
  print("1. Create a New Note")
  print("2. View Notes")
  print("3. Sign out")
  option = input(">>")
  
  if option == "1":
    new_note = open("notes.txt", "a")
    text = input(">>>>")
    new_note.write(text + "\n\n")
    print("Note Submitted.")
    new_note.close() ##### CLOSE THE NOTES FILE
    time.sleep(1.5)
    menu()
  
  elif option == "2":
    new_note = open("notes.txt", "a")
    print(new_note.read())
    new_note.close()
    input("Press enter to continue...")
    menu()

    
  
  
  elif option == "3":
    pass
  
  else:
    print("Invalid option.")
    time.sleep(1.5)
    menu()
  
  
  
while True:
  os.system("clear")
  print("....LOGIN....")
  username = input("USERNAME: ")
  if username == account1["username"]:
    password = input("PASSWORD: ")
    if password == account1["password"]:
      print("Logged in as " + username)
      menu()
  else:
    print("Invalid username")
  time.sleep(1.5)
    
  
  









