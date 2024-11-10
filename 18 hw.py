k = input().split(" ")
for str in k:
    if str.isalpha():
        k.append(str)
for str in k:
    if str.isdigit():
        k.append(str) 
print(k)