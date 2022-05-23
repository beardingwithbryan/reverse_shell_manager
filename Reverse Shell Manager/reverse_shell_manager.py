import shell
import listener
import settings

# Main

if __name__ == "__main__":
    settings.init()
    shell.RS_Shell().cmdloop()
    #listen(args.lhost, int(args.lport))