import rand 

you = input("Pedra, Papel ou Tesoura: ")
pc = randint(1, 3)
if pc == 1 and you == 'papel':
	print('Voce escolheu Papel e o Pc escolheu Pedra. Voce Venceu.')
elif pc == 2 and you == 'pedra' :
	print('Voce escolheu pedra e o Pc escolheu papel. O PC  Venceu.')

if pc == 2 and you == 'papel':
	print('Voce escolheu Papel e o Pc escolheu Pedra. Voce Venceu.')
elif pc == 2 and you == 'pedra' :
	print('Voce escolheu pedra e o Pc escolheu papel. O PC  Venceu.')