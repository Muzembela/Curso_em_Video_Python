
vals = []

while True:
	vals.append(int(input('Digite um numero: ')))
	br = input('Quer continuar? [s or n] : ')
	if br == 'n' :
		break
print('Nums de nums digitados -> {}. '.format(len(vals)))
print('Lista ordenada->', sorted(vals))

if 5 in vals :
	posicao = vals.index(5)
	print('O numero 5 foi digitado, ele encontra-se na posicao {} da lista' .format(posicao))
else :
	print('O numero 5 nao foi digitado, ele nao se encontra na lista.')