n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2 :
	print('O primeiro numero ({}) e maior'.format(n1))
elif n1 < n2 :
	print('O segundo numero ({}) e maior'.format(n2))
else :
	print('Os numeros sao iguais.')