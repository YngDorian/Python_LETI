d = {1:"str1", 2:"str2", 3:"str3"}
inp_str = "k m"
def check_dict(d,inp_str):  
    for i in d:
        if d.index() == len(inp_str):
          return d[i]
        elif d.index() != len(inp_str):
          return {len(inp_str): inp_str}
k = check_dict(d,inp_str)
print(k)