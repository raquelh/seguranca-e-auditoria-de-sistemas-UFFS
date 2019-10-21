import copy

class Arvore :
	def __init__(self, frequencia, letra=None, pai=None, esquerda=None, direita=None) :
		self.frequencia = frequencia
		self.letra = letra
		self.pai = pai
		self.esquerda  = esquerda
		self.direita = direita

	def __str__(self) :
		if self.letra != '\n':
			return f"{self.frequencia} {self.letra}"
		else:
			return f"{self.frequencia} enter"

def ordenar(val): 
	return val[1]

def constroiArvore(texto):
	frequencias = []
	for s in texto:
		i = 0
		while(i < len(frequencias) and frequencias[i][0] != s):
			i += 1
		if(i < len(frequencias)):
			frequencias[i][1] += 1
		else:
			frequencias.append([s, 1])
	frequencias.sort(key = ordenar)
	
	vetorFolhas = []
	for i in frequencias:
		vetorFolhas.append(Arvore(i[1], i[0]))
	vetorArvore = copy.copy(vetorFolhas)
	
	while(1):
		freq = vetorArvore[0].frequencia + vetorArvore[1].frequencia
		ind1, ind2 = 0, 1
		for i in range(0, len(vetorArvore)-1):
			for j in range(i+1, len(vetorArvore)):
				if((vetorArvore[i].frequencia + vetorArvore[j].frequencia) < freq):
					freq = vetorArvore[i].frequencia + vetorArvore[j].frequencia
					ind1, ind2 = i, j
		vetorArvore[ind1] = Arvore(vetorArvore[ind1].frequencia + vetorArvore[ind2].frequencia,
			esquerda = vetorArvore[ind1], direita = vetorArvore[ind2])
		vetorArvore[ind1].esquerda.pai = vetorArvore[ind1]
		vetorArvore[ind1].direita.pai = vetorArvore[ind1]
		vetorArvore.pop(ind2)
		if(len(vetorArvore) == 1):
			return vetorArvore[0], vetorFolhas

def salvaArvore(arvore, nivel, arq):
	arq.write(f"{arvore} {nivel}\n")
	if arvore.esquerda:
		salvaArvore(arvore.esquerda, nivel+1, arq)
	if arvore.direita:
		salvaArvore(arvore.direita, nivel+1, arq)

from array import array

def compactaTexto(caminhoTextoClaro, caminhoArvore, caminhoTextoCompactado):
	arq = open(caminhoTextoClaro, "r")
	texto = arq.read()
	arq.close()

	arvore, folhas = constroiArvore(texto)
	textoCompac = ""
	for s in texto:
		caminhoSimbolo = []
		for j in folhas:
			if(j.letra == s):
				no = j
				while(no.pai != None):
					if no.pai.esquerda == no:
						caminhoSimbolo.append(0)
					else:
						caminhoSimbolo.append(1)
					no = no.pai
				break
		while caminhoSimbolo:
			textoCompac += str((caminhoSimbolo.pop()))
	
	#Salva a árvore em um arquivo
	arq = open(caminhoArvore, "w")
	salvaArvore(arvore, 0, arq)
	arq.close()

	#Salva o texto compactado em outro arquivo
	bin_array = array("B")
	while len(textoCompac) % 8 != 0:
		textoCompac += '0'
	for i in range(0, len(textoCompac), 8):
		byte = textoCompac[i:i+8]
		bin_array.append(int(byte, 2))

	with open(caminhoTextoCompactado, "wb") as arq:
		arq.write(bytes(bin_array))
	arq.close()

	return textoCompac, arvore

def montaArvore(caminhoArvore):
	arqArvore = open(caminhoArvore, "r").readlines()
	noAtual = None
	arvore = None
	for i in arqArvore:
		split = i[0:len(i)-1].split(" ")
		if len(split) == 3:
			frequencia, letra, nivel = split
			if letra == 'enter':
				letra = '\n'
		else:
			frequencia = split[0]
			letra = ' '
			nivel = split[1]
		if letra != "None":
			novoNo = Arvore(frequencia = int(frequencia), letra = letra, pai = noAtual)
			if(noAtual.esquerda):
				noAtual.direita = novoNo
				while(noAtual != arvore and noAtual.direita):
					noAtual = noAtual.pai
			else:
				noAtual.esquerda = novoNo
		else:
			novoNo = Arvore(frequencia = int(frequencia), pai = noAtual)
			if(noAtual and noAtual.esquerda):
				noAtual.direita = novoNo
			elif noAtual:
				noAtual.esquerda = novoNo
			noAtual = novoNo
		if(not arvore):
			arvore = novoNo
	return arvore

def descompactaTexto(caminhoTextoCompac, caminhoArquivoArvore, caminhoTextoDescompactado):
	arvore = montaArvore(caminhoArquivoArvore)
	
	arq = open(caminhoTextoCompac, "rb")
	textoCompac = arq.read()
	arq.close()

	bitsTexto = ""
	for i in textoCompac:
		byte = (bin(i)[2:])
		while len(byte) < 8:
			byte = '0' + byte
		bitsTexto += byte

	textoDescomp = []
	noAtual = arvore
	for i in bitsTexto:
		if i == '1':
			noAtual = noAtual.direita
		else:
			noAtual = noAtual.esquerda
		if(noAtual.letra):
			textoDescomp.append(noAtual.letra)
			noAtual = arvore

	arq = open(caminhoTextoDescompactado, "w")
	for i in textoDescomp:
		arq.write(i)
	arq.close()

	return textoDescomp

def main():
	compactaTexto("texto.txt", "arvore", "textoCompactado")
	descompactaTexto("textoCompactado", "arvore", "textoDescomp.txt")

main()