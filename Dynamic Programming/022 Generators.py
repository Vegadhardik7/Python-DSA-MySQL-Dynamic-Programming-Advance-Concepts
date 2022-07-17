'''
Generators which give us iterators

- We got iterator without using iter and next function

return terminates the function but yield doesnot

Q.) Why we use Generators?

- Let's say we want to fetch 1000 records and work with one record at a time that time we use
  Generators.
'''

def topten():
    yield 1
    yield 2
    yield 3
    yield 4

val = topten()

print(val.__next__())
print(val.__next__())

for i in val:
    print(i)


def top10squares():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

print('-'*10)
val2 = top10squares()

for i in val2:
    print(i)