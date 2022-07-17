list=[4,5,1,2,3,8,9]
maxval=list[0]
for i in range(0,len(list),1):
    if maxval<list[i]:
        maxval=list[i]

print(maxval)
