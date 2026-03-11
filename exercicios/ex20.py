import random
nome1 = str(input('Digite o 1 nome: '))
nome2 = str(input('Digite o 2 nome: '))
nome3 = str(input('Digite o 3 nome: '))
nome4 = str(input('Digite o 4 nome: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('Ordem de apresentacao da tarefa.',lista)