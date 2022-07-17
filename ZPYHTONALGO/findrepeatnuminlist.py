def Repeat(x):
    size=len(x)
    rep=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[i]==x[j] and x[i] not in rep:
                rep.append(x[i])
    return rep
list=[10,20,50,40,10,50,60,80]
print(Repeat(list))
