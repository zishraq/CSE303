from math import pow


def compound_interest_2019_2_60_022(P: float, r: float, t: float) -> float:
    return P * (pow((1 + (r/100)), t))


P = float(input('Initial principal balance, P = '))
r = float(input('Interest rate, r = '))
t = float(input('Number of years, t = '))

print('Compound interest, CI = ', compound_interest_2019_2_60_022(P, r, t))
