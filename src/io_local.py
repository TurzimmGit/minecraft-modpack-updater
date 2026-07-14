import hashlib
import os 
import shutil
import zipfile
import json

base_path = os.path.expanduser('~')
mods_path = os.path.join(base_path,'AppData/Roaming/.minecraft/mods/')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DESTINY_DIRECTORY = os.path.join(BASE_DIR, '..', 'backupmods')
MODS_JSON_PATH = os.path.join(BASE_DIR, 'mods.json')

def getList():
    final_list = []

    full_list = os.listdir(mods_path)

    for nome in full_list:
        full_path = os.path.join(mods_path, nome)
        
        if os.path.isfile(full_path):
            
            final_list.append(nome)
    
    return final_list


def calculate_hash():
    list_ = getList()
    hash_list = []
    for file_name in list_:
        sha1 = hashlib.sha1()
        file_path = os.path.join(mods_path,file_name)
        try:
            with open (file_path, 'rb') as f:
                while block :=f.read(8192):
                    sha1.update(block)
            hash_list.append(sha1.hexdigest())
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_name}: {e}")
    return hash_list


def backup_modpack():
    
    os.makedirs(DESTINY_DIRECTORY, exist_ok=True)
    
    for file_name in getList():
        origin = os.path.join(mods_path, file_name)
        destiny = os.path.join(DESTINY_DIRECTORY, file_name)
        shutil.copy2(origin, destiny)
   
def clean_mods_folder():
    for file_name in getList():
        os.remove(os.path.join(mods_path, file_name))
        
def get_mod_id_from_jar(file_name):
    
    full_jar_path = os.path.join(mods_path, file_name)    
    no_data = {}
    
    with open('src/mods.json', 'w', encoding='utf-8') as file:
        json.dump(no_data, file)
    try:
        with zipfile.ZipFile(full_jar_path, 'r') as jar:
            if 'fabric.mod.json' in jar.namelist():
                with jar.open('fabric.mod.json') as f:
                    mod_data = json.loads(f.read().decode('utf-8'))
                    return mod_data.get('id')
    except Exception as e:
        print(f"ERROR reading the metadata from jar {file_name}: {e}")
    return None

def sync_mods_database(current_physical_files):

    database = {}
    if os.path.exists(MODS_JSON_PATH):
        try:
            with open(MODS_JSON_PATH, 'r', encoding='utf-8') as f:
                database = json.load(f)
        except Exception:
            database = {}

    synchronized_db = {file: p_id for file, p_id in database.items() if file in current_physical_files}

    save_mods_database(synchronized_db)
    return synchronized_db

def save_mods_database(data):
    with open(MODS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)