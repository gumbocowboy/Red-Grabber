import json
import config

def get_ff_urls(data, target_title):
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