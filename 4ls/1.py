# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def number_Pi():
    n = 500
    Pi = 3
    z = 1
    result = []
    for i in range(2, n+1, 2):
        Pi = Pi + (4*z)/(i*(i+1)*(i+2))
        z *= -1
    for i in range(1, 11):
        d = 10**-i
        res = int(Pi/d)*d
        result.append(res)
    return result


p = number_Pi()
print(p)
