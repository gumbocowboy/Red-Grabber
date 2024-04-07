import json
import config
from bs4 import BeautifulSoup
# Converts Chrome's HTML bookmark output to JSON
def parse_folder(folder_tag):
    folder = {"name": folder_tag.text, "children": []}
    for child in folder_tag.find_all(recursive=True):
        #if child.name == 'A':
        folder['children'].append({
        "title": child.text,
        "url": child.get('href'),
        #"add_date": int(child.get('add_date')),
        "icon": child.get('icon')
        })
    return folder

def html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h3_tags = soup.find_all("h3")
    for h3_tag in h3_tags:
        if h3_tag.text.strip() == config.bookmark_folder_name:
            dl_tag = h3_tag.find_next_sibling("dl")
            if dl_tag:
                return parse_folder(dl_tag)

    return None

def main():
    print("Foo")
    with open(config.chrome_html_filename, "r", encoding="utf-8") as file:
        html_content = file.read()

    json_data = html_to_json(html_content)
    print(json_data)
    if json_data:
        with open(config.bookmark_jsonfile, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        print("JSON data exported to bleh")
    else:
        print("No 'To DL' folder found in the HTML.")

if __name__ == "__main__":
    main()