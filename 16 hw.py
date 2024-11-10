import math
listing='2.0 4.0 6.0 56.0'
L = listing.strip().split()
L_1 = [float(i) for i in L]
def radians(L_1):
    for item in range(len(L_1)) : L_1[item] = round(L_1[item] * math.pi / 180, 2)
    return L_1
D = radians(L_1)
print(D)
    