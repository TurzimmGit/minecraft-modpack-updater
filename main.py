from src import TerminalController


def main():
    mod_loader_atual ="Fabric"
    while True:
        op = TerminalController.menu()
        match (op):
            case 1:
                pass
            case 2:
                mod_loader_atual = TerminalController.select_mod_loader()
            case 0:
                break;

if __name__ == '__main__':
    main()