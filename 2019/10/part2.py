import math

def dist(x, y):
    return abs(y[0]-x[0]) + abs(y[1]-x[1])

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
    return asteroids, len(asteroids.keys())

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
    max_asts = dict()
    for point in points:
      asteroids, seen = can_see(points, point)
      if seen > max_seen:
          max_seen = seen
          max_point = point
          max_asts = asteroids
    return max_asts, max_point

points = read_input()
asteroids, centre = get_best_ast(points)
destroyed = 0
looked_up = False
while destroyed < 201:
    for angle in sorted(asteroids.keys(), reverse=False):
        # lol magic numbers
        if angle == -1.5707963267948966:
            looked_up = True
        if looked_up:
            destroyed += 1
            if destroyed == 200:
                # read the first because destroying sutff doesnt matter as 284 seen > 200
                print(sorted(asteroids[angle], key=lambda x: dist(x, centre))[0])  



