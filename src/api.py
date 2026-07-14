import requests
from src import io_local

def getAPIData():
    url_bulk = f"https://api.modrinth.com/v2/version_files"
    hashes_list = io_local.calculate_hash()

    paylaod = {
    "hashes":hashes_list,
    "algorithm":"sha1"
    }
    resposnse = requests.post(url=url_bulk,json=paylaod)

    if resposnse.status_code == 200:
        data = resposnse.json()
        return data

def get_download_response(download_url):
    
    response = requests.get(download_url)
    
    if response.status_code == 200:
        return response
    else:
        raise f"No response error:"