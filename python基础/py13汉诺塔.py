def hano(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return None
    hano(n-1, a, c, b)
    print(a, "-->", c)
    hano(n-1, b, a, c)

a, b, c = 'A', 'B', 'C'


n = 4
hano(n, a, b, c)