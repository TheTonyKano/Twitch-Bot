#This bot was created by TheTonyKano for the purpose of automation.
import requests
import sys
from TheTonyKanoBot import TwitchBot
import account_configuration
#import subprocess
#Global Variables
mainMenuOptions = ["Start Bot", "Configure Bot", "Restart Bot","Shutdown Bot", "Exit"]
configBotMenuOptions = ["Set Broadcaster's Channel","Set Broadcaster ID","Set Broadcaster Client ID", "Set Broadcaster Client Secret", "Set Bot's Channel","Set Bot ID","Set Bot Client ID", "Set Bot Client Secret","Test OAuth Connection", "Set API Address (Do after setting Broadcaster's ID)", "Test Bot Connection", "Go Back"]
configOAuthMenuOptions = ["Set Client ID", "Set Client Secret","Post OAuth", "Go Back"]
APIkeyValue = "API_Address"
broadcaster_id = "broadcaster_id"
# Set up the Twitch API endpoint URL
url = 'https://id.twitch.tv/oauth2/token'
# Set up the Client ID and Client Secret as variables
channel = 'channel'
channel_ID = 'channel_ID'
channel_client_id = 'channel_client_id'
channel_client_secret = 'channel_client_secret'
bot_channel = 'bot_channel'
bot_channel_ID = 'bot_channel_ID'
bot_channel_client_id = 'bot_channel_client_id'
bot_channel_client_secret = 'bot_channel_client_secret'
access_Token = 'access_token'
token_type = 'token_type'
expires_in = 'expires_in'

#process = subprocess.Popen("StartBot.py")

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
            StartBot()
            #process = subprocess.Popen("StartBot.py")
            print("Bot Started!")
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

def StartBot():
    currentDB = account_configuration.load_config()
    username = currentDB[channel]
    client_id = currentDB[bot_channel_client_id]
    try:
        token = currentDB[access_Token]
    except Exception as e:
        print("Configuration incorrect: Check Client ID and Secret. OAuthToken failed to get.")
        token = ""
        mainMenu()
    Botchannel = currentDB[channel]
    bot_user_id = currentDB[bot_channel_ID]
    bot = TwitchBot(username, client_id, token, Botchannel, bot_user_id)
    try:
        bot.start()
        print("Bot Started!")
    except Exception as e:
        mainMenu()

def configBotMenu():
    lastMenu = "configBotMenu"
    selection_menu(configBotMenuOptions)
    if main_user_input == "1": #Configure Broadcaster's Channel
        question = "Enter your Broadcaster's Channel name: "
        setKeyValueToDB(question, channel, lastMenu)
    elif main_user_input == "2": #Configure Broadcaster ID
        question = "Enter your Broadcaster ID: "
        setKeyValueToDB(question, channel_ID, lastMenu)
    elif main_user_input == "3": #Configure Broadcaster's Client ID 
        question = "Enter your Broadcaster's Client ID: "
        setKeyValueToDB(question, channel_client_id, lastMenu)
    elif main_user_input == "4": #Configure Broadcaster's Client Secret
        question = "Enter your Broadcaster's Client Secret: "
        setKeyValueToDB(question, channel_client_secret, lastMenu)
    elif main_user_input == "5": #Configure Bot's Channel
        question = "Enter your Bot's Channel name: "
        setKeyValueToDB(question, bot_channel, lastMenu)
    elif main_user_input == "6": #Configure Bot's ID
        question = "Enter your Bot's ID: "
        setKeyValueToDB(question, bot_channel_ID, lastMenu)
    elif main_user_input == "7": #Configure Bot's Client ID
        question = "Enter your Bot's Client ID: "
        setKeyValueToDB(question, bot_channel_client_id, lastMenu)
    elif main_user_input == "8": #Configure Bot's Client Secret
        question = "Enter your Bots's Client Secret: "
        setKeyValueToDB(question, bot_channel_client_secret, lastMenu)
    elif main_user_input == "9": #Configure OAuth
        PostOAuth()
    elif main_user_input == "10": #Sets the API address
        ConfigAPIAddress()
    elif main_user_input == "11": #Test Bot Connection
        Test_API_Connection()
    elif main_user_input == "12": #Go Back
        mainMenu()
    else:
        while True:
            selection_menu_incorrect(configBotMenuOptions)
            if main_user_input == "1": #Configure Broadcaster's Channel
                question = "Enter your Broadcaster's Channel name: "
                setKeyValueToDB(question, channel, lastMenu)
            elif main_user_input == "2": #Configure Broadcaster ID
                question = "Enter your Broadcaster ID: "
                setKeyValueToDB(question, channel_ID, lastMenu)
            elif main_user_input == "3": #Configure Broadcaster's Client ID 
                question = "Enter your Broadcaster's Client ID: "
                setKeyValueToDB(question, channel_client_id, lastMenu)
            elif main_user_input == "4": #Configure Broadcaster's Client Secret
                question = "Enter your Broadcaster's Client Secret: "
                setKeyValueToDB(question, channel_client_secret, lastMenu)
            elif main_user_input == "5": #Configure Bot's Channel
                question = "Enter your Bot's Channel name: "
                setKeyValueToDB(question, bot_channel, lastMenu)
            elif main_user_input == "6": #Configure Bot's ID
                question = "Enter your Bot's ID: "
                setKeyValueToDB(question, bot_channel_ID, lastMenu)
            elif main_user_input == "7": #Configure Bot's Client ID
                question = "Enter your Bot's Client ID: "
                setKeyValueToDB(question, bot_channel_client_id, lastMenu)
            elif main_user_input == "8": #Configure Bot's Client Secret
                question = "Enter your Bots's Client Secret: "
                setKeyValueToDB(question, bot_channel_client_secret, lastMenu)
            elif main_user_input == "9": #Configure OAuth
                PostOAuth()
            elif main_user_input == "10": #Sets the API address
                ConfigAPIAddress()
            elif main_user_input == "11": #Test Bot Connection
                Test_API_Connection()
            elif main_user_input == "12": #Go Back
                mainMenu()
            else:
                continue


def ConfigAPIAddress():
    database = account_configuration.load_config()
    UserID = database[channel_ID]
    account_configuration.apiAddress_to_db(APIkeyValue, UserID)
    configBotMenu()

def Test_API_Connection():
    database = account_configuration.load_config()
    status = Test_API_Address(database[APIkeyValue])
    print(status)
    configBotMenu()

def Test_API_Address(addressRequest):
    status = requests.get(addressRequest)
    print(status.status_code)
    configBotMenu()

def setKeyValueToDB(question, key, lastMenu):
    value = input(question)
    account_configuration.simplekeyValue_to_db(key, value)
    if lastMenu == 'mainMenu':
        mainMenu()
    elif lastMenu == "configBotMenu":
        configBotMenu()
    else:
        mainMenu()

def assignToken():
    database = account_configuration.load_config()
    jsonData = {
    bot_channel_client_id: database[bot_channel_client_id],
    bot_channel_client_secret: database[bot_channel_client_secret],
    'grant_type': 'client_credentials'
    }
    #print(str("https://id.twitch.tv/oath2/token" + '&client_id=' + database[bot_channel_client_id] + "&client_secret=" + database[bot_channel_client_id] + "&grant_type=client_credentials"))
    response = requests.post(url, data=jsonData)
    access_token = response.json()[access_Token]
    return access_token

def PostOAuth():
    database = account_configuration.load_config()
    client_id = database[bot_channel_client_id]
    client_secret = database[bot_channel_client_secret]
    jsonData = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
    }
    #urlOAuth = str("https://id.twitch.tv/oath2/token" + '&client_id=' + database[bot_channel_client_id] + "&client_secret=" + database[bot_channel_client_secret] + "&grant_type=client_credentials")
    response = requests.post(url, data=jsonData)
    print(response.json())
    token = response.json()[access_Token]
    expires = response.json()[expires_in]
    type = response.json()[token_type]
    print("Your access token is: " + token)
    account_configuration.simplekeyValue_to_db(access_Token, token)
    print("Your access token expires in: " + str(expires_in))
    account_configuration.simplekeyValue_to_db(expires_in, expires)
    print("Your token type is: " + token_type)
    account_configuration.simplekeyValue_to_db(token_type, type)
    configBotMenu()

def exit_application():
    print("End of Script")
    sys.exit()

mainMenu()

