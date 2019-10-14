def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def lcm(a, b):
	return ((a / gcd(a, b)) * b)

def sum(n, p):
    return n * (p // n) * ((p // n) + 1) // 2

def euler(a,b,n):
    return int(sum(a, n) + sum(b, n) - sum(lcm(a,b), n))

print(f"A soma de todos os multiplos de 3 ou 5 menores que 1000 eh {euler(3, 5, 999)}")
print(f"A soma de todos os multiplos de 3 ou 5 menores que 1000000 eh {euler(3, 5, 999999)}")

# Referência
# https://www.mathblog.dk/project-euler-problem-1/
