# Find the k closest points to the origin
# Points = [[1, 3], [-2, 2]]
# K = 1
# Output = [-2, 2]

def kClosest(points, k):

    distance = []

    for point in points:
        x = point[0]
        y = point[1]

        d = x*x + y*y

        distance.append([d, point])

    distance.sort()
    result = []

    for i in range(k):
        result.append(distance[i][1])

    return result


points = [[1,3], [-2,2]]
k = 1
print(kClosest(points, k))