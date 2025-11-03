


values = [20, 5, 10, 40, 15, 25]


weights = [1, 2, 3, 8, 7, 4]


capacity = 10



def calc_total(selection):
    total_value = 0
    total_weight = 0
    for i in range(len(selection)):
        if selection[i] == 1:  
            total_value += values[i]
            total_weight += weights[i]
    return total_value, total_weight



def generate_combinations(n):
    if n == 0:
        return [[]]
    smaller = generate_combinations(n - 1)
    result = []
    for s in smaller:
        result.append(s + [0]) 
        result.append(s + [1])  
    return result



all_combinations = generate_combinations(6)

max_value = 0
best_selection = None

for sel in all_combinations:
    total_value, total_weight = calc_total(sel)
    if total_weight <= capacity and total_value > max_value:
        max_value = total_value
        best_selection = sel


print("Best selection (0=not taken, 1=taken):", best_selection)
print("Maximum value that can be carried:", max_value)
