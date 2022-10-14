import json
import os

encoding_code = "utf-8"


def txt_to_json(txt_file, split, json_path):
    # 内容按行读取,每行按split分割,生成字典,再转换为json
    with open(txt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(split) for line in lines]
        lines = [{line[0]: line[1]} for line in lines]
        # print(lines)
        # 写入json文件(中文显示正常)
        with open(json_path, "w", encoding=encoding_code) as f:
            lines = json.dumps(lines, ensure_ascii=False, indent=4)
            f.write(lines)


if __name__ == "__main__":
    # txt_to_json('Animal.txt', ':', 'id-name.json')
    # 获得ID文件夹下的文件目录
    path = os.path.dirname(__file__)
    path_id_json = os.path.join(path, "ID_json")
    path_id = os.path.join(path, "ID")
    try:
        os.mkdir(path_id_json)
    except FileExistsError:
        pass
    files = os.listdir(path_id)
    for file in files:
        if os.path.splitext(file)[1] == ".txt":
            txt_to_json(
                os.path.join(path_id, file),
                ":",
                os.path.join(path_id_json, os.path.splitext(file)[0] + ".json"),
            )

# Path: id-name-json-generate.py
