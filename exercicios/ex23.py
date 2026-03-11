n = int(input("Dgite um numero: "))
milhar = n // 1000
centena = (n%1000)// 100
dezena = (n%100)// 10
unidade = (n%10)

print("Unidade->", unidade)
print("Dezena->", dezena)
print("Centena->", centena)
print("Milhar->", milhar)
