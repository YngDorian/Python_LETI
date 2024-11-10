K = input().strip().split('\t')
print(K.count(max(set(K), key=K.count)))