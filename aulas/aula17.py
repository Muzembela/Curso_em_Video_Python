
"""num =[2, 5, 9, 1]

num.append(7)
num.insert(2, 2)
num.remove(2)
print(num)"""

vals = []
vals.append(5)
vals.append(9)
vals.append(4)

for cont in range(0, 5) :
	vals.append(int(input('Digite um valor: ')))
for c, v in enumerate(vals) :
	print(f'na posicao {c} encontrei o valor {v}...', end="")