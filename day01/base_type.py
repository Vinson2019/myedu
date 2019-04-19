

def test1( ):
    print('zhws')

def test2():
    print('zhws')

def test3():
    print('zhws')

def cvc():
    asd  = 5
    print(asd)
    print(type(asd))

# if __name__ == '__main__':
    cvc()

def str_demo():
    # 声明astr变量 , 并赋值 '1'
    astr = '1'
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))
    # 不写
    print('--------------')
    astr = 1
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))


# def add_demo(a,b):
#     print(a+b)
# def float():
#     asd = 0.1
#     print(asd)
#     print(type(asd))

def add_demo(a,b):
     print(a+b)

def str_demo():
    a = 888
    b = '中国'
    c = 666
    print(str(a)+b+str(c))
    print('%s%s%s' %(a,b,c))
def str_d1emo():
     astr = 'ysl'
     print(astr.strip())
def jianfa_demo(a,b):
    d = a - b
    return d
# def aasjda():
#     aint = 15
#     print(type(aint))
#     print(type(str(aint)))
#     print(type(int(aint)))

def list_demo():
    alist = [7,8,33,2,1,3,4]
    # print(alist)
    # print(alist[0])
    # print(alist[1])
    # print(alist[-1])
    # print(alist[-2])
    alist[0] = 12
    print(alist)


# from day01 import base_type
if __name__ == '__main__':
    # aint = '123'
    # str_demo()
    # aint = 123
    # return a+b
    # aasjda()
    # add_demo('hello',str(aint))
    # str_d1emo()
    # print( jianfa_demo(5,2))
    # value = jianfa_demo(5,3)
    # print(value)
    # value1 = add_demo(2,3)
    # list_demo()
    list_demo()

