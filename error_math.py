def add(a,b):
    c = [None,None]
    c[0] = a[0] + b[0]
    c[1] = ( (a[1]**2) + (b[1]**2) ) ** 0.5
    return c

def sub(a,b):
    c = [None,None]
    c[0] = a[0] - b[0]
    c[1] = ( (a[1]**2) + (b[1]**2) ) ** 0.5
    return c

def mul(a,b):
    fa = a[1] / a[0]
    fb = b[1] / b[0]
    fc = ( (fa**2) + (fb**2) ) ** 0.5
    c = [None,None]
    c[0] = a[0] * b[0]
    c[1] = c[0] * fc
    return c

def div(a,b):
    fa = a[1] / a[0]
    fb = b[1] / b[0]
    fc = ( (fa**2) + (fb**2) ) ** 0.5
    c = [None,None]
    c[0] = a[0] / b[0]
    c[1] = c[0] * fc
    return c

def pow(a,p):
    fa = a[1] / a[0]
    fc = fa * abs(p)
    c = [None,None]
    c[0] = a[0] ** p
    c[1] = c[0] * fc
    return c
