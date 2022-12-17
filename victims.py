def init():
    global VICTIM_CTR
    VICTIM_CTR = 0


    global VICTIM_LIST
    VICTIM_LIST = [{}]

    '''
    Format for VICTIM List:
    "ID": 2,
    "IP": "10.0.0.2",
    "Connection": conn
    '''