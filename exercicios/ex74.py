
import random
i = 0
tup = ();
while len(tup) < 5 :
    num = random.randint(1, 100)
    tup += (num,)
print(sorted(tup))
print('Maior->', max(tup))
print('Menor->', min(tup))