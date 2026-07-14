import requests
import io_local

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
