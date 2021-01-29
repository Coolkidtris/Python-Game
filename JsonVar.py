import json



with open('json/Dungeon1.json', 'r') as myfile:
    Json = myfile.read()

LoadedVar1 = json.loads(Json)

with open('json/Dungeon1.json', 'r') as myfile:
    Json = myfile.read()

LoadedVar2 = json.loads(Json)

dungeon_descriptions = [LoadedVar1["desc"], [LoadedVar2["desc"]]]


