from src import TerminalController

def main():
    mod_loader_atual ="Fabric"
    while True:
        op = int(TerminalController.menu())
        match (op):
            case 1:
                TerminalController.select_version(mod_loader_atual)
            case 2:
                mod_loader_atual = TerminalController.select_mod_loader()
            case 0:
                break;
            case _:
                print("Try again!\n")

if __name__ == '__main__':
    main()