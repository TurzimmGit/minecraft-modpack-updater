import api
import io_local


def check_for_updates(version):
    
    hashes_list = api.getAPIData()
    
    cleaned_hashes_list = clean_hashes_list(hashes_list)
    for i in cleaned_hashes_list:
        if version not in cleaned_hashes_list[i]['game_versions']:
            raise f"Not found any version for the mod :{cleaned_hashes_list[i]['title']}"
        if 'release' not in cleaned_hashes_list[i]['version_type']:
            raise f"Not found a release for the mod :{cleaned_hashes_list[i]['title']}"

    update = input("Do you wanna update it? - yes or no").lower()
    
    if update == 'yes':
        io_local.backup_modpack()
        
        
    if update == 'no':
        return
def clean_hashes_list(hashes_list):
    
    cleaned_hash_list = []
    
    for hash in hashes_list:    
        dict_hash = {'title': hash['title'],
                    'game_versions' : hash['game_versions'],
                     'version_type':hash['version_type'],
                     'loaders': hash['loaders'],
                     'files': hash['files']} 
        cleaned_hash_list.append(dict_hash)
    return cleaned_hash_list