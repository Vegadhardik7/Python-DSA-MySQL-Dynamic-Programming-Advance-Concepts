def gcd(m,n):
    fm=[]
    for i in range(1,1+m):
        if(m%i)==0:
            fm.append(i)
    fn=[]
    for j in range(1,1+n):
        if(n%j)==0:
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[-1])
    
