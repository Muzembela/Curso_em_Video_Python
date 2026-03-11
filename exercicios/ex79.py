
vals = []

while True:
    num = int(input("Digite um número: "))
    if num in vals:
        print("Esse número já está na lista, tente outro.")
    else:
        vals.append(num)
    br = input("Quer continuar? [s/n]: ")
    if br.lower() == 'n':
        break
print("Lista ordenada:", sorted(vals))

