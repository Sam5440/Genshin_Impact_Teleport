import json
import os
import re
from codecs import latin_1_decode
from unittest import result

import matplotlib.pyplot as plt

###########
language_name = ["zh-cn", "zh-tw", "en-us", "ru-ru"]
item_json_name = "GadgetSpawns.json"
monster_json_name = "Spawns.json"
###########
############################################
def road_long(point1, point2):
    return (
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    ) ** 0.5


def nearest_road(points):
    if len(points) <= 1:
        return points
    result = [points[0]]
    while points != []:
        min = 2147483647
        point = result[-1]
        for index, next_point in enumerate(points):
            length = road_long(next_point, point)
            if length < min:
                min = length
                index_nearest = index  # points.index(point)
        result.append(points[index_nearest])
        points.pop(index_nearest)
    # print(result)
    print(len(result),count_road_long(result))
    result = remove_same_area_point(result)
    print(len(result),count_road_long(result))
    print(len(result))
    return result

# def point_center(point1,point2,point3):
#     #求到这三个点的距离相等的点A


def remove_same_area_point(points, loot_range=13):
    if len(points) <= 1:
        return points
    result = [points[0]]
    points.pop(0)
    last_is_optimize = False
    while points != []:
        length = road_long(points[0], result[-1])
        if  length > loot_range*2 or last_is_optimize:
            if length > loot_range:
                result.append(points[0])
                last_is_optimize = False
        else:
            # 取中点
            result[-1] = [
                (result[-1][0] + points[0][0]) / 2,
                (result[-1][1] + points[0][1]) / 2,
                (result[-1][2] + points[0][2]) / 2,
            ]
            last_is_optimize = True
        points.pop(0)
    return result
            # result[-1] =


def count_road_long(points):
    # 计算路径长度
    long = 0
    for i in range(len(points) - 1):
        long += (
            (points[i][0] - points[i + 1][0]) ** 2
            + (points[i][1] - points[i + 1][1]) ** 2
            + (points[i][2] - points[i + 1][2]) ** 2
        ) ** 0.5
    return long


def draw_3d(points, show=False):
    print(count_road_long(points))
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    z = [i[2] for i in points]
    if show:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(x, y, z)
        ax.set_xlabel("X Label")
        ax.set_ylabel("Y Label")
        ax.set_zlabel("Z Label")
        plt.show()


##############################################################
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
def get_all_id_name(folader_name):
    id_json = {}
    for file in os.listdir(folader_name):
        print(file)
        with open(os.path.join(folader_name, file), "r", encoding="utf-8") as f:
            # print(json.load(f))
            # file_json = {file:json.load(f)}
            id_json[file] = json.load(f)
    return id_json


def save_json(result_path, item_dict):
    pos_json = {}  # formate
    for scene, items in item_dict.items():
        # print(scene)
        for item, points in items.items():
            i = 0
            # if len(points) > 100:
            #     print(f"{len(points)}{item}-{scene}")
            #     draw_3d(points)
            #     best_road = nearest_road(points)
            #     draw_3d(best_road)
            best_road = nearest_road(points)

            for pos in best_road:
                i += 1
                pos_name = f"{i}-{item}-{scene}"
                pos_json["description"] = str(i)  # 拼音
                pos_json["name"] = str(i)  # 拼音
                pos_json["position"] = pos
                with open(
                    path_fix(
                        os.path.join(result_path, scene, item, pos_name + ".json")
                    ),
                    "w",
                    encoding="utf-8",
                ) as f:
                    lines = json.dumps(
                        pos_json,
                        # ensure_ascii=False,
                        # indent=4,
                    )
                    # f.write(lines)
                    json.dump(pos_json, f)


def json_pos_generate_dict(
    language_id,
    id_json,
    item_json,
    result_path,
    pos_type_name="gatherItemId",
    id_name_json_filename="Item.json",
):
    global count_dict
    item_dict = {}
    for scene_data in item_json:
        # print(scene_data["sceneId"])
        scene_data["sceneId"] = str(scene_data["sceneId"])
        scene_data["sceneId"] = id_json["Scene.json"][scene_data["sceneId"]][
            language_id
        ]
        if scene_data["sceneId"] not in item_dict.keys():
            item_dict.update({scene_data["sceneId"]: {}})
        new_folder(os.path.join(result_path, scene_data["sceneId"]))
        for item in scene_data["spawns"]:
            if pos_type_name in item:
                item[pos_type_name] = str(item[pos_type_name])
                if item[pos_type_name] in id_json[id_name_json_filename].keys():
                    # print(len(id_json[id_name_json_filename][item[pos_type_name]]))
                    item[pos_type_name] = id_json[id_name_json_filename][
                        item[pos_type_name]
                    ][language_id]
                if item[pos_type_name] not in item_dict[scene_data["sceneId"]].keys():
                    item_dict[scene_data["sceneId"]].update({item[pos_type_name]: []})
                new_folder(
                    os.path.join(
                        result_path, scene_data["sceneId"], item[pos_type_name]
                    )
                )
                pos = [item["pos"]["x"], item["pos"]["y"], item["pos"]["z"]]
                item_dict[scene_data["sceneId"]][item[pos_type_name]].append(pos)
                count(item[pos_type_name])
        # count(scene_data["sceneId"])
    # print(item_dict)
    count_dict_sort = sorted(
        count_dict.items(), key=lambda x: x[1], reverse=True
    )  # 按照value排序
    print(count_dict_sort)
    count_dict = {}
    return item_dict


def get_pos_json(item_json_name):
    item_json_path = os.path.join(os.path.dirname(__file__), "pos", item_json_name)
    with open(item_json_path, "r") as f:
        item_json = json.load(f)
    return item_json


def main___item_point_generate(language_id):
    # language_id = 3  # 0:cn,1:tw,2:en,3:ru
    folader_name = os.path.join(os.path.dirname(__file__), "ID_json")
    id_json = get_all_id_name(folader_name)
    result_path = os.path.join(
        os.path.dirname(__file__),
        "result",
        language_name[language_id],
    )
    #######################################################################
    item_json = get_pos_json(item_json_name)
    item_result_path = os.path.join(result_path, "Item")
    item_dict = json_pos_generate_dict(
        language_id,
        id_json,
        item_json,
        item_result_path,
        pos_type_name="gatherItemId",
        id_name_json_filename="Item.json",
    )
    save_json(item_result_path, item_dict)
    ################################################################
    monster_json = get_pos_json(monster_json_name)
    monster_result_path = os.path.join(result_path, "Monster_And_Animal")
    for k, v in id_json["Monster.json"].items():
        if k in id_json["Animal.json"].keys():
            print(
                k,
                v,
                "-------------------------------------------------------------------------",
            )
    id_json["Monster.json"].update(id_json["Animal.json"])
    monster_dict = json_pos_generate_dict(
        language_id,
        id_json,
        monster_json,
        monster_result_path,
        pos_type_name="monsterId",
        id_name_json_filename="Monster.json",
    )
    save_json(monster_result_path, monster_dict)


if __name__ == "__main__":
    for i in range(4):
        main___item_point_generate(i)
    # main___item_point_generate(0)
    # main___item_point_generate(1)
    # main___item_point_generate(2)
    # main___item_point_generate(3)
