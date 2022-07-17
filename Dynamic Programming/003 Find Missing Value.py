def Miss(data):
    data = sorted(data)
    n = data[-1]
    val1 = (n*(n+1)/2) # print(5*(5+1)/2) = 15
    val2 = sum(data)   # print(1+3+4+5)   = 13
    print(f"Missing value present in the list is ",val1-val2)
lst = [1,3,4,5]
x = Miss(lst)
print(x)