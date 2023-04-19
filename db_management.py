import json
import pathlib

twitchAPI_BeginningAddressTemplate = "https://api.twitch.tv/helix/"
channels = "channels"
schedule = "schedule"
broadcaster = "?broadcaster_id="


# Functions
def apiAddress_to_db(keyValue, API_ID): 
        print(twitchAPI_BeginningAddressTemplate + channels + broadcaster + API_ID)
        programFile_db[keyValue] = twitchAPI_BeginningAddressTemplate + channels + broadcaster + API_ID
        output_db_to_file(programFile_db)

def oauth_to_db(keyValue, value): 
        print("Your " + keyValue + " is: " + value + ".")
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
            blank_dict = {} #Makes new DB if one does not exist
            with open('config.json', 'w') as create_file:
                json.dump(blank_dict, create_file)
        load_config()
        break


def load_config():
    check_db_file()
    with open('config.json', 'r') as temp_dict:
        programFile_db = json.load(temp_dict)
        return programFile_db
    
    
# Variables

programFile_db = load_config()