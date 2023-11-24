import math

def fx(x, y, lm, a):
    x2 = lm*x*math.exp(-1*a*y)
    return x2

def fy(x, y, c, a):
    y2 = c*x*(1-math.exp(-1*a*y))
    return y2

def simulation(x1, y1, lm, c, a, n):
    X = [x1]
    Y = [y1]
    for i in range(n):
        x2 = fx(x1, y1, lm, a)
        y2 = fy(x1, y1, c, a)
        X.append(x2)
        Y.append(y2)
        x1 = x2
        y1 = y2

    return X, Y 


def gx(x, y, lm, a, b):
    x2 = lm*x*((1+((a*y)/b))**(-1*b))
    return x2

def gy(x, y, a, b, c):
    y2 = c*x*(1-(1+((a*y)/b))**(-1*b))
    return y2

def simulation2(x1, y1, lm, a, b, c, n):
    X = [x1]
    Y = [y1]
    for i in range(n):
        x2 = gx(x1, y1, lm, a, b)
        y2 = gy(x1, y1, a, b, c)
        X.append(x2)
        Y.append(y2)
        x1 = x2
        y1 = y2

    return X, Y 