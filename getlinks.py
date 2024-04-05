import json
import os
import configparser
import config
# The file that the links are written to
listfile = open(config.listfile_location, "w")

# The process of finding the URLs - I'm not really sure exactly how it works lol
# This is used for Firefox ONLY
def find_uri_of_children(data, target_title):
    found_uri = []

    def traverse(data):
        if isinstance(data, dict):
            title = data.get("title")
            if title == target_title:
                children = data.get("children", [])
                for child in children:
                    uri = child.get("uri")
                    if uri:
                        found_uri.append(uri)
            else:
                children = data.get("children", [])
                for child in children:
                    traverse(child)
        elif isinstance(data, list):
            for item in data:
                traverse(item)

    traverse(data)
    return found_uri

def find_uri_chrome(data):
    # Iterate through children and extract proper URLs
    proper_urls = []
    urls = []
    children = data.get("children",[])
    for child in children:
        if child['url'] and not child['url'].startswith('http'):
            # Prepend 'https://www.youtube.com' to relative URLs
            proper_url = 'https://www.youtube.com' + child['url']
            proper_urls.append(proper_url)
        else:
            proper_urls.append(child['url'])
        url = child.get("url")
        if url != None:
            urls.append(str(url))
    return urls
# Opening the given json file
with open(config.bookmark_jsonfile, "r") as file:
    json_data = json.load(file)


# Find the uri of all children of the given bookmark folder.
uris_to_red_children = find_uri_chrome(json_data)

# Print the found URIs and writing them to the list file.
for uri in uris_to_red_children:
    print(uri)
    listfile.write(uri + "\n")
listfile.close()
# Deletes existing bookmark file
os.remove(file.name)

os.system('yt-dlp -P home:'+ config.download_location + ' -a ' +config.listfile_location)
os.system('rm ' + config.listfile_location + "&& touch " + config.listfile_location )