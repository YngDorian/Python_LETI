N = list(map(int, input().split(" ")))
def check_list(N):
    a = len(N)
    b = max(N) - min(N)
    return a,b
L = check_list(N)
print(L)