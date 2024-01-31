def myfunc(n):
    return abs(n-50)
x = [1, 2, 56, 100, 84]
x.sort(key = myfunc)
print(x)