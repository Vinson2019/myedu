def lest_name(a):
    print(a[2])
    print(a[1:3])
def lest_qname():
    alist = [1,'世','界','你','好']
    # print(alist[0:6])
    alist[0] = 5
    alist.pop()
    print(alist)

def alist_add():
    blist =[123,56464,121231,45465,5434]
    blist.append('china')
    print(blist)
    clist =[78943,1313,54654]
    blist.append(clist)
    print(blist)


if __name__ == '__main__':
   # alist = ['china','日本',825,961,]
   lest_name(alist)
   # lest_qname()
   #  alist_add()
   # lest_qname()