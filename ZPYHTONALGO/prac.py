# def fibo(n):
#     cnt1 = 0
#     cnt2 = 1
#     val = 0
#     if n<=0:
#         print("Invalid")
#     for i in range(n):
#         val = cnt1+cnt2
#         print(cnt1)
#         cnt1 = cnt2
#         cnt2 = val
# n = 10
# x = fibo(n)
# print(x)
# ---------------------------------------------------------

# def factorial(data):
#     cnt=1
#     for i in range(1,data+1):
#         cnt*=i
#         print(cnt)
# x = factorial(5)
# print(x)

# ------------------------------------------------------------------------

# def findrepeatnuminlist(data):
#     val = []
#     d = len(data)
#     for i in range(d):
#         key =i+1
#         for j in range(key,d):
#             if data[i]== data[j] not in val:
#                 val.append(data[i])
#     return val
#
# lst = [2,3,1,3,3,0,1]
# x = findrepeatnuminlist(lst)
# print(x)
# ------------------------------------------------------------------------------


# def largestNumInList(data):
#     largest = 0
#     for x in range(0, len(data)):
#         if (data[x]>largest):
#             largest = data[x]
#     return largest
#
# lst = [1,2,3,4,5,155,4,3,200]
# x = largestNumInList(lst)
# print(x)
#----------------------------------------------------------------------

# def primeornot(data):
#     if data>1:
#         for i in range(2,data//2):
#             if (data%i) == 0:
#                 print(data,"is Not Prime")
#                 break
#         else:
#             print(data,"is Prime")
#     else:
#         print(data,"is Not Prime")
# x = primeornot(17)
# print(x)
# -------------------------------------------------------------------------

def sumOfEven(num):
    s = 0
    for i in range(num):
        if i%2==0:
            print(f"{i}")
            s+=i
    print(s)
#

x = sumOfEven(10)
print(x)

















