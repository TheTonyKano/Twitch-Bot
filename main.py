#This bot was created by TheTonyKano for the purpose of automation.
import requests
import db_management

#Global Variables
mainMenuOption = ["Set API address", "Test API address", "Set OAuth2","Exit"]
APIkeyValue = "API_Address"


#Functions
def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")


def selection_menu(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input


def selection_menu_incorrect(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input

def mainMenu():
    print("\n" * 100)
    i = True
    while i:
        global database
        database = db_management.programFile_db
        selection_menu(mainMenuOption)
        if main_user_input == "1":
           print("Current address is: " + str(database))
           apiAddress = input("Enter Twitch Username: ")
           db_management.apiAddress_to_db(APIkeyValue, apiAddress)
           mainMenu()
        elif main_user_input == "2":
            Test_API_Menu()
        elif main_user_input == "3":
            Get_Secret()
        elif main_user_input == "4":
            exit_application()
            break
        else:
            while True:
                database = db_management.programFile_db
                selection_menu_incorrect(mainMenuOption)
                if main_user_input == "1":
                    print("Current address is: " + str(database))
                    apiAddress = input("Enter Twitch Username: ")
                    db_management.apiAddress_to_db(APIkeyValue, apiAddress)
                    mainMenu()
                elif main_user_input == "2":
                    Test_API_Menu()
                elif main_user_input == "3":
                    exit_application()
                    break
                else:
                    continue


def Test_API_Menu():
    
    status = Test_API_Address(database[APIkeyValue])
    print(status)
    i = False
    exit_application()

def Get_Secret():
    clientIDKey = "Client ID"
    clientSecretKey = "Client Secret"
    clientID = input("What is your Client ID? ")
    #Send the Key/Value pair to the DB for storage.
    db_management.oauth_to_db("Client ID", clientID)
    #Send the Key/Value pair to the DB for storage.
    clientSecret = input("What is your Client Secret? ")
    db_management.oauth_to_db("Client Secret", clientSecret)
    database = db_management.load_config()
    requests.post("https://id.twitch.tv/oath2/token", '&client_id=' + database[clientIDKey] + "&client_secret=" + database[clientSecretKey])

def Test_API_Address(addressRequest):
    status = requests.get(addressRequest)
    return status.status_code

def exit_application():
    print("End of Script")

mainMenu()
