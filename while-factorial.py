n=int(input('Enter the number:'))

fact=1

if n>0:
    while (n>0):
        fact=fact*n
        n=n-1

    print(fact)
else:
    print('Invalid number')