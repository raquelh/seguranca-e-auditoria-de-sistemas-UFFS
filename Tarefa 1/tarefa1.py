#Calcula o maior divisor comum
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#Calcula o mínimo múltiplo comum
def lcm(a, b):
	return ((a / gcd(a, b)) * b)

def main():
	qntBuracos = int(input())
	buracos = []
	leituraTeclado = input().split(" ", qntBuracos)
	for i in range(0, qntBuracos):
		buracos.append(int(leituraTeclado[i]))
	resposta = 1
	for i in range(0, qntBuracos):	#varre o vetor de túneis
		tempo = 1;
		#buraco atual
		buraco = buracos[i]
		while (buraco-1 != i):			#verrifica se o burraco atual é diferente do burraco pertencente ao diglett i, se não for:
			tempo = tempo + 1			#adiciona 1 ao tempo
			buraco = buracos[buraco-1]	#o diglett vai para o próximo burraco
		resposta = lcm(resposta, tempo) #calcula o mínimo múltiplo comum entre os tempos anteriores e o tempo atual
	print(int(resposta))

main()
