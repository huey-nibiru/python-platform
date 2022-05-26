"""
Project Name: NOTES APP 
Concepts: dictionaries, loops, variables, functions, file io
Homework: make the app capable of deleting notes (delete all notes)
"""



# you can select only the system method from the os library
from os import system

# you can select only the sleep method from the time library
from time import sleep


# CREATE THE ACCOUNT
# dictionaries hold info with key and a value
# username is a key, PY_GUY is the value
# password is a key, slim3Y is the value
account = {"username":"py_guy",
           "password":"slim3y"}


# create a menu function
def menu():
    sleep(1)
    system("clear")
    print("Logged in as " + account["username"])
    print("1. Create new note")
    print("2. View all notes")
    print("3. Sign out")
    option = input(">>>")

    # cycle thru the options
    if option == "1":
       
        # create new note
        with open("notes.txt", "a") as file:
            note = input(">>>>")   
            file.write("* "+note+"\n")  

        # notify user
        print("Note created.")   
        
        # return to menu
        menu()                        
    
    elif option == "2":
        try:
            # clear screen and view notes
            system("clear")
            with open("notes.txt", "r") as file:
                print(note.read())            

            # create buffer before returning to menu
            input("Press enter to continue...")
            menu()
        except:
            # if there are no notes, let the user know
            input("No notes available...Press enter to continue.")
            menu()
        
    elif option == "3":
        # nothing qill happen. Menu will dissapear and return to login
        pass

    else:
        # only use options 1 - 3
        print("* invalid choice *")
        menu()
    
    



    
# CREATE THE LOGIN SCREEN
# THIS WILL LOOP THE PROGRAM FOREVER
while True:
    # pause the screen
    sleep(1)        

    # clear the screen
    system("clear") 

    # LOGIN SCREEN 
    print(".......LOGIN.......")
    username = input("Enter Username:")

    # VERIFY THE USERNAME AND PASSWORD
    if username == account["username"]:
        password = input("Enter Password:")
        if password == account["password"]:
            print("User logged in.")
            menu() # start the menu
        else: 
            print("invalid password")
    else:
        print("invalid username")


