import random

num = random.randint(1, 5)
my = int(input("Digite o seu numero: "))
if my == num :
	print("O seu numero e ",my, "e do computador e ", num, "parabens, voce acertou.")
else :
	print("O seu numero e ",my, "e do computador e " ,num, "voce nao acertou.")
