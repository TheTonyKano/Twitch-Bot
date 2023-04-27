import json
import pathlib
defaultJsonFormat = {'channel' : "", 'channel_ID' : "", 'channel_client_id' : "", 'channel_client_secret' : "", 'bot_channel' : "", 'bot_channel_ID' : "", 'bot_channel_client_id' : "", 'bot_channel_client_secret' : "", 'access_Token' : "", 'token_type' : "", 'expires_in' : ""}
broadcaster = "?broadcaster_id="
twitchAPI_BeginningAddressTemplate = "https://api.twitch.tv/helix/"
channels = "channels"
schedule = "schedule"

def apiAddress_to_db(keyValue, API_ID): 
    programFile_db[keyValue] = twitchAPI_BeginningAddressTemplate + channels + broadcaster + API_ID
    output_db_to_file(programFile_db)

def simplekeyValue_to_db(keyValue, value): 
    programFile_db[keyValue] = value
    output_db_to_file(programFile_db)

def output_db_to_file(un_dict): # Write Dictionary Memory to file
    with open('config.json', 'w') as temp_dict:
        json.dump(un_dict, temp_dict)
        programFile_db = un_dict
        return programFile_db

def check_db_file(): # Retrieve Dictionary from JSON to Memory
    file_path = pathlib.Path("config.json")
    while True:
        if file_path.exists():
            break
        else:
            with open('config.json', 'w') as create_file:
                json.dump(defaultJsonFormat, create_file)
        load_config()
        break


def load_config():
    check_db_file()
    with open('config.json', 'r') as temp_dict:
        programFile_db = json.load(temp_dict)
        return programFile_db 
    
programFile_db = load_config()

class AccountConfig:
    def __init__(self, channel, channel_ID, channel_client_id, channel_client_secret, bot_channel, bot_channel_ID, bot_channel_client_id, bot_channel_client_secret, access_Token, token_type, expires_in):
        self.channel = channel
        self.channel_ID = channel_ID
        self.channel_client_id = channel_client_id
        self.channel_client_secret = channel_client_secret
        self.bot_channel = bot_channel
        self.bot_channel_ID = bot_channel_ID
        self.bot_channel_client_id = bot_channel_client_id
        self.bot_channel_client_secret = bot_channel_client_secret
        self.access_Token = access_Token
        self.token_type = token_type
        self.expires_in = expires_in


    
