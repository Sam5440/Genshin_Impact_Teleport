# coding:utf-8

import json
import math
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 辅助函数
def get_scene_name(sceneid: int, lag: int):
    with open(f"Data/Scene.json", "r", encoding="UTF-8") as f:
        js = json.load(f)
    return js[f"{sceneid}"][lag]


def get_type_name(typestr: str, lag: int):
    typename = {
        "Monster": ["怪物", "怪物", "Monster"],
        "Animals": ["动物", "動物", "Animals"],
        "Plant": ["植物", "植物", "Plant"],
        "Ore": ["矿物", "礦物", "Ore"],
    }
    return typename[typestr][lag]


def get_kind_name(kindstr: str, lag: int):
    kindname = {
        "SmallSlime": ["小史莱姆", "繁体1", "SmallSlime"],
        "BigSlime": ["大史莱姆", "繁体1", "BigSlime"],
        "Slime": ["史莱姆", "繁体1", "Slime"],
        "EyeOfStrom": ["狂风之核", "繁体1", "EyeOfStrom"],
        "Spector": ["漂浮灵", "繁体1", "Spector"],
        "Hilichurl": ["丘丘人", "繁体1", "Hilichurl"],
        "HilichurlShooter": ["丘丘人射手", "繁体1", "HilichurlShooter"],
        "UnusualHilichurl": ["大伟丘", "繁体1", "UnusualHilichurl"],
        "Mitachurl": ["丘丘人暴徒", "繁体1", "Mitachurl"],
        "HilichurlKing": ["丘丘王", "繁体1", "HilichurlKing"],
        "HilichurlSama": ["丘丘萨满", "繁体1", "HilichurlSama"],
        "AbyssMage": ["深渊法师", "繁体1", "AbyssMage"],
        "AbyssHerald": ["深渊使徒", "繁体1", "AbyssHerald"],
        "SmallWolve": ["兽境幼犬", "繁体1", "SmallWolve"],
        "BigWolve": ["兽境猎犬", "繁体1", "BigWolve"],
        "Wolve": ["全兽境猎犬", "繁体1", "Wolve"],
        "BlackSerpents": ["黑蛇骑士", "繁体1", "BlackSerpents"],
        "Fatui": ["愚人众", "繁体1", "Fatui"],
        "FatuiAgent": ["讨债人", "繁体1", "FatuiAgent"],
        "FatuiCiciMage": ["莹术士", "繁体1", "FatuiCiciMage"],
        "fatuiMirrorMaiden": ["藏镜仕女", "繁体1", "fatuiMirrorMaiden"],
        "RuinGuard": ["遗迹守卫and猎手", "繁体1", "RuinGuard"],
        "RuinGrader": ["遗迹重机", "繁体1", "RuinGrader"],
        "RuinSentinel": ["遗迹机兵", "繁体1", "RuinSentinel"],
        "TreasureHoarder": ["盗宝团", "繁体1", "TreasureHoarder"],
        "Nobushi": ["浪人", "繁体1", "Nobushi"],
        "Kairagi": ["海乱鬼", "繁体1", "Kairagi"],
        "Samurai": ["武士", "繁体1", "Samurai"],
        "WhopperFlower": ["骗骗花", "繁体1", "WhopperFlower"],
        "SmallGeovishap": ["小龙蜥", "繁体1", "SmallGeovishap"],
        "BigGeovishap": ["大龙蜥", "繁体1", "BigGeovishap"],
        "Geovishap": ["全龙蜥", "繁体1", "Geovishap"],
        "Cicin": ["蚊子", "繁体1", "Cicin"],
        "SmallFugi": ["小蕈兽", "繁体1", "SmallFugi"],
        "BigFugi": ["大蕈兽", "繁体1", "BigFugi"],
        "Fugi": ["全蕈兽", "繁体1", "Fugi"],
        "RuinDrake": ["遗迹龙兽", "繁体1", "RuinDrake"],
        "SmallEreMites": ["小镀金", "繁体1", "SmallEreMites"],
        "BigEreMites": ["大镀金", "繁体1", "BigEreMites"],
        "EreMites": ["全镀金", "繁体1", "EreMites"],
        "PrimalConstruct": ["元能构装体", "繁体1", "PrimalConstruct"],
        "Crab": ["螃蟹", "繁体1", "Crab"],
        "Lizard": ["蜥蜴", "繁体1", "Lizard"],
        "Loach": ["啾啾", "繁体1", "Loach"],
        "Frog": ["青蛙", "繁体1", "Frog"],
        "Unagi": ["鳗鱼", "繁体1", "Unagi"],
        "Fish": ["鱼肉", "繁体1", "Fish"],
        "CrystalCore": ["晶核", "繁体1", "CrystalCore"],
        "Scrab": ["圣金虫", "繁体1", "Scrab"],
        "RawMeat_Drop1": ["兽肉_掉落1", "繁体1", "RawMeat_Drop1"],
        "RawMeat_Drop2": ["兽肉_掉落2", "繁体1", "RawMeat_Drop2"],
        "RawMeat_Drop3": ["兽肉_掉落3", "繁体1", "RawMeat_Drop3"],
        "RawMeat_Drop4o5": ["兽肉_掉落4或5", "繁体1", "RawMeat_Drop4o5"],
        "Fowl_Drop1": ["禽肉_掉落1", "繁体1", "Fowl_Drop1"],
        "Fowl_Drop2": ["禽肉_掉落2", "繁体1", "Fowl_Drop2"],
        "Fowl_Drop3": ["禽肉_掉落3", "繁体1", "Fowl_Drop3"],
        "FrozenBoat": ["冻猪", "繁体1", "FrozenBoat"],
        "Daobaoyou": ["盗宝鼬", "繁体1", "Daobaoyou"],
        "LucklightFly": ["吉光虫", "繁体1", "LucklightFly"],
        "Apple": ["苹果", "繁体1", "Apple"],
        "Sensettia": ["日落果", "繁体1", "Sensettia"],
        "Mushroom": ["蘑菇", "繁体1", "Mushroom"],
        "SweetFlower": ["甜甜花", "繁体1", "SweetFlower"],
        "Carrot": ["胡萝卜", "繁体1", "Carrot"],
        "Radish": ["白萝卜", "繁体1", "Radish"],
        "Snapdragon": ["金鱼草", "繁体1", "Snapdragon"],
        "Mint": ["薄荷", "繁体1", "Mint"],
        "Pinecone": ["松果", "繁体1", "Pinecone"],
        "Wolfhook": ["钩钩果", "繁体1", "Wolfhook"],
        "Valberry": ["落落莓", "繁体1", "Valberry"],
        "Cecillia": ["塞西莉亚花", "繁体1", "Cecillia"],
        "WindeWhellAster": ["风车菊", "繁体1", "WindeWhellAster"],
        "PhilanemoMushroom": ["慕风蘑菇", "繁体1", "PhilanemoMushroom"],
        "LotusHead": ["莲蓬", "繁体1", "LotusHead"],
        "JueyunChili": ["绝云椒椒", "繁体1", "JueyunChili"],
        "SilkFlower": ["霓裳花", "繁体1", "SilkFlower"],
        "GlazeLily": ["琉璃百合", "繁体1", "GlazeLily"],
        "Qingxin": ["清心", "繁体1", "Qingxin"],
        "Horsetail": ["马尾", "繁体1", "Horsetail"],
        "Starconch": ["星螺", "繁体1", "Starconch"],
        "Violetgrass": ["琉璃袋", "繁体1", "Violetgrass"],
        "Berry": ["树莓", "繁体1", "Berry"],
        "MistFlower": ["冰雾花", "繁体1", "MistFlower"],
        "FlamingFlower": ["火焰花", "繁体1", "FlamingFlower"],
        "SmallLampGrass": ["小灯草", "繁体1", "SmallLampGrass"],
        "CallaLily": ["嘟嘟莲", "繁体1", "CallaLily"],
        "DandelionSeed": ["蒲公英", "繁体1", "DandelionSeed"],
        "BirdEgg": ["鸟蛋", "繁体1", "BirdEgg"],
        "Matsutake": ["松茸", "繁体1", "Matsutake"],
        "BambooShoot": ["竹笋", "繁体1", "BambooShoot"],
        "Onikabuto": ["鬼兜虫", "繁体1", "Onikabuto"],
        "SakulaBloom": ["绯樱绣球", "繁体1", "SakulaBloom"],
        "CrystalMarrow": ["晶化骨髓", "繁体1", "CrystalMarrow"],
        "Dendrobium": ["血斛", "繁体1", "Dendrobium"],
        "NakuWeed": ["鸣草", "繁体1", "NakuWeed"],
        "SeaGanoderma": ["海灵芝", "繁体1", "SeaGanoderma"],
        "SangoPearl": ["珊瑚珍珠", "繁体1", "SangoPearl"],
        "AmakumoFruit": ["天云草实", "繁体1", "AmakumoFruit"],
        "FluorescentFungus": ["幽灯蕈", "繁体1", "FluorescentFungus"],
        "SeaGrass": ["海草", "繁体1", "SeaGrass"],
        "LavenderMelon": ["堇瓜", "繁体1", "LavenderMelon"],
        "Starshroom": ["星蕈", "繁体1", "Starshroom"],
        "RukkhashavaMushroom": ["树王圣体菇", "繁体1", "RukkhashavaMushroom"],
        "Padisarah": ["帕莎拉蒂", "繁体1", "Padisarah"],
        "NilotpalaLotus": ["月莲", "繁体1", "NilotpalaLotus"],
        "HarraFruit": ["香辛果", "繁体1", "HarraFruit"],
        "KalpalataLotus": ["劫莲波", "繁体1", "KalpalataLotus"],
        "ZaytunPeach": ["墩墩桃", "繁体1", "ZaytunPeach"],
        "SumeruRose": ["须弥玫瑰", "繁体1", "SumeruRose"],
        "Redcrest": ["赤念果", "繁体1", "Redcrest"],
        "AjilenakhNut": ["枣椰", "繁体1", "AjilenakhNut"],
        "NoctilucousJade": ["夜泊石", "繁体1", "NoctilucousJade"],
        "ElectroCrystal": ["电气水晶", "繁体1", "ElectroCrystal"],
        "CorLapis": ["石珀", "繁体1", "CorLapis"],
        "IronChunk": ["铁矿", "繁体1", "IronChunk"],
        "WhiteChunk": ["白铁矿", "繁体1", "WhiteChunk"],
        "CrystalChunk": ["水晶矿", "繁体1", "CrystalChunk"],
        "MagicalCrystalChunk": ["魔晶矿", "繁体1", "MagicalCrystalChunk"],
        "StarSilver": ["星银矿", "繁体1", "StarSilver"],
        "AmethystLump": ["紫晶矿", "繁体1", "AmethystLump"],
    }
    return kindname[kindstr][lag]


def distance3d(dic1: dict, dic2: dict):
    return math.sqrt(
        (dic1["x"] - dic2["x"]) ** 2
        + (dic1["y"] - dic2["y"]) ** 2
        + (dic1["z"] - dic2["z"]) ** 2
    )


def distance2d(dic1: dict, dic2: dict):
    return math.sqrt((dic1["x"] - dic2["x"]) ** 2 + (dic1["z"] - dic2["z"]) ** 2)


def min_dist_sort(lst: list):
    new_list = [lst.pop(0)]

    while len(lst) > 0:
        min_dist = 100000000
        min_pos = {}
        for i in lst:
            end = new_list[-1]
            dist = distance3d(i, end)
            if min_dist >= dist:
                min_dist = dist
                min_pos = i
        new_list.append(min_pos)
        lst.remove(min_pos)
        # draw_map3d(new_list)
    return new_list


def sort(lst: list):
    if len(lst) >= 2:
        new_list = [lst.pop(0), lst.pop(0)]
    elif len(lst) >= 1:
        new_list = [lst.pop(0)]
    else:
        print("list为空")
        return []

    while len(lst) > 0:
        pop = lst.pop(0)  # 弹出lst首位
        start = new_list[0]
        end = new_list[-1]
        # 计算插入列表首位产生的代价
        cost_start = distance3d(pop, start)
        # 计算插入列表尾部产生的代价
        cost_end = distance3d(pop, end)

        # 检测插入列表中产生的最小代价
        min_cost = 10000000000
        min_index = -1
        for i in range(len(new_list) - 1):
            A = new_list[i]
            B = new_list[i + 1]
            distance_AB = distance3d(A, B)
            distance_A = distance3d(A, pop)
            distance_B = distance3d(B, pop)
            cost = distance_A + distance_B - distance_AB
            if min_cost >= cost:
                min_cost = cost
                min_index = i

        # 判断最小代价
        if cost_start <= cost_end and cost_start <= min_cost:  # 插入列表首代价最小
            new_list.insert(0, pop)
        if cost_end <= cost_start and cost_end <= min_cost:  # 插入列表尾代价最小
            new_list.insert(len(new_list), pop)
        if min_cost <= cost_start and min_cost <= cost_end:  # 插入列表中代价最小
            new_list.insert(min_index + 1, pop)
        # draw_map3d(new_list)
    return new_list


def draw_map3d(lst: list):
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(projection="3d")

    ax.set_xlabel("X label")  # 画出坐标轴
    ax.set_ylabel("z label")
    ax.set_zlabel("y label")

    x = []
    y = []
    z = []
    for i in lst:
        x.append(i["x"])
        y.append(i["y"])
        z.append(i["z"])
    ax.scatter(x, z, y)
    ax.plot(x, z, y)
    plt.show()


def DeletePos(lst: list, ran: int = 0):
    remove = []
    pos_list = lst
    if ran > 0:
        for i in range(len(pos_list) - 1):
            distance = distance3d(pos_list[i], pos_list[i + 1])
            if distance < ran:
                remove.append(pos_list[i + 1])
        for i in remove:
            pos_list.remove(i)
    return pos_list


def DeletePos_v2(lst: list, ran: int = 0):
    pos_list = lst
    new_list = []
    if ran > 0:
        pos = 0
        check = 1
        while pos_list:
            if len(pos_list) == 1:
                new_list.append(pos_list[0])
                pos_list.remove(pos_list[0])
                continue
            for i in range(check):
                dist = distance3d(pos_list[i], pos_list[check])
                if dist > ran:
                    # pos为最优点位 删除最优点位周围的点
                    new_list.append(pos_list[pos])
                    # 删除上半点位
                    remove = []
                    for j in range(pos):
                        remove.append(pos_list[j])
                    # 删除下半点位
                    for k in range(pos, len(lst)):
                        dist = distance3d(pos_list[pos], pos_list[k])
                        if dist > ran:
                            break
                        else:
                            remove.append(pos_list[k])
                    # 删除点位
                    for re in remove:
                        pos_list.remove(re)
                    pos = -1
                    check = 0
                    break
            pos = check

            if pos == len(pos_list) - 1:
                # pos为最优点位 删除最优点位周围的点
                new_list.append(pos_list[pos])
                # 删除上半点位
                remove = []
                for j in range(pos):
                    remove.append(pos_list[j])
                # 删除下半点位
                for k in range(pos, len(lst)):
                    dist = distance3d(pos_list[pos], pos_list[k])
                    if dist > ran:
                        break
                    else:
                        remove.append(pos_list[k])
                # 删除点位
                for re in remove:
                    pos_list.remove(re)
                pos = 0
                check = 0
                break

            check = check + 1
    return new_list


# create_type = "Starshroom"
# scene = 3
# json_prefix = "teyvat_" + "Starshroom" + "_"

create_mode = 1  # 0:自动生成 1:自定义生成 99:测试
language = 0  # 0=Simplified Chinese 1=Traditional Chinese 2=EN
y_offset = 3
AL_Range = 18

sort_type = 1  # 0:最近距离点位排序  1:# 最小代价插入排序

if sort_type == 0:
    sort_method = min_dist_sort
elif sort_type == 1:
    sort_method = sort
else:
    sort_type = sort  # 默认
    print("sort_type无法识别，默认为最小代价插入排序")


def CreateAllPos(data):
    kind_js = data  # 拷贝
    for item_type_key in kind_js:  # 循环遍历所有type的item
        if item_type_key == "Monster" or item_type_key == "Animals":
            load_json_filename = "Spawns.json"
            spawns_json_key_str = "monsterId"
        elif item_type_key == "Plant" or item_type_key == "Ore":
            load_json_filename = "GadgetSpawns.json"
            spawns_json_key_str = "gatherItemId"
        else:
            print("item_type匹配失败，请检查代码")
            return

        item_type = kind_js[item_type_key]  # 当前循环的type
        # 遍历所有key
        for item_key in item_type:
            print(f"正在查找 {get_kind_name(item_key, language)} 的坐标...")
            id_group = item_type[item_key]
            if not id_group:
                print(f"id_group为空，请检查代码")
                return

            # 读取spawns json
            with open(f"Data/{load_json_filename}", "r") as f:
                spawns_js = json.load(f)
            # 获取scene json
            with open(f"Data/Scene.json", "r", encoding="UTF-8") as f:
                scene_js = json.load(f)

            # 遍历坐标
            pos_list = []
            # 遍历所有世界
            for scene_key in scene_js:
                for spawns_group in spawns_js:
                    # 找到 大世界的group
                    if spawns_group["sceneId"] == int(scene_key):
                        spawns = spawns_group["spawns"]
                        for spawn in spawns:
                            if not spawns_json_key_str in spawn:  # 查询是否有存在 id_key
                                continue
                            if (
                                spawn[spawns_json_key_str] in id_group
                            ):  # 查询id_key 的值是否为我们需要的id
                                print(
                                    f"该坐标为 {get_kind_name(item_key, language)},"
                                    f'{spawns_json_key_str}={spawn[spawns_json_key_str]},pos={spawn["pos"]}'
                                )
                                pos_list.append(spawn["pos"])
                monster_count = 0
                if pos_list:
                    monster_count = len(pos_list)
                    print(
                        f"世界:{get_scene_name(scene_key, language)} 总怪物数:{monster_count}"
                    )
                else:
                    print(f"找不到任何坐标")
                if not pos_list:  # 为 空 不执行后续动作
                    continue
                flist = sort_method(pos_list)

                # 删除小于指定距离的坐标
                flist = DeletePos_v2(flist, AL_Range)
                print(f"坐标数：{len(flist)}")
                # 生成json文件
                count = 1
                path = (
                    f"pos/{get_type_name(item_type_key, language)}/"
                    f"{get_kind_name(item_key, language)}/"
                    f"{get_scene_name(scene_key, language)}"
                )
                for i in flist:
                    if not os.path.exists(path):
                        os.makedirs(path)
                    name = f"{get_scene_name(scene_key, language)}_{get_kind_name(item_key, language)}_{count}"
                    with open(f"{path}/{name}.json", "w") as f:
                        write_js = {
                            "description": "",
                            "name": f"{get_scene_name(scene_key, 2)}_{get_kind_name(item_key, 2)}_{count}",
                            "position": [i["x"], i["y"] + y_offset, i["z"]],
                        }
                        json.dump(write_js, f)
                        count = count + 1
                with open(f"{path}/总数{monster_count}.txt", "w") as f:
                    f.close()


def CustomCustomMaterials(
    offset_y: int = 5,
    al_range: int = 12,
    filename: str = "MyRoute",
    lag: int = 0,
    prefix: str = "No.",
):
    all_list = []  # 总列表
    items = [
        "IronChunk",
        "WhiteChunk",
        "CrystalChunk",
        "MagicalCrystalChunk",
        "StarSilver",
        "AmethystLump",
        "Wolfhook",
        "Valberry",
        "Cecillia",
        "WindeWhellAster",
        "PhilanemoMushroom",
        "SmallLampGrass",
        "CallaLily",
        "DandelionSeed",
        "NoctilucousJade",
        "SilkFlower",
        "GlazeLily",
        "Starconch",
        "Violetgrass",
        "CorLapis",
        "Onikabuto",
        "CrystalMarrow",
        "Dendrobium",
        "SangoPearl",
        "FluorescentFungus",
        "RukkhashavaMushroom",
        "Padisarah",
        "NilotpalaLotus",
        "KalpalataLotus",
        "Redcrest",
        "Scrab",
        "Horsetail",
        "MistFlower",
        "FlamingFlower",
        "ElectroCrystal",
        "Frog",
        "Lizard",
        "CrystalCore",
        "Loach",
        "Snapdragon",
        "LotusHead",
        "Matsutake",
        "Crab",
        "BambooShoot",
        "Unagi",
        "LavenderMelon",
        "AjilenakhNut",
    ]
    items_count = {}
    # 读取kind.json
    with open(f"kind.json", "r") as f:
        kind_json = json.load(f)

    for item in items:
        # 判断item属于什么分类 Monsters/Animals Plant/Ore 选择读取的json
        item_kind = ""
        for kind in kind_json:
            if item in kind_json[kind]:
                item_kind = kind
        if item_kind == "Monster" or item_kind == "Animals":
            spawns_json_name = "Spawns.json"
            spawns_json_key_str = "monsterId"
        elif item_kind == "Plant" or item_kind == "Ore":
            spawns_json_name = "GadgetSpawns.json"
            spawns_json_key_str = "gatherItemId"
        else:
            print(f"item_kind无法对应，请检查代码")
            return
        # 读取 坐标json
        with open(f"Data/{spawns_json_name}", "r") as f:
            spawns_json = json.load(f)
        # 获取item的id_Group
        id_group = kind_json[item_kind][item]
        # 遍历获取坐标
        item_pos_list = []  # item的坐标list
        # 遍历json 第一轮 找出 scene 符合的 SpawnsGroup
        for i in spawns_json:
            if i["sceneId"] != 3:  # 不符合条件的SpawnsGourp直接跳过
                continue
            spawns = i["spawns"]  # 符合条件的group中的spawns
            for spawn in spawns:
                if spawns_json_key_str not in spawn:  # 如果不存在对应key 则跳过
                    continue
                if spawn[spawns_json_key_str] in id_group:  # 如果id在id_group中则记录坐标
                    item_pos_list.append(spawn["pos"])
        if item_pos_list:
            all_list = all_list + item_pos_list
            items_count[item] = len(item_pos_list)  # 记录 点位数量
        print(f"item:{item}\n{item_pos_list}")
    print(items_count)
    # 加载额外的json坐标 只排序 不剔除
    extra_item_all_list = []
    extra_items = os.listdir(f"ExtraPos")
    for extra_item in extra_items:  # 遍历所有文件夹
        extra_item_pos_list = []
        if not os.path.isdir(f"ExtraPos/{extra_item}"):  # 如果不是文件夹则跳过
            continue
        extra_item_jsons = os.listdir(f"ExtraPos/{extra_item}")  # 遍历所有json
        for extra_item_json_filename in extra_item_jsons:
            if not extra_item_json_filename.endswith(".json"):  # 如果不是json文件则跳过
                continue
            with open(f"ExtraPos/{extra_item}/{extra_item_json_filename}", "r") as f:
                extra_item_json = json.load(f)
            extra_item_pos_list.append(
                {
                    "x": extra_item_json["position"][0],
                    "y": extra_item_json["position"][1],
                    "z": extra_item_json["position"][2],
                }
            )
        if extra_item_pos_list:
            extra_item_all_list = extra_item_all_list + extra_item_pos_list
            items_count[extra_item] = len(extra_item_pos_list)  # 记录 点位数量
    draw_map3d(all_list)
    # 对all list 进行排序 和 剔除
    all_list = sort_method(all_list)
    draw_map3d(all_list)
    # 删除小于指定距离的坐标
    all_list = DeletePos_v2(all_list, al_range)

    draw_map3d(all_list)

    all_list = all_list + extra_item_all_list

    draw_map3d(all_list)
    # 再排序一次
    all_list = sort_method(all_list)

    draw_map3d(all_list)

    # 生成json
    count = 1
    path = f"CustomRoute/{filename}"
    for i in all_list:
        if not os.path.exists(f"{path}"):
            os.makedirs(f"{path}")
        name = prefix + str(count).rjust(5, "0")
        with open(f"{path}/{name}.json", "w") as f:
            write_js = {
                "description": "",
                "name": name,
                "position": [i["x"], i["y"] + offset_y, i["z"]],
            }
            json.dump(write_js, f)
            count = count + 1
    # 总点位数
    pos_count = 0
    for count in items_count:
        pos_count = pos_count + items_count[count]
    with open(f"{path}/总数{pos_count}.txt", "w") as f:
        for count in items_count:
            f.write(f"{get_kind_name(count, lag)}:{items_count[count]}\n")
        f.close()


def main():
    # 加载Data json
    with open(f"kind.json", "r") as f:
        js_data = json.load(f)
    # 检测create_mode
    if create_mode == 0:
        CreateAllPos(js_data)
    elif create_mode == 1:
        CustomCustomMaterials(3, 13, "MyRoute", 0, "No.")
    elif create_mode == 99:
        templst = [{"x": i, "y": 0, "z": 0} for i in range(0, 30)]
        print(templst)
        templst = DeletePos_v2(templst, 13)
        print(templst)


if __name__ == "__main__":
    main()
