
n = int(input('Digite n: '))
i = n
fat = 1
while i > 1:
    fat *= i
    i -= 1
print('Fatorial de {} e {}'.format(n, fat))