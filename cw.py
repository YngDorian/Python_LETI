d = {1:"str1", 2:"str2", 3:"str3"}
inp_str = "k m"
def check_dict(d, inp_str):
    key = len(inp_str)
    if key in d:
        return d[key]
    else:
        d[key] = inp_str
        return d
k = check_dict(d, inp_str)
print(k)