def fact(n):
    return n * fact(n - 1) if n > 1 else 1

def inc(n, dn=1):
    return n + dn
