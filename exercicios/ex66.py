
n = int(input('Digite n: '))
soma = 0
while n != 999 :
    n = int(input('Digite n: '))
    if n == 999 :
        print('Programa interropido.')
        break
    soma = soma + n
print("A soma e {}".format(soma))