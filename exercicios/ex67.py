
i = 1 
while True:
    n = int(input('Digite n: '))
    if n <= 0 :
      break
    else :
        for i in range(0, 10) :
            tab = n*i
            print('{} * {} = {}'.format(n, i, tab))   