#This bot was created by TheTonyKano for the purpose of automation.
import requests
import db_management

#Global Variables
mainMenuOptions = ["Start Bot", "Configure Bot", "Restart Bot","Shutdown Bot", "Exit"]
configBotMenuOptions = ["Configure OAuth", "Set Twitch User ID", "Test Bot Connection", "Go Back"]
configOAuthMenuOptions = ["Set Client ID", "Set Client Secret", "Go Back"]
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
        selection_menu(mainMenuOptions)
        if main_user_input == "1":
            StartBot()
        elif main_user_input == "2":
            configBotMenu()
        elif main_user_input == "3":
            RestartBot()
        elif main_user_input == "4":
            ShutdownBot()
        elif main_user_input == "5":
            exit_application()
            break
        else:
            while True:
                database = db_management.programFile_db
                selection_menu_incorrect(mainMenuOptions)
                if main_user_input == "1":
                    StartBot()
                elif main_user_input == "2":
                    configBotMenu()
                elif main_user_input == "3":
                    RestartBot()
                elif main_user_input == "4":
                    ShutdownBot()
                elif main_user_input == "5":
                    exit_application()
                    break
                else:
                    continue
def StartBot():
    exit_application()

def RestartBot():
    exit_application()

def ShutdownBot():
    exit_application()

def  configBotMenu():
    selection_menu(configBotMenuOptions)
    if main_user_input == "1": #Configure OAuth
        OAuthMenu()
    elif main_user_input == "2": #Set Twitch User ID
        ConfigTwitchUserID()
    elif main_user_input == "3": #Test Bot Connection
        Test_API_Connection()
    elif main_user_input == "4": #Go Back
        mainMenu()
    else:
        while True:
            selection_menu_incorrect(configBotMenuOptions)
            if main_user_input == "1": #Configure OAuth
                OAuthMenu()
            elif main_user_input == "2": #Set Twitch User ID
                ConfigTwitchUserID()
            elif main_user_input == "3": #Test Bot Connection
                Test_API_Connection()
            elif main_user_input == "4": #Go Back
                mainMenu()
            else:
                continue

def ConfigTwitchUserID():
    print("Current User ID: " + str(database))
    UserID = input("Enter Twitch User ID: ")
    db_management.apiAddress_to_db(APIkeyValue, UserID)

def OAuthMenu():
    selection_menu(configBotMenuOptions)
    if main_user_input == "1": #Set the Client ID
        SetClientID()
    elif main_user_input == "2": #Set the Client Secret
        SetClientSecret()
    elif main_user_input == "3": #Post Client ID and Client Secret
        PostOAuth()
    elif main_user_input == "4": #Go Back
        mainMenu()
    else:
        while True:
            selection_menu_incorrect(configBotMenuOptions)
            if main_user_input == "1": #Set the Client ID
                SetClientID()
            elif main_user_input == "2": #Set the Client Secret
                SetClientSecret()
            elif main_user_input == "3": #Post Client ID and Client Secret
                PostOAuth()
            elif main_user_input == "4": #Go Back
                mainMenu()
            else:
                continue

def Test_API_Connection():
    status = Test_API_Address(database[APIkeyValue])
    print(status)
    
def SetClientID():
    global clientIDKey
    clientIDKey = "Client ID"
    #Send the Key/Value pair to the DB for storage.
    clientID = input("What is your Client ID? ")
    db_management.oauth_to_db("Client ID", clientID)

def SetClientSecret():
    global clientSecretKey
    clientSecretKey = "Client Secret"
    #Send the Key/Value pair to the DB for storage.
    clientSecret = input("What is your Client Secret? ")
    db_management.oauth_to_db("Client Secret", clientSecret)

def PostOAuth():
    database = db_management.load_config()
    requests.post("https://id.twitch.tv/oath2/token", '&client_id=' + database[clientIDKey] + "&client_secret=" + database[clientSecretKey])

def Test_API_Address(addressRequest):
    status = requests.get(addressRequest)
    return status.status_code

def exit_application():
    print("End of Script")

mainMenu()
