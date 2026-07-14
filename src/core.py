from src import api
from src import io_local
import os
import requests
import platform

def check_for_updates(version, mod_loader):
    all_files = io_local.getList()
    physical_mods = [f for f in all_files if f.lower().endswith('.jar')]
    
    if not physical_mods:
        print("\nNo data received the mods folder is empty).\n")
        return

    mods_db = io_local.sync_mods_database(physical_mods)
    
    local_mods_mapped = []
    database_updated = False
    
    loader_str = (mod_loader or "fabric").lower()
    
    print("Verifiyng local IDs...")
    for file_name in physical_mods:
        project_id = mods_db.get(file_name)
        
        if not project_id:
            print(f" -> New Mod detected: {file_name}. Searching for Metadata...\n")
            fabric_id = io_local.get_mod_id_from_jar(file_name)
        
            if fabric_id:
                project_id = api.get_project_id_by_slug(fabric_id)
                if project_id:
                    mods_db[file_name] = project_id
                    database_updated = True
                    print(f"    [Success] mapped: {fabric_id} -> ID: {project_id}")
                else:
                    print(f"    [Warning] Modrinth didn't reconize the fabric ID: '{fabric_id}'")
            else:
                if file_name!= "desktop.ini":
                    print(f"    [Warning] It was not possible to read the fabric.mod.json at {file_name}")
        if not project_id:
            print(f"\n[!] Não conseguimos mapear automaticamente o mod: {file_name}")
            user_input = input(f"Por favor, digite o ID do Modrinth ou a URL do mod '{fabric_id}' (ou aperte Enter para pular): ").strip()
            
            if user_input:
                if "modrinth.com/mod/" in user_input:
                    project_id = user_input.split("/mod/")[-1].split("/")[0]
                else:
                    project_id = user_input
                    project_id = api.get_project_id_by_slug(project_id)

        if project_id:
            local_mods_mapped.append({
                'title': file_name.replace('.jar', ''),
                'project_id': project_id
            })

    if database_updated:
        io_local.save_mods_database(mods_db)

    if not local_mods_mapped:
        print("No valid mod to update!")
        return
    
    print("\nChecking for updates in Modrinth...\n")
    
    compatible_mods = []
    incompatible_mods = []
    mods_to_download = []

    for mod in local_mods_mapped:
        p_id = mod['project_id']
        title = mod['title']
        
        url_version = f"https://api.modrinth.com/v2/project/{p_id}/version"
        try:
            response = requests.get(url_version, headers=api.HEADERS)
            if response.status_code == 200:
                versions = response.json()
                found_update = False
                
                for ver in versions:
                    has_version = version in ver.get('game_versions', [])
                    has_loader = loader_str in [l.lower() for l in ver.get('loaders', [])]
                                
                    if has_version and has_loader:
                        compatible_mods.append(title)
                        mods_to_download.append({
                            'title': title,
                            'filename': ver['files'][0]['filename'],
                            'url': ver['files'][0]['url']
                        })
                        found_update = True
                        print(f"    -> [COMPATBILE MOD FOUND!]: {ver['files'][0]['filename']}")
                        break
                
                if not found_update:
                    incompatible_mods.append(title)
            else:
                print(f"[Warning] Incorrect ID detected to {title}. Reseting local identifier...")
                if title + ".jar" in mods_db:
                    del mods_db[title + ".jar"]
                    database_updated = True
                incompatible_mods.append(title)
                
        except Exception as e:
            print(f"[Script Error] Failure to Process {title}: {e}\n")
            incompatible_mods.append(title)

    if database_updated:
        io_local.save_mods_database(mods_db)

    print(f"\n Compatible_mods {len(compatible_mods)} | incompatible: {len(incompatible_mods)}\n")
    if incompatible_mods:
        print("Mods without update avaiable:")
        for mod in incompatible_mods:
            print(f" - {mod}")
        print()

    if not mods_to_download:
        print("No updates found for the version!")
        return
    
    update = input("Would you like to update? (yes/no)\n").lower()
    if update == 'yes':
        io_local.backup_modpack()
        io_local.clean_mods_folder()
        download_modpack(mods_to_download)
        print("\n[Success] Modpack updated Successfully!")
    else:
        print("Cancelled Update!")

def get_minecraft_mods_path():
    sistema = platform.system()
    home = os.path.expanduser("~")
    
    if sistema == "Windows":
        appdata = os.getenv("APPDATA")
        if appdata:
            return os.path.join(appdata, ".minecraft", "mods")
        return os.path.join(home, "AppData", "Roaming", ".minecraft", "mods")
        
    elif sistema == "Darwin":  
        return os.path.join(home, "Library", "Application Support", "minecraft", "mods")
        
    else:
        return os.path.join(home, ".minecraft", "mods")

def download_modpack(mod_to_download):
    print("\n Starting Downloads...")
    
    mods_folder = get_minecraft_mods_path()
    
    print(f"Target directory: {mods_folder}")

    if not os.path.exists(mods_folder):
        os.makedirs(mods_folder)
   
    for mod in mod_to_download:
        try:
            print(f"Downloading {mod['title']}...")
            file_bytes = api.download_file_bytes(mod['url'])
            
            final_path = os.path.join(mods_folder, mod['filename'])
            
            with open(final_path, 'wb') as f:
                f.write(file_bytes)
            print(f" -> [Success]: {mod['filename']} downloaded directly to .minecraft/mods!")
            
        except Exception as e:
            print(f"Failed to download {mod['title']}: {e}\n")