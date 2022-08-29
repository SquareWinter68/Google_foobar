"""def TEST_ALG(n):
    list_ = []
    for i in range(100):
        k = len(list(str(n)))
        x = int("".join(sorted(list(str(n)), reverse=True)))
        y =  int("".join(sorted(list(str(n)))))
        z = x-y
        print x,y,z
        if len(str(z)) < k:
            z = list(str(z))
            for i in range(k-len(z)):
                z = ["0"]+z
            z = "".join(z)

            list_.append(z)
        n = z
    return list_
#print TEST_ALG(580)"""


#print Convert_to_decimal(11112,3)

#print(convert_from_decimal(484,3))

#print convert_from_decimal(13767525,8)



def TEST_ALG_2(n,b):
    list_ = []
    ans =0
    for i in range(100):
        k = len(list(str(n)))
        x = int("".join(sorted(list(str(n)), reverse=True)))
        y = int("".join(sorted(list(str(n)))))
        z = convert_from_decimal(Convert_to_decimal(x,b)-Convert_to_decimal(y,b),b)
        if len(str(z)) < k:
            z = list(str(z))
            for i in range(k-len(z)):
                z = ["0"]+z
            z = "".join(z)
        list_.append(z)
        n=z
    return Counter(list_)
