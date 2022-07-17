def find_sum(n):
    s = 0
    for i in range(1,n+1):
        s+=i
    return s

def find_sum_rec(n):
    if n == 1:      # Base Condition
        return 1
    return n+find_sum_rec(n-1)

def fibo(n):
    v1 = 0
    v2 = 1
    cnt = 0
    while cnt<n:
        print(v1)
        nth = v1+v2
        v1 = v2
        v2 = nth
        cnt+=1
    return v1

def fibo_rec(n):
    if n == 0 or n == 1:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)


if __name__ == '__main__':
    print("find_sum:",find_sum(5))
    print("find_sum_rec",find_sum_rec(5))
    print("fibo",fibo(10))
    print("fibo_rec", fibo_rec(10))
