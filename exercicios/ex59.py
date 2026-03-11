
res = 0
a = 0
n = int(input("Digite um número: "))
while n != 5 :
    n1 = int(input('Digite n1: '))
    n2 = int(input('Digite n2: '))
    print("\n1->Somar 2->Multiplicar 4->Novos numeros 5->Sair\n")
    a = int(input('Digite  a opcao: '))
    if a == 1 :
        res = n1 + n2
    if a == 2 :
        res = n1 * n2
    print('Resultado da opcao desjada {}'.format(res))
print("Finished")
    
