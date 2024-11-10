listing='2 4 6 56'
L =listing.strip().split()
L_1 = [int(i) for i in L]
def my_det(L_1):
    a = L_1[0]
    b = L_1[1]
    c = L_1[2]
    D = b*b - 4 * a * c
    return D
T = my_det(L_1)
print(T)