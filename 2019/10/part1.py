import math

def get_angle(point, other):
    delta_x = other[0] - point[0]
    delta_y = other[1] - point[1]
    return math.atan2(delta_y, delta_x)

def can_see(points, point):
    asteroids = dict()
    for other in points:
        angle = get_angle(point, other)
        if angle in asteroids.keys():
            asteroids[angle].append(other)
        else:
            asteroids[angle] = [other]
    return len(asteroids.keys())

def read_input():
    i = 0
    points = []
    for row in [x for x in open("input.txt").read().strip().split('\n')]:
        j = 0
        for point in row:
            if point == '#':
                points.append((j,i)) 
            j+=1
        i+=1
    return points

def get_best_ast(points):
    max_point = ((points[0]))
    max_seen = 0
    for point in points:
      seen = can_see(points, point)
      if seen > max_seen:
          max_seen = seen
          max_point = point
    return max_seen, max_point

print(get_best_ast(read_input()))