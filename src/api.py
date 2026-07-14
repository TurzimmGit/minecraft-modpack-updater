import requests
from src import io_local
import urllib
HEADERS = {
    "User-Agent": "turzimm/minecraft-modpack-updater/1.0.0 (turzimm.contact@email.com)"
}

def get_updates_for_version(version,loader):
    
    url_update = "https://api.modrinth.com/v2/version_files/update"
    hashes_list = io_local.calculate_hash()

    payload = {
        "hashes": hashes_list,
        "algorithm": "sha1",
        "loaders": [loader.lower()],
        "game_versions": [version]
    }

    response = requests.post(url=url_update, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    return {}
    
def download_file_bytes(download_url):
    response = requests.get(download_url)
    
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download file from {download_url}")
    
def get_project_id_by_slug(slug):
    slug_clean = slug.lower()
    
  
    if slug_clean == 'noisium':
        return 'hasdd01q' 
        
    variations = [
        slug_clean,
        slug_clean.replace('_', '-'),
        slug_clean.replace('_', ''),
        slug_clean.replace('-fabric', ''),
        slug_clean.replace('_fabric', '')
    ]
    
    if slug_clean.endswith('3d'):
        prefix_version = '3d' + slug_clean[:-2]
        variations.append(prefix_version)
        variations.append(prefix_version.replace('_', '-'))
        
    variations = list(dict.fromkeys(variations))

    for var in variations:
        url_direct = f"https://api.modrinth.com/v2/project/{var}"
        try:
            response = requests.get(url_direct, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                project_slug = data.get('slug', '').lower()
                
                target_check = var.replace('_', '').replace('-', '')
                clean_project_slug = project_slug.replace('_', '').replace('-', '')
                
                if target_check == clean_project_slug or target_check in clean_project_slug:
                    return data.get('id')
        except Exception:
            pass

    url_search = f"https://api.modrinth.com/v2/search?query={slug_clean}&facets=[[\"project_type:mod\"]]"
    try:
        response = requests.get(url_search, headers=HEADERS)
        if response.status_code == 200:
            hits = response.json().get('hits', [])
            for hit in hits:
                hit_slug = hit.get('slug', '').lower()
                hit_title = hit.get('title', '').lower()
                
                target_check = slug_clean.replace('_', '').replace('-', '')
                clean_hit_slug = hit_slug.replace('_', '').replace('-', '')
                
                if target_check in clean_hit_slug or target_check in hit_title.replace(' ', ''):
                    return hit.get('project_id')
            
            if hits:
                return hits[0].get('project_id')
    except Exception:
        pass
        
    return None