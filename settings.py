def init():
    global LHOST 
    LHOST = ""

    global LPORT 
    LPORT = -1

    global VICTIM_LIST
    VICTIM_LIST = [{}]

    global VICTIM_CTR
    #initialize with 1 as the list is initialized with 1 dictionary
    VICTIM_CTR = 1