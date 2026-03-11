
vals = []
for c in range(0, 5) :
	vals.append(int(input('Digite um numero: ')))
	maior = (max(vals))
	menor= (min(vals))
	i_maior = vals.index(maior)
	menor = (min(vals))
	i_menor = vals.index(menor)
print('Maior valor -> {} indice->{}... Menor valor-> {} ->indice {}.' .format(maior, i_maior, min(vals), i_menor))
print(sorted(vals))