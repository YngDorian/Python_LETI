import math
listing='1 1000 6 56'
L = listing.strip().split()
L_1 = [int(i) for i in L]
def find_solution(L_1):
    a = L_1[0]
    b = L_1[1]
    c = L_1[2]
    D = b * b - 4 * a * c
    if D < 0: 
        return None
    if D > 0: 
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return round(x1, 2), round(x2, 2)
D = find_solution(L_1)
print(D)