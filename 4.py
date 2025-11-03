
def calculate_distance(route, dist):
    total = 0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]
    
    total += dist[route[-1]][route[0]]
    return total



def get_permutations(data):
    if len(data) == 1:
        return [data]
    
    result = []
    for i in range(len(data)):
        current = data[i]
        remaining = data[:i] + data[i+1:]
        for p in get_permutations(remaining):
            result.append([current] + p)
    return result



dist = [
    [0, 2, 9, 10, 7],
    [1, 0, 6, 4, 3],
    [15, 7, 0, 8, 3],
    [6, 3, 12, 0, 11],
    [9, 7, 5, 6, 0]
]


cities = [0, 1, 2, 3, 4]


routes = get_permutations(cities)


min_distance = float('inf')
best_route = None

for route in routes:
    total = calculate_distance(route, dist)
    if total < min_distance:
        min_distance = total
        best_route = route

print("Shortest route:", best_route)
print("Minimum distance:", min_distance)
