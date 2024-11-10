K = input().split(" ")
for item in range(len(K)) : K[item] = K[item][0]
def list_to_dict_with_index(K):
    dict_with_index = {index: ord(value) for index, value in enumerate(K)}
    return dict_with_index
sample_list = K
result_dict = list_to_dict_with_index(sample_list)
print(result_dict)