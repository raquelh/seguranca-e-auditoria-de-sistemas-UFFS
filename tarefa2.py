def gcd(a, m):
    if a == 0:
        return(m, 0, 1)
    a1, y, x = gcd(m%a, a)
    return(a1, x-(m//a)*y, y)

def inversoMultiplicativo(a, m):
    a1, x, y = gcd(a, m)
    if a1 != 1:
        return 0
    return x%m

def main():
    print("Exercicio 1")
    print("Calcular o inverso multiplicativo de todos os numeros modulo 21.")
    print("Numero - Inverso Multiplicativo")
    for i in range(1, 21):
        print(i, "-", inversoMultiplicativo(i, 21))
    print("\nExercicio 2")
    print("Calcular o inverso multiplicativo de 45 modulo 94.")
    print("Inverso multiplicativo de 45 modulo 94 =", inversoMultiplicativo(45, 94), "\n")

main()

# Referência:
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
