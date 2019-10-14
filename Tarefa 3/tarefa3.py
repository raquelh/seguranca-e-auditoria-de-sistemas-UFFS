def exp(a, e, m):
    if e == 0:
        return 1
    if e % 2 == 1:
        return ((exp(a, e-1, m) * a) % m)
    aux = exp(a, e/2, m)
    return ((aux * aux) % m)

def main():
    for a in [1, 2, 3, 4, 5]:
        for e in [3, 5, 6]:
             print(f"{a}^{e-1}(mod {e}) = {exp(a, (e-1), e)}")

main()

