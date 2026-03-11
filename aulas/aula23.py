
try:
	a = int(input('Digite a: '))
	b = int(input('Digite b: '))

	r = a / b
except Exception as erro :
	print("Infelizmente temos um problema, foi", erro.__class_)
else :
	print('Valor ->', r)
finally:
	print('Volte sempre.')