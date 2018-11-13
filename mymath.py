def fact(n):
    return n * fact(n - 1) if n > 1 else 1

def inc(n, dn=1):
    return n + dn

def negabs(n):
    return n if n <= 0 else -n
