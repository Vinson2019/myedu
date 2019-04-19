adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
cdict = {5:"yansl","password":[2,5]}
def dict_sel():
    print(adict["username"])
    print(bdict[5])

def dict_del():
    adict.pop('username')
    bdict.pop('password')
    print(adict,bdict,cdict)

if __name__ == '__main__':
  # dict_sel()
  dict_del()