import json

def init():
    global LHOST 
    LHOST = ""

    global LPORT 
    LPORT = -1


    global VICTIM_LIST
    with open('victim_template.json') as json_file:

        VICTIM_LIST = [json.load(json_file)]

    global VICTIM_CTR
    #initialize with 1 as the list is initialized with 1 dictionary
    VICTIM_CTR = 0

    global ALL_CONNECTIONS
    ALL_CONNECTIONS = []

    global ALL_ADDRESSES
    ALL_ADDRESSES = []