res=[]
for i in range (10000, 100000):
    flag=True
    # print(len(str(i)))
    for j in range (1, len(str(i))):
        # print(int('i'[j]))
        if int(str(i)[j])<=int(str(i)[j-1]):
            flag=False
    if flag==True:
        res.append(i)
print(res, len(res))
            
