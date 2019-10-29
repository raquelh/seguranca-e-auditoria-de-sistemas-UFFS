from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def geraChaves():
	chaves = RSA.generate(1024, Random.new().read)
	return chaves

def assinarArquivo(arq, chaves):
	hash = SHA256.new(arq).digest()
	return chaves.sign(hash, '')

def verificarAssinatura(arq, assinatura, chavePublica):
	hash = SHA256.new(arq).digest()
	if(chavePublica.verify(hash, assinatura)):
		print("O arquivo é autêntico\n")
		return True
	print("O arquivo não é autêntico\n")
	return False

def main():
	print()
	arqParaAssinar = open("textoOriginal.txt", "rb").read()
	chaves = geraChaves();
	assinatura = assinarArquivo(arqParaAssinar, chaves)
	arqAssinatura = open("mensagem.txt", "wb")
	arqAssinatura.write(assinatura[0].to_bytes(128, 'little'))
	arqAssinatura.write(chaves.exportKey("DER"))
	arqAssinatura.close()
	print("Arquivo assinado\n")

	print("Verificando assinatura com arquivo não alterado:\n\t", end = "")
	arqParaVerificar = open("textoOriginal.txt", "rb").read()
	arqAssinatura = open("mensagem.txt", "rb")
	assinatura = arqAssinatura.read(128)
	assinatura = [int.from_bytes(assinatura, byteorder='little')]
	chavePublica = arqAssinatura.read()
	arqAssinatura.close()
	verificarAssinatura(arqParaVerificar, assinatura, RSA.importKey(chavePublica))
	
	print("Verificando assinatura com arquivo alterado:\n\t", end = "")
	arqParaVerificar = open("textoAlterado.txt", "rb").read()
	verificarAssinatura(arqParaVerificar, assinatura, RSA.importKey(chavePublica))

main()