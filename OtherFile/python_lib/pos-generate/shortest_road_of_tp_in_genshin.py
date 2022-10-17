points = [[2,3,3],[1,2,3],[1,3,4],[2,5,5],[1,3,2]]
def shortest_lines(points):
    #3D coordinates The shortest path
    # points = [[2,3,3],[1,2,3],[1,3,4],[2,5,5],[1,3,2]]
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