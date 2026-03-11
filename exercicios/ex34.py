sal = float(input('Digite o seu salario: '))

if sal < 1250 :
	n_sal = (sal)*0.1 + sal
else :
	n_sal = (sal)*1.5 + sal
print('Caro funcionario o seu novo salario e {} kzs'.format(n_sal))