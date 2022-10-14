import json
import os
import time

time.sleep(1)
only_number = lambda s: "".join(filter(str.isdigit, s))


def remove_start_space(s):
    if s.startswith(" "):
        return remove_start_space(s[1:])
    else:
        return s


if __name__ == "__main__":
    need_file = ["Animal.txt","Item.txt","Monster.txt","Scene.txt"]
    need_path = ["zh-cn", "zh-tw", "en-us", "ru-ru"]

    # 获得ID文件夹下的文件目录
    path = os.path.dirname(__file__)
    path_id_json = os.path.join(path, "ID_json")
    path_id = os.path.join(path, "ID")
    try:
        os.mkdir(path_id_json)
    except FileExistsError:
        pass
    for file in need_file:
        file_data = {}
        for path in need_path:
            with open(os.path.join(path_id, path, file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines]
                lines = [line.split(":") for line in lines]
                # only_number 去除乱码编号,,开头空格
                lines = [
                    [only_number(line[0]), remove_start_space(line[1])]
                    for line in lines
                ]
                lines_dict = {}
                for line in lines:
                    lines_dict[line[0]] = [line[1]]
                file_data[path] = lines_dict
            if path != need_path[0]:
                # print(type(file_data[need_path[0]]))
                for k, v in file_data[need_path[0]].items():
                    # print(k,v)
                    if k in file_data[path]:
                        file_data[need_path[0]][k].append(file_data[path][k][0])
                        # print(file_data[path][k])
        # print(file_data)
        with open(
            os.path.join(path_id_json, file.replace(".txt", ".json")),
            "w",
            encoding="utf-8",
        ) as f:
            lines = json.dumps(
                file_data[need_path[0]],
                ensure_ascii=False,
                indent=4,
            )
            f.write(lines)
    # for file in files:
    #     print(file)
    #     if os.path.splitext(file)[1] == ".txt":
    #         txt_to_json(
    #             os.path.join(path_id, file),
    #             ":",
    #             os.path.join(path_id_json, os.path.splitext(file)[0] + ".json"),
    #         )

# Path: id-name-json-generate.py
