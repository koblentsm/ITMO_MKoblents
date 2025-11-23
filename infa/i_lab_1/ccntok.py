def from10toN(x, n):
    s = ''
    if n < 10:
        while x > 0:
            s += str(x % n)
            x = x//n
    else:
        arr = [' ']*n
        for i in range(10):
            arr[i] = str(i)
        for i in range(10, n):
            arr[i] = chr(55+i)
        while x > 0:
            ch = x % n
            s += arr[ch]
            x = x//n
    return s[::-1]


def fromNto10(x, n):
    X = str(x)[::-1]
    res = 0
    if 0 < n < 10:
        for i in range(len(X)):
            res += int(X[i])*(n**i)
    else:
        for i in range(len(X)):
            if X[i].isalpha():
                res += (ord(X[i])-55)*(n**i)
            else:
                res += int(X[i])*(n**i)

    return res


def from10toFib(x):
    first = 1
    second = 1
    arr = [1, 1]
    third = 2
    while third <= x:
        arr.append(third)
        first = second
        second = third
        third = first+second
    arr = arr[::-1]
    s = ''
    print(arr)
    for i in range(len(arr)-1):
        s += str(x//arr[i])
        x = x % arr[i]
    return s


print(fromNto10(83, 16))
print(from10toN(660, 2))
