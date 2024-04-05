import json
import os
import configparser
import config
import ffgrab
import chgrab
import jsonconverter

browser = None
uris_to_red_children = []

def append_urls(uris):

# Print the found URIs and writing them to the list file.
    for uri in uris:
        print(uri)
        listfile.write(uri + "\n")
        listfile.close()
# Opening the given json file
def open_json():
    with open(config.bookmark_jsonfile, "r") as file:
        json_data = json.load(file)
        return(json_data)
def get_json():
    with open(config.bookmark_jsonfile, "r") as file:
        return(file)

def foo():
    browser = input("Chrome(c) or Firefox(f)?")
    if browser == "c" or browser == "C":
        print("Checking for HTML Chrome bookmarks..")
        jsonconverter.main()
        open_json()
        uris_to_red_children = chgrab.find_uri_chrome(open_json())
        append_urls(uris_to_red_children)
    elif browser == "f" or browser == "F":
        print("Firefox")
        open_json()
        uris_to_red_children = ffgrab.get_ff_urls(open_json(), config.bookmark_folder_name)
        append_urls(uris_to_red_children)

    else:
        print("WRONG")
        foo()
listfile = open(config.listfile_location, "w")

foo()

# The file that the links are written to






# Find the uri of all children of the given bookmark folder.


# Deletes existing bookmark file
os.remove(get_json().name)

os.system('yt-dlp -P home:'+ config.download_location + ' -a ' +config.listfile_location)
os.system('rm ' + config.listfile_location + "&& touch " + config.listfile_location )