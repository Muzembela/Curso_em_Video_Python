num = int(input('Digite o numero: '))
escolha = int(input('Digite a sua escolha entre  1->binario , 2->octal e 3->hexa: '))

if escolha == 1 :
	print('Binario', bin(num))
elif escolha == 2 :
	print('Octal', oct(num))
elif escolha == 3 :
	print('Hexa', hex(num))
