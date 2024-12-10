import json

def hello_json(file="config.json"):
    with open(file, "r", encoding="utf8") as f:
        content = json.load(f)
        
    return content["mode"] + " " + content["nom"]

print(hello_json())