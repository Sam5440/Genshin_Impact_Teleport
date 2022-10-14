item_json_name = "GadgetSpawns.json"

import json
import os

# Path: json_export.py
item_json_path = os.path.join(os.path.dirname(__file__), "pos", item_json_name)
with open(item_json_path, "r") as f:
    item_json = json.load(f)

j = item_json[0]["spawns"]
for i in j:
    # 判断key是否存在
    if "gatherItemId" in i:
        print(i["gatherItemId"])
        print(i["pos"]['x'], i["pos"]['y'], i["pos"]['z'])
