import settings
import listener
import argparse
from cmd import Cmd
from colorama import Fore, Back, Style
import reverse_shell_manager


class RS_Shell(Cmd):

    intro = "Need ASCII Art Here"
    prompt = 'Shell manager > '
    def do_exit(self, inp):
        'Exit the Reverse Shell Manager'
        print("Bye")
        return True

    def do_victims(self, inp):
        'List all current Victims'
        print(Back.MAGENTA + "Listing all current vicitims..." + Style.RESET_ALL)
        
    
    def do_set_lhost(self, arg):
        'Give IP Address to Listen on'
        settings.LHOST = str(arg)

    def do_set_lport(self, arg):
        'Give Port to Listen on'   
        settings.LPORT = int(arg)
    
    def do_listen(self, inp):
        'Start to Listen'
        if settings.LPORT == -1 or settings.LHOST == "":
            print("Listener not assigned IP address or port. Use set_lhost or set_lport to set listener up")
            print("Current values are")
            print("LHOST: ", settings.LHOST)
            print("LPORT: ", settings.LPORT)
        else:
            listener.listen(settings.LHOST, settings.LPORT)




