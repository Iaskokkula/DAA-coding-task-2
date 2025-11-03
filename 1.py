def permutation(data):

    if len(data) == 1:
        return [data]

    result = [] 

    
    for i in range(len(data)):
        
        current = data[i]

        remaining = []
        for j in range(len(data)):
            if j != i:
                remaining.append(data[j])

        
        smaller_perms = permutation(remaining)

        
        for perm in smaller_perms:
            result.append([current] + perm)

    return result



nums = [1, 2, 3]
all_perms = permutation(nums)

for p in all_perms:
    print(p)
