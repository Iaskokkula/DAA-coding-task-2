
def calculate_total(weights, values, selection):
    total_weight = 0
    total_value = 0
    for i in range(len(selection)):
        if selection[i] == 1:  
            total_weight += weights[i]
            total_value += values[i]
    return total_weight, total_value



def get_combinations(n):
    if n == 0:
        return [[]]
    smaller = get_combinations(n - 1)
    result = []
    for combo in smaller:
        result.append(combo + [0])  
        result.append(combo + [1])  
    return result



values = [20, 5, 10, 40, 15, 25]   
weights = [1, 2, 3, 8, 7, 4]     
capacity = 10                      


combinations = get_combinations(len(values))


max_value = 0
best_selection = None

for selection in combinations:
    total_weight, total_value = calculate_total(weights, values, selection)
    if total_weight <= capacity and total_value > max_value:
        max_value = total_value
        best_selection = selection


print("Best item selection (0 = skip, 1 = take):", best_selection)
print("Maximum value:", max_value)
