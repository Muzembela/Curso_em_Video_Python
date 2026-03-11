vel = int(input('Digite a velocidade atual da sua viatura: '))

if vel > 80 :
	multa = vel - 80
	print('A velocidade da viatura excedeu o limite, a sua multa e de {}R$'.format(multa))
else :
	print('A sua velocidade e otima, continue dirigindo assim.')