points = [[2,3,3],[1,2,3],[1,3,4],[2,5,5],[1,3,2]]
def shortest_road(points):
    #要求每个点1以内的距离
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
result = (shortest_road(points))
print(result)
def count_road_long(points):
    #计算路径长度
    long = 0
    for i in range(len(points)-1):
        long += ((points[i][0]-points[i+1][0])**2+(points[i][1]-points[i+1][1])**2+(points[i][2]-points[i+1][2])**2)**0.5
    return long
def best_touch_road(points):
    """_summary_
    1. 以每个点为起点，计算所有路径长度
    2. 选出最短路径
    3.不需要经过所有点,在点1m范围内的点可以忽略
    """
    result = []
    for i in range(len(points)):
        result.append(count_road_long(points[i:]+points[:i]))
    return points[result.index(min(result)):] + points[:result.index(min(result))]
print(best_touch_road(result))

print(result,count_road_long(result))
result2 = [[1, 3, 2], [1, 2, 3], [1, 3, 3], [2, 5, 5],[2, 3, 3],]
print(result2,count_road_long(result2))
import matplotlib.pyplot as plt
import numpy as np


#绘制三维度图像 并且按顺序连接
def draw_3d(points):
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    z = [i[2] for i in points]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
        
draw_3d(result)

