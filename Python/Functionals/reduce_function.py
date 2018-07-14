from fractions import Fraction
from functools import reduce

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

def product(fracs):
    t = reduce(Fraction.__mul__, fracs)
    return t.numerator, t.denominator