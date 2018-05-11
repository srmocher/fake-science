import bs4
from SolrClient import SolrClient
import os
import json
import requests


CC_LINKS_FILES_DIRECTORIES = []
SOLR_INSTANCE_URL = ""
SOLR_CORE = ""

solr_client = SolrClient(SOLR_INSTANCE_URL)

def get_url_content(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    resp = requests.get(url,headers=headers)
    return resp.text

for directory in CC_LINKS_FILES_DIRECTORIES:
    files = [f for f in os.listdir(directory) if os.path.isfile(f)]
    for file in files:
        docs = []
        with open(directory+'/'+file,'r') as f:
            for line in f:
                json_obj = json.loads(line,encoding="utf-8")
                url = json_obj["url"]
                text = get_url_content(url)
                docs.append({"file_name" : file,"html" : text})
            solr_client.index(SOLR_CORE,docs)
            solr_client.commit(SOLR_CORE,openSearcher=True)
