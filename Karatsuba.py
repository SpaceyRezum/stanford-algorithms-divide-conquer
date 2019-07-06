import math


def karatsuba(x, y):
    print('x: ', x)
    print('y: ', y)
    if (x < 10) or (y < 10):
        return x * y

    n = min(len(str(x)), len(str(y)))
    n2 = n // 2

    high1 = x // 10**n2
    low1 = x % 10**n2
    high2 = y // 10**n2
    low2 = y % 10**n2

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return z2 * 10**(2*n2) + ((z1 - z2 - z0) * 10**n2) + z0


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))