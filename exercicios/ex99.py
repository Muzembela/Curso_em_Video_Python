
def maior( *nums) :
	val = max(nums)
	print('O maior valor e {}'.format(val))

nums = 0
vals = []
while True:
	nums = int(input('Digite nums: '))
	vals.append(nums)
	br = input('Quer Continuar [s or n]: ')
	if br == 'n':
		break
maior(*vals)