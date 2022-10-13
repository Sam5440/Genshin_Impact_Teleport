import zipfile
import os
import datetime

# 获取自身上一级文件目录
def get_parent_dir(n=2):
    current_path = os.path.realpath(__file__)
    for _ in range(n):
        current_path = os.path.dirname(current_path)
    return current_path


current_path = get_parent_dir()
print(current_path)
# raise SystemExit
# 获取当前目录下的所有文件夹
dirs = os.listdir(current_path)
# 获取当前时间
now = datetime.datetime.now()
# 获取当前时间的字符串
now_str = now.strftime("%y-%m-%d-(%Hh%Mm%Ss)")
# 在用户桌面创建压缩包存放目录
releases_path = os.path.join(os.path.expanduser("~"), "Desktop", "release", now_str)
if not os.path.exists(releases_path):
    os.makedirs(releases_path)
# 遍历所有文件夹
for dir in dirs:
    print(dir, "is ziping...")
    if dir.startswith("."):
        continue
    # 获取文件夹的绝对路径
    dir_path = os.path.join(current_path, dir)
    # 判断是否为文件夹
    if os.path.isdir(dir_path):
        # 压缩文件的名称(img打包readme)
        zip_name = os.path.basename(dir_path) if dir != "img" else "readme"
        zip_name += ".zip"
        # 压缩文件的绝对路径
        zip_path = os.path.join(releases_path, zip_name)
        # 创建压缩文件
        z = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        # 遍历文件夹下的所有文件
        for root, dirs, files in os.walk(dir_path):
            # 遍历文件
            for file in files:
                # 获取文件的绝对路径
                file_path = os.path.join(root, file)
                # 写入压缩文件
                z.write(file_path, arcname=file_path.replace(dir_path, dir))
        if dir == "img":
            z.write(os.path.join(current_path, "readme.md"), arcname="readme.md")
        # 关闭压缩文件
        z.close()
        # raise Exception("压缩完成")
# 统计文件大小
total_size = 0
for root, dirs, files in os.walk(releases_path):
    for file in files:
        file_path = os.path.join(root, file)
        total_size += os.path.getsize(file_path)
# print("压缩完成,共生成{}个压缩包,总大小为{}M".format(len(os.listdir(releases_path)), round(total_size/1024/1024, 2)))
# 压缩包存放目录下创建txt文本
release_txt = f"release time:{now_str} \ntotal size:{round(total_size/1024/1024, 2)}M \nspend time:{round((datetime.datetime.now()-now).total_seconds(), 2)}s"
print("-" * 30, "\n", release_txt)
with open(os.path.join(releases_path, "release.txt"), "w") as f:
    f.write(release_txt)
# 打开压缩包存放目录
os.system("explorer %s" % releases_path)
url = "https://github.com/Sam5440/Genshin_Impact_Teleport/releases/new"
# 打开网页
os.system("start %s" % url)
