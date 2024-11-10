K = input().split(" ")
for item in range(len(K)) : K[item] = K[item][0]
def list_to_dict_with_index(K):
    dict_with_index = {value: ord(value) for index, value in enumerate(K)}
    return dict_with_index
result_dict = list_to_dict_with_index(K)
print(result_dict)