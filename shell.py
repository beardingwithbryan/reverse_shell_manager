import functions
import victims

def get_command(cmd, extra_args):
    match cmd:
        case "exit":
            functions.exit_program()
        case "help":
            functions.print_main_help_msg()
        case "victims":
            functions.list_victims()
        case "kill":
            functions.kill_victim(extra_args)
        #case "send":
        case " ":
            pass
        case _:
            print("Command "+cmd+" not recognized")