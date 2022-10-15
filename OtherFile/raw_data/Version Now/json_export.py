item_json_name = "GadgetSpawns.json"

import json
import os
from pydoc import describe


def shortest_road(points):
    # 要求每个点1以内的距离
    points.sort(key=lambda x: x[2])
    result = []
    for i in range(len(points)):
        if i == 0:
            result.append(points[i])
        else:
            if points[i][0] == result[-1][0] and points[i][1] == result[-1][1]:
                result[-1] = points[i]
            else:
                result.append(points[i])
    return result


def path_fix(path):
    path = path.replace('"', "'")
    return path


def new_folder(path):
    path = path_fix(path)
    if not os.path.exists(path):
        os.makedirs(path)

count_dict = {}
def count(key="N"):
    global count_dict
    if key in count_dict:
        count_dict[key] += 1
    else:
        count_dict[key] = 1


# load id_json 文件夹内全部文件
def item_point_generate(language_id):
    # language_id = 3  # 0:cn,1:tw,2:en,3:ru
    language_name = ["zh-cn", "zh-tw", "en-us", "ru-ru"]
    folader_name = os.path.join(os.path.dirname(__file__), "ID_json")
    id_json = {}
    for file in os.listdir(folader_name):
        print(file)
        with open(os.path.join(folader_name, file), "r", encoding="utf-8") as f:
            # print(json.load(f))
            # file_json = {file:json.load(f)}
            id_json[file] = json.load(f)
    item_json_path = os.path.join(os.path.dirname(__file__), "pos", item_json_name)
    with open(item_json_path, "r") as f:
        item_json = json.load(f)

    result_path = os.path.join(
        os.path.dirname(__file__), "result", language_name[language_id]
    )
    if not os.path.exists(os.path.dirname(result_path)):
        os.makedirs(os.path.dirname(result_path))

    item_dict = {}


    for scene_data in item_json:
        # print(scene_data["sceneId"])
        scene_data["sceneId"] = str(scene_data["sceneId"])
        scene_data["sceneId"] = id_json["Scene.json"][scene_data["sceneId"]][language_id]
        if scene_data["sceneId"] not in item_dict.keys():
            item_dict.update({scene_data["sceneId"]: {}})
        new_folder(os.path.join(result_path, scene_data["sceneId"]))
        for item in scene_data["spawns"]:
            if "gatherItemId" in item:
                item["gatherItemId"] = str(item["gatherItemId"])
                if item["gatherItemId"] in id_json["Item.json"].keys():
                    item["gatherItemId"] = id_json["Item.json"][item["gatherItemId"]][
                        language_id
                    ]
                if item["gatherItemId"] not in item_dict[scene_data["sceneId"]].keys():
                    item_dict[scene_data["sceneId"]].update({item["gatherItemId"]: []})
                new_folder(
                    os.path.join(result_path, scene_data["sceneId"], item["gatherItemId"])
                )
                pos = [item["pos"]["x"], item["pos"]["y"], item["pos"]["z"]]
                item_dict[scene_data["sceneId"]][item["gatherItemId"]].append(pos)
                count(item["gatherItemId"])
        # count(scene_data["sceneId"])
    # print(item_dict)
    count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)  # 按照value排序



    pos_json = {
        "description": "",
        "name": "jingdie1",
        "position": [-518.974853515625, 355.34765625, 615.0311279296875],
    }  # formate
    for scene, items in item_dict.items():
        print(scene)
        for item, points in items.items():
            i = 0
            shortest_points = shortest_road(points)
            for pos in shortest_points:
                i += 1
                pos_name = f"{i}-{item}-{scene}"
                pos_json["description"] = pos_name
                pos_json["name"] = pos_name
                pos_json["position"] = pos
                with open(
                    path_fix(os.path.join(result_path, scene, item, pos_name + ".json")),
                    "w",
                    encoding="utf-8",
                ) as f:
                    lines = json.dumps(
                        pos_json,
                        ensure_ascii=False,
                        indent=4,
                    )
                    f.write(lines)
# print(count_dict)

if __name__ == "__main__":
    for i in range(4):
        item_point_generate(i)