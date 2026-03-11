import random


my = int (input('Digite o numero: '))
num = random.randint(1, 10)
pal = 0
while num != my :
    print('Voce errou o numero era', num)
    pal = pal+1
    num = random.randint(1, 10)
print('Voce acertou em {} tentativas'.format(pal))