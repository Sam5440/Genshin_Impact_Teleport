item_json_name = "GadgetSpawns.json"

import json
import os

#load id_json 文件夹内全部文件
language_id = 0  # 0:cn,1:tw,2:en,3:ru
folader_name = "ID_json"
id_json = {}
for file in os.listdir(folader_name):
    print(file)
    with open(os.path.join(folader_name, file), 'r',encoding="utf-8") as f:
        # print(json.load(f))
        # file_json = {file:json.load(f)}
        id_json[file] = json.load(f)


item_json_path = os.path.join(os.path.dirname(__file__), "pos", item_json_name)
with open(item_json_path, "r") as f:
    item_json = json.load(f)
count_dict = {}

def count(key="N"):
    global count_dict
    if key in count_dict:
        count_dict[key] += 1
    else:
        count_dict[key] = 1
        
result_path = os.path.join(os.path.dirname(__file__), "result", str(language_id))
if not os.path.exists(os.path.dirname(result_path)):
    os.makedirs(os.path.dirname(result_path))
    
item_dict = {}
for scene_data in item_json:
    # print(scene_data["sceneId"])
    scene_data["sceneId"] = id_json["Scene.json"][str(scene_data["sceneId"])][language_id]
    if not os.path.exists(os.path.join(result_path, scene_data["sceneId"])):
        os.makedirs(os.path.join(result_path, scene_data["sceneId"]))
    for item in scene_data["spawns"]:
        # 如果存在key   gatherItemId
        if "gatherItemId" in item:
            if str(item["gatherItemId"]) in id_json["Item.json"].keys():
                item["gatherItemId"] = id_json["Item.json"][str(item["gatherItemId"])][language_id]
            count(item["gatherItemId"])
    # count(scene_data["sceneId"])
count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)  # 按照value排序
print(count_dict)
