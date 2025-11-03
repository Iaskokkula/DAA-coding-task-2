


r1, c1 = map(int, input("Enter rows and columns of Matrix 1: ").split())
print("Enter elements of Matrix 1 row-wise:")
A = [list(map(int, input().split())) for _ in range(r1)]


r2, c2 = map(int, input("Enter rows and columns of Matrix 2: ").split())
print("Enter elements of Matrix 2 row-wise:")
B = [list(map(int, input().split())) for _ in range(r2)]

if c1 != r2:
    print("Matrix multiplication not possible!")
else:
   
    result = [[sum(A[i][k] * B[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
    
   
    print("Resultant Matrix:")
    for row in result:
        print(*row)
