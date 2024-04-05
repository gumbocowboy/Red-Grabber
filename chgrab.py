import json
import config

def find_uri_chrome(data):
    # Iterate through children and extract proper URLs
    proper_urls = []
    urls = []
    children = data.get("children",[])
    for child in children:
        url = child.get("url")
        if url != None:
            urls.append(str(url))
    return urls
