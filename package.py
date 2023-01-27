import time
import zipfile

# import sys
import os
from urllib.parse import quote
print("Don't Run in Your Computer, Run in Server")
time.sleep(10)
except_folders = [".git", ".vscode", "zips"]
no_zip_folders = [
    "AutoGeneratePoint",
    "Genshin_Impact_Teleport",
]  # "ManualCollectPoint"]

# 获得当前路径
path = os.getcwd()
path_zips = path+"/zips"
def log(text):
    text = str(text)
    # print(text)
    # 写入文件
    with open(path_zips+"/log.txt", "a", encoding="utf-8") as f:
        f.write(text+"\n")
        f.close()
        
def readme_create(readme_path, text):
    decode_code = "utf-8"
    text = text.encode().decode(decode_code)
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding=decode_code) as f:
            #写入时间
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(f"# {time_now}\n\n")
            f.close()
    # 在readme文件后面补充一行
    with open(readme_path, "a", encoding=decode_code) as f:
        f.write(text)
        f.close()
# t= """
# (Raw)[cn-en-ru]\ru-ru\Monster_And_Animal\ID1-BigWorld_LevelStreaming\ID20010401-Большой Анемо слайм
# ### [文件夹](http://www.baidu.com)"""
# readme_create(path+"/readme2.md", t)
# exit()
def zip_folder(source_dir, output_filename):
    zip = zipfile.ZipFile(output_filename, "w")
    pre_len = len(os.path.dirname(source_dir))
    for parent, _, filenames in os.walk(source_dir):
        for filename in filenames:
            path_file = os.path.join(parent, filename)
            arc_name = path_file[pre_len:].strip(os.path.sep)  # 相对路径
            zip.write(path_file, arc_name)
    zip.close()


def get_folder_files(path):
    for root, dirs, files in os.walk(path):
        # 在dir中删除except_folders出现的文件夹
        for folder in except_folders:
            if folder in dirs:
                dirs.remove(folder)
        return {"root": root, "dirs": dirs, "files": files}


def get_path_tree(path):
    folder_files = get_folder_files(path)
    root = folder_files["root"]
    dirs = folder_files["dirs"]
    files = folder_files["files"]
    path_tree = []
    # for file in files:
    #     path_tree.append(os.path.join(root,file))
    for dir in dirs:
        path_tree.append(os.path.join(root, dir))
        path_tree += get_path_tree(os.path.join(root, dir))
    return path_tree




# 获得当前路径下的所有文件
path_tree = get_path_tree(path)
# 保存path_tree的str
# with open(path+"/path_tree.txt", "w",encoding=decode_code) as f:
#     f.write(str(path_tree).encode().decode('unicode_escape'))
#     f.close()

# exit()
zip_task = {}
# 创建文件夹根据path_tree
for file in path_tree:
    zip_task[file] = [
        file.replace(path, path + "\\zips"),
        file.replace(path, "zips") + ".zip",
    ]
    if not os.path.exists(zip_task[file][0]):
        os.makedirs(zip_task[file][0])
i, l = 0, len(zip_task.keys())


def endwith_check(endwith_str):
    for check_str in no_zip_folders:
        if endwith_str.endswith(check_str):
            return True
    return False
os.system("rmdir /s /q .git")

for k, v in zip_task.items():
    # print(k,v)
    zip_name = v[1].split("\\")[-1]
    log(zip_name)
    # exit()
    i += 1
    log(f"进度：{i}/{l}\n=======压缩文件夹：{k}->{v[1]}")
    if endwith_check(k):
        log(f"进度：{i}/{l}\n=======跳过文件夹：{k}->{v[1]}")
        continue
    zip_folder(k, v[1].replace("\\", "/"))
    readme_path = os.path.dirname(v[0]) + "/readme.md"
    # 获得压缩包文件名
    
    url = (
        "https://raw.githubusercontent.com/Sam5440/Genshin_Impact_Teleport_Files/main/"
        + quote(v[1].replace("\\", "/").replace("zips/", ""))
    )
    # print(f"进度：{i}/{l}\n=======写入readme：{k}->{v[1]}")
    
    readme_create(readme_path, f"### [{zip_name}]({url})\n\n")





#删除全部空文件夹 

del_folders = []
for root, dirs, files in os.walk(path_zips, topdown=False):
    for name in dirs:
        if not os.listdir(os.path.join(root, name)):
            del_folders.append(os.path.join(root, name))
            os.rmdir(os.path.join(root, name))
log(del_folders)

push_bat = """
cd ./zips
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:Sam5440/Genshin_Impact_Teleport_Files
git push -u origin main -f
""".strip()

with open(path_zips+"/push.bat", "w") as f:
    f.write(push_bat)
    f.close()
    
#创建目录.github/workflows
if not os.path.exists(path_zips+"/.github/workflows"):
    os.makedirs(path_zips+"/.github/workflows")
#创建文件.github/workflows/main.yml
main_yml = """
name: Auto-run package.py
on:
    workflow_dispatch:
    schedule:
     - cron: '0 8 * * *'
jobs:
  run-package:
    runs-on: windows-latest
    steps:
    - name: Git long allow
      run : git config --global core.longpaths true
    - name: Git clone
      run: git clone https://github.com/Sam5440/Genshin_Impact_Teleport
    - name: Run package.py
      run: python Genshin_Impact_Teleport/package.py
    - name: Auto push
      run: |
        cd ./zips
        git init
        git config --local user.email "Y_sam5440@outlook.com"
        git config --local user.name "Sam5440"
        git add .
        git commit --allow-empty -m "daily sync"
        git branch -m master main
        git remote add origin https://${{ github.actor }}:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}
        git push -u origin main -f
"""
with open(path_zips+"/.github/workflows/main.yml", "w") as f:
    f.write(main_yml)
    f.close()

log("完成")

# # 运行push.bat
# push_confirm = "yes" #input(f"是否push？(yes/no)")
# if push_confirm == "yes":
#     os.system(path_zips+"/push.bat")
#     log("push")
# else:
#     log("不push")

# del_confirm = input(f"是否删除压缩文件夹？(yes/no)path:{path_zips}")
# if del_confirm == "yes":
#     os.system("rmdir /s /q "+path_zips.replace("/","\\"))
#     log("删除压缩文件夹")
# else:
#     log("不删除压缩文件夹")
