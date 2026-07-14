import hashlib
import os 
import shutil

base_path = os.path.expanduser('~')
path = os.path.join(base_path,'AppData/Roaming/.minecraft/mods/')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DESTINY_DIRECTORY = os.path.join(BASE_DIR, '..', 'backupmods')

def getList():
    final_list = []

    full_list = os.listdir(path)

    for nome in full_list:
        full_path = os.path.join(path, nome)
        
        if os.path.isfile(full_path):
            
            final_list.append(nome)
    
    return final_list


def calculate_hash():
    list_ = getList()
    hash_list = []
    for file_name in list_:
        sha1 = hashlib.sha1()
        file_path = os.path.join(path,file_name)
        try:
            with open (file_path, 'rb') as f:
                while block :=f.read(8192):
                    sha1.update(block)
            hash_list.append(sha1.hexdigest())
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_name}: {e}")
    return hash_list


def backup_modpack(name,source_path):
    
    os.makedirs(DESTINY_DIRECTORY, exist_ok=True)
    
    file_path = os.path.join(DESTINY_DIRECTORY, f'{name}')
    
    root_dir = source_path 
  
    shutil.copy2(root_dir,file_path)
        