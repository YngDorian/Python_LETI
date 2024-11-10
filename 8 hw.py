N = list(map(int, input().strip().split()))
K = [item for item in N if item % 2 == 0]
print(K)