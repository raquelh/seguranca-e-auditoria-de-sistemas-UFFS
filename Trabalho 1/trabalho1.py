def gcd(a, m):
    if a == 0:
        return(m, 0, 1)
    a1, y, x = gcd(m % a, a)
    return(a1, x - (m // a) * y, y)

def inversoMultiplicativo(a, m):
    a1, x, y = gcd(a, m)
    if a1 != 1:
        return None
    return x % m

def exp(a, e, m):
    if e == 0:
        return 1
    if e % 2 == 1:
        return ((exp(a, e-1, m) * a) % m)
    aux = exp(a, e/2, m)
    return ((aux * aux) % m)

def totiente(n):
	for p in range(3, n, 2):
		if(n%p == 0):
			return (p-1)*((n/p)-1)
	return 0

def main():
	leituraTeclado = input().split(" ", 3)
	n = int(leituraTeclado[0])
	e = int(leituraTeclado[1])
	c = int(leituraTeclado[2])
	d = inversoMultiplicativo(e, totiente(n))
	print(exp(c, d, n))

main()