
def sortear(*nums):
	print('Numeros ordenados ->', sorted(nums))

def pares(*nums) :
	par = 0
	for n in nums:
		if n % 2 == 0 :
			par += n
	print('Soma de nums pares -> {}' .format(par))

#programa
vals = []
for c in range(0, 5) :
	nums = int(input('Digite o numero: '))
	vals.append(nums)
sortear(*vals)
pares(*vals)

