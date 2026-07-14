from src import core

def menu():
    print("\n================")
    print("\n0 - Exit...\n")
    print("1 - Select Version to Update\n")
    print("2 - Select ModLoader(Default: Fabric)\n")
    print("================\n")
    
    return input()

def mod_loader_menu():
    
    print("\n================")
    print("1 - Fabric\n")
    print("2 - Forge\n")
    print("3 - NeoForge\n")
    print("4 - Quilt")
    print("================\n")
    
def select_version(mod_loader):
    
    version = input("Type what version ypu want to update to: \n")

    core.check_for_updates(version,mod_loader)
    
def select_mod_loader():
    mod_loader_dict = {
        1:"Fabric",
        2:"Forge",
        3:"NeoForge",
        4:"Quilt"
    }
    
    mod_loader_menu()
    new_mod_loader = int(input("What's your modloader?"))
    
    return mod_loader_dict[new_mod_loader]