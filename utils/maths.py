from math import gcd


def least_common_multiple(numbers: list) -> int:
    lcm = 1
    for i in numbers:
        i = int(i)
        lcm = lcm * i // gcd(lcm, i)
    return lcm
