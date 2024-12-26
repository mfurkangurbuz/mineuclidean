import math

points = [(1, 1), (2, 2), (3, 1), (4, 3)]

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")