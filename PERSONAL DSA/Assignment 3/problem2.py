# Given three points, check whether they ie on a straight(collinear) or not. [GOOGLE]

# For example:
# Input- [(1,1), (1,6), (0,9)]
# Output- No

# Input- [(1,1), (1,4), (1,5)]
# Output- Yes

def isCollinear(points):

    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return "Yes"

    return "No"


points = [(1,1), (1,4), (1,5)]
print(isCollinear(points))