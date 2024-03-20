def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_fraction(num, den):
    divisor = gcd(num, den)
    return num // divisor, den // divisor

def add_fractions(a_num, a_den, b_num, b_den):
    common_denominator = a_den * b_den
    new_a_num = a_num * b_den
    new_b_num = b_num * a_den
    result_num = new_a_num + new_b_num
    return simplify_fraction(result_num, common_denominator)

a_num, a_den = map(int, input().split())
b_num, b_den = map(int, input().split())

result_num, result_den = add_fractions(a_num, a_den, b_num, b_den)

print(result_num, result_den)