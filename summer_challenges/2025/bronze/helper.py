def calculateDistance(position, target):
    dist_x = abs(target[0] - position[0])
    dist_y = abs(target[1] - position[1])
    dist = dist_x + dist_y
    return dist

def clampValues(value, min_value, max_value):
    return min(max_value, max(min_value, value))