
n = int(input('Digite n: '))
eh_primo = True

for c in range(2, n):
    if n % c == 0:
        eh_primo = False
        break

if eh_primo:
    print('Is prime')
else:
    print('Not is prime')
