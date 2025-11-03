def combinations(data, r):
    
    if r == 0:
        return [[]]  
    if r > len(data):
        return []  
    
    
    first = data[0]
    
    
    rest = []
    for i in range(1, len(data)):
        rest.append(data[i])
    
    
    include_first = combinations(rest, r - 1)
    for combo in include_first:
        combo.insert(0, first)  

    
    exclude_first = combinations(rest, r)

    
    return include_first + exclude_first



nums = [1, 2, 3]
r = 2
result = combinations(nums, r)


for c in result:
    print(c)
