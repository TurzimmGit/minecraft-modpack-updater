from src import api
from src import io_local
import os

def check_for_updates(version,mod_loader):
    
    hashes_list = api.getAPIData()
    
    if not hashes_list:
        print("No data received from Modrinth API (or mods folder is empty).")
        return
    
    compatible_mods= []
    incompatible_mods = []
    
    cleaned_hashes_list = clean_hashes_list(hashes_list)
    for mod in cleaned_hashes_list:
        print(mod['game_versions'])
        if version in mod['game_versions'] and mod_loader.lower() in [l.lower() for l in mod['loaders']]:
            compatible_mods.append(mod['title'])
        else:
            incompatible_mods.append(mod['title'])
            
    print(f"Compatible: {len(compatible_mods)} | Incompatible: {len(incompatible_mods)}\n")
    print("Incompatible Mods:\n")
    for mod in incompatible_mods:
        print(f" - {mod}")
    print()

    update = input("Do you wanna update it? - yes or no").lower()
    
    if update == 'yes':
        io_local.backup_modpack()
        io_local.clean_mods_folder()
        download_modpack(cleaned_hashes_list)
        
        
    if update == 'no':
        return
def clean_hashes_list(hashes_list):
    
    cleaned_hash_list = []
    
    for _, file_info in hashes_list.items():  
        
        title = file_info.get('name','Unknown Mod File')
        game_versions = file_info.get('game_versions',[])
        version_type = file_info.get('version_type', 'release')        
        loaders = file_info.get('loaders', [])
        files = file_info.get('files',[])
        
          
        dict_hash = {'title': title,
                    'game_versions' : game_versions,
                     'version_type':version_type,
                     'loaders': loaders,
                     'files': files} 
        cleaned_hash_list.append(dict_hash)
    return cleaned_hash_list


def download_modpack(cleaned_hashes_list):
    
    for mod in cleaned_hashes_list:
        download_url = mod['files'][0]['url']
        file_name = mod['files'][0]['filename']
        response = api.get_download_response(download_url)
        
        final_path = os.path.join(io_local.path,file_name)
        
        with open(final_path, 'wb') as f:
            f.write(response.content)
            
    
        
            