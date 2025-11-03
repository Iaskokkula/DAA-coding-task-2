import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist



def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])  
    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist



def closest_pair(points_sorted_x):
    n = len(points_sorted_x)
    
    if n <= 3:
        return brute_force(points_sorted_x)
    
    
    mid = n // 2
    mid_point = points_sorted_x[mid]
    
    left_points = points_sorted_x[:mid]
    right_points = points_sorted_x[mid:]
    
    
    dl = closest_pair(left_points)
    dr = closest_pair(right_points)
    
    
    d = min(dl, dr)
    
    
    strip = [p for p in points_sorted_x if abs(p[0] - mid_point[0]) < d]
    
    
    return min(d, strip_closest(strip, d))



def find_closest_pair(points):
    points_sorted_x = sorted(points, key=lambda point: point[0])
    return closest_pair(points_sorted_x)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]


min_distance = find_closest_pair(points)
print("The smallest distance is:", round(min_distance, 4))
