#This bot was created by TheTonyKano for the purpose of automation.
import requests
import db_management
import sys
from TheTonyKanoBot import TwitchBot
#Global Variables
mainMenuOptions = ["Start Bot", "Configure Bot", "Restart Bot","Shutdown Bot", "Exit"]
configBotMenuOptions = ["Set Broadcaster's Channel","Set Broadcaster ID", 'Set Bot Username',"Configure OAuth", "Set API Address (Do after setting Broadcaster's ID)", "Test Bot Connection", "Go Back"]
configOAuthMenuOptions = ["Set Client ID", "Set Client Secret","Post OAuth", "Go Back"]
APIkeyValue = "API_Address"
broadcaster_id = "broadcaster_id"
# Set up the Twitch API endpoint URL
url = 'https://id.twitch.tv/oauth2/token'
# Set up the Client ID and Client Secret as variables
clientIDKey = "client_id"
clientSecretKey = "client_secret"
botUsernameKey = 'bot_username'
channelKey = 'channel'
tokenKey = 'access_token'
tokenTypeKey = 'token_type'
expiresInKey = 'expires_in'
botUserID = 'bot_user_id'

#Functions
def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")

def selection_menu(menuList):
    #print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input

def selection_menu_incorrect(menuList):
    #print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input

def mainMenu():
    #print("\n" * 100)
    i = True
    while i:
        selection_menu_incorrect(mainMenuOptions)
        if main_user_input == "1":
            print("Bot Started!")
            StartBot()
            mainMenu()
        elif main_user_input == "2":
            configBotMenu()
        elif main_user_input == "3":
            try:
                TwitchBot.stop_bot
            except Exception as e:
                mainMenu()
            print("Bot Stopped!")
            StartBot()
            print("Bot Started!")
            mainMenu()
        elif main_user_input == "4":
            try:
                TwitchBot.stop_bot
            except Exception as e:
                mainMenu()
            print("Bot Stopped!")
            mainMenu()
        elif main_user_input == "5":
            exit_application()
        else:
            while i:
                selection_menu_incorrect(mainMenuOptions)
                if main_user_input == "1":
                    print("Bot Started!")
                    StartBot()
                    mainMenu()
                elif main_user_input == "2":
                    configBotMenu()
                elif main_user_input == "3":
                    try:
                        TwitchBot.stop_bot
                        print("Bot Stopped!")
                    except Exception as e:
                        mainMenu()
                    StartBot()
                    mainMenu()
                elif main_user_input == "4":
                    try:
                        TwitchBot.stop_bot
                        print("Bot Stopped!")
                    except Exception as e:
                        mainMenu()
                    mainMenu()
                elif main_user_input == "5":
                    exit_application()
                else:
                    continue
def loadDB():
    return db_management.load_config()

def StartBot():
    currentDB = loadDB()
    username = currentDB[channelKey]
    client_id = currentDB[clientIDKey]
    try:
        token = currentDB[tokenKey]
    except Exception as e:
        print("Configuration incorrect: Check Client ID and Secret. OAuthToken failed to get.")
        mainMenu()
    channel = currentDB[channelKey]
    bot_user_id = currentDB[botUserID]
    bot = TwitchBot(username, client_id, token, channel, bot_user_id)
    try:
        bot.start()
        print("Bot Started!")
    except Exception as e:
        mainMenu()

def configBotMenu():
    selection_menu(configBotMenuOptions)
    if main_user_input == "1": #Configure Broadcaster's Channel
        question = "Enter your Broadcaster's Channel name: "
        setKeyValueToDB(question, channelKey, 'configBotMenu')
    elif main_user_input == "2": #Configure Broadcaster ID
        question = "Enter your Broadcaster ID: "
        setKeyValueToDB(question, broadcaster_id, 'configBotMenu')
    elif main_user_input == "3": #Configure Bot's Username
        question = "Enter your Bot's Username: "
        setKeyValueToDB(question, botUsernameKey, 'configBotMenu')
    elif main_user_input == "4": #Configure OAuth
        OAuthMenu()
    elif main_user_input == "5": #Sets the API address
        ConfigAPIAddress()
    elif main_user_input == "6": #Test Bot Connection
        Test_API_Connection()
    elif main_user_input == "7": #Go Back
        mainMenu()
    else:
        while True:
            selection_menu_incorrect(configBotMenuOptions)
            if main_user_input == "1": #Configure Broadcaster's Channel
                question = "Enter your Broadcaster's Channel name: "
                setKeyValueToDB(question, channelKey, "configBotMenu")
            elif main_user_input == "2": #Configure Broadcaster ID
                question = "Enter your Broadcaster ID: "
                setKeyValueToDB(question, broadcaster_id, 'configBotMenu')
            elif main_user_input == "3": #Configure Bot's Username
                question = "Enter your Bot's Username: "
                setKeyValueToDB(question, botUsernameKey, 'configBotMenu')
            elif main_user_input == "4": #Configure OAuth
                OAuthMenu()
            elif main_user_input == "5": #Sets the API address
                ConfigAPIAddress()
            elif main_user_input == "6": #Test Bot Connection
                Test_API_Connection()
            elif main_user_input == "7": #Go Back
                mainMenu()
            else:
                continue


def ConfigAPIAddress():
    database = loadDB()
    UserID = database[broadcaster_id]
    db_management.apiAddress_to_db(APIkeyValue, UserID)
    configBotMenu()

def Test_API_Connection():
    database = loadDB()
    status = Test_API_Address(database[APIkeyValue])
    print(status)
    configBotMenu()

def Test_API_Address(addressRequest):
    status = requests.get(addressRequest)
    print(status.status_code)
    configBotMenu()


def OAuthMenu():
    selection_menu(configOAuthMenuOptions)
    if main_user_input == "1": #Set the Client ID
        question = "Enter your Client ID: "
        setKeyValueToDB(question, clientIDKey, 'OAuthMenu')
    elif main_user_input == "2": #Set the Client Secret
        question = "Enter your Client Secret: "
        setKeyValueToDB(question, clientSecretKey, 'OAuthMenu')
    elif main_user_input == "3": #Post Client ID and Client Secret
        PostOAuth()
    elif main_user_input == "4": #Go Back
        configBotMenu()
    else:
        while True:
            selection_menu_incorrect(configOAuthMenuOptions)
            if main_user_input == "1": #Set the Client ID
                question = "Enter your Client ID: "
                setKeyValueToDB(question, clientIDKey, 'OAuthMenu')
            elif main_user_input == "2": #Set the Client Secret
                question = "Enter your Client ID: "
                setKeyValueToDB(question, clientSecretKey, 'OAuthMenu')
            elif main_user_input == "3": #Post Client ID and Client Secret
                PostOAuth()
            elif main_user_input == "4": #Go Back
                configBotMenu()
            else:
                continue

def setKeyValueToDB(question, key, lastMenu):
    value = input(question)
    db_management.simplekeyValue_to_db(key, value)
    if lastMenu == 'mainMenu':
        mainMenu()
    elif lastMenu =='configBotMenu':
        configBotMenu()
    elif lastMenu == 'OAuthMenu':
        OAuthMenu()
    else:
        mainMenu()

def assignToken():
    database = db_management.load_config()
    jsonData = {
    clientIDKey: database[clientIDKey],
    clientSecretKey: database[clientSecretKey],
    'grant_type': 'client_credentials'
    }
    #print(str("https://id.twitch.tv/oath2/token" + '&client_id=' + database[clientIDKey] + "&client_secret=" + database[clientSecretKey] + "&grant_type=client_credentials"))
    response = requests.post(url, data=jsonData)
    access_token = response.json()[tokenKey]
    return access_token

def PostOAuth():
    database = db_management.load_config()
    jsonData = {
    clientIDKey: database[clientIDKey],
    clientSecretKey: database[clientSecretKey],
    'grant_type': 'client_credentials'
    }
    #print(str("https://id.twitch.tv/oath2/token" + '&client_id=' + database[clientIDKey] + "&client_secret=" + database[clientSecretKey] + "&grant_type=client_credentials"))
    response = requests.post(url, data=jsonData)
    access_token = response.json()[tokenKey]
    expires_in = response.json()[expiresInKey]
    token_type = response.json()[tokenTypeKey]
    print("Your access token is: " + access_token)
    db_management.simplekeyValue_to_db(tokenKey, access_token)
    print("Your access token expires in: " + str(expires_in))
    db_management.simplekeyValue_to_db(expiresInKey, expires_in)
    print("Your token type is: " + token_type)
    db_management.simplekeyValue_to_db(tokenTypeKey, token_type)
    OAuthMenu()

def exit_application():
    print("End of Script")
    sys.exit()

mainMenu()

