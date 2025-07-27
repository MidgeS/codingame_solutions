def calculateDistance(position, target):
    dist_x = abs(target[0] - position[0])
    dist_y = abs(target[1] - position[1])
    dist = dist_x + dist_y
    return dist