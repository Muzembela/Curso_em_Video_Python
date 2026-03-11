
vals = []
l1 = []
l2 = []
while True:
	num = int(input('Digite um numero: '))
	vals.append(num);

	if num % 2 == 0 :
		l1.append(num)
	else :
		l2.append(num)
	br = input('Quer Continuar [s or n] ? : ')
	if br == 'n' :
		break

print('Lista 1-> original', vals)
print('Lista 2-> pares', l1)
print('Lista 3-> impares', l2)
