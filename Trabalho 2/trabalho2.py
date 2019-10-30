import random

def geraChave():
	return random.sample(range(0, 256), 255)

def cifraTexto(nomeArqTexto, chave):
	arq = open(nomeArqTexto,'r').read()
	textoCifrado = ""
	for simbolo in arq:
		if(0 <= ord(simbolo) < 256):
			textoCifrado = textoCifrado + chr(chave[ord(simbolo)])
	return textoCifrado

def decifraTexto(nomeArqTexto, chave):
	arq = open(nomeArqTexto,'r').read()
	textoDecifrado = ""
	for simbolo in arq:
		textoDecifrado = textoDecifrado + chr(chave.index(ord(simbolo)))
	return textoDecifrado

def ordenar(val): 
    return val[1]

def ataqueEscuro(nomeTC):
	frequenciasCifrado = []
	frequenciasDicionario = []
	for i in range(0, 256):
		frequenciasCifrado.append([i, 0])
		frequenciasDicionario.append([i, 0])

	arqTC = open(nomeTC,'r').read()
	for simbolo in arqTC:
		frequenciasCifrado[ord(simbolo)][1] += 1

	for i in range(0, 10):
		nomeDic = f"{i}.txt"
		arqDic = open(nomeDic,'r').read()
		for simbolo in arqDic:
			if(0 <= ord(simbolo) < 256):
				frequenciasDicionario[ord(simbolo)][1] += 1

	frequenciasCifrado.sort(key = ordenar)
	frequenciasDicionario.sort(key = ordenar)

	chave = []
	for i in range(0, 256):
		chave.append([frequenciasCifrado[i][0], frequenciasDicionario[i][0]])

	chave.sort(key = ordenar)

	chaveRet = []
	for i in range(0, 256):
		chaveRet.append(chave[i][0])

	# digrafosDic = []
	# frequenciaDigrafosDic = []
	# trigrafosDic = []
	# frequenciaTrigrafosDic = []

	# for i in range(0, 3):
	# 	print(i)
	# 	nomeDic = f"{i}.txt"
	# 	arqDic = open(nomeDic,'r').read()
	# 	digrafosDic.append(f"{arqDic[0]}{arqDic[1]}")
	# 	frequenciaDigrafosDic.append(int(1))
	# 	for j in range(2, len(arqDic)):
	# 		if f"{arqDic[j-1]}{arqDic[j]}" in digrafosDic:
	# 			frequenciaDigrafosDic[digrafosDic.index(f"{arqDic[j-1]}{arqDic[j]}")] += 1
	# 		else:
	# 			digrafosDic.append(f"{arqDic[j-1]}{arqDic[j]}")
	# 			frequenciaDigrafosDic.append(int(1))
	# 		if f"{arqDic[j-2]}{arqDic[j-1]}{arqDic[j]}" in trigrafosDic:
	# 			frequenciaTrigrafosDic[trigrafosDic.index(f"{arqDic[j-2]}{arqDic[j-1]}{arqDic[j]}")] += 1
	# 		else:
	# 			trigrafosDic.append(f"{arqDic[j-2]}{arqDic[j-1]}{arqDic[j]}")
	# 			frequenciaTrigrafosDic.append(int(1))

	# digrafosTextoCif = []
	# frequenciaDigrafosTextoCif = []
	# trigrafosTextoCif = []
	# frequenciaTrigrafosTextoCif = []

	# arqTC = open(nomeTC,'r').read()
	# digrafosTextoCif.append(f"{arqTC[0]}{arqTC[1]}")
	# frequenciaDigrafosTextoCif.append(int(1))
	# for j in range(2, len(arqTC)):
	# 	if f"{arqTC[j-1]}{arqTC[j]}" in digrafosTextoCif:
	# 		frequenciaDigrafosTextoCif[digrafosTextoCif.index(f"{arqTC[j-1]}{arqTC[j]}")] += 1
	# 	else:
	# 		digrafosTextoCif.append(f"{arqTC[j-1]}{arqTC[j]}")
	# 		frequenciaDigrafosTextoCif.append(int(1))
	# 	if f"{arqTC[j-2]}{arqTC[j-1]}{arqTC[j]}" in trigrafosTextoCif:
	# 		frequenciaTrigrafosTextoCif[trigrafosTextoCif.index(f"{arqTC[j-2]}{arqTC[j-1]}{arqTC[j]}")] += 1
	# 	else:
	# 		trigrafosTextoCif.append(f"{arqTC[j-2]}{arqTC[j-1]}{arqTC[j]}")
	# 		frequenciaTrigrafosTextoCif.append(int(1))

	return chaveRet

chave = geraChave()
open("outCifrado.txt","w").write(cifraTexto("in.txt", chave))
chaveDescoberta = ataqueEscuro("outCifrado.txt")
open("outDecifrado.txt","w").write(decifraTexto("outCifrado.txt", chaveDescoberta))