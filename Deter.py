import random

n=int(input('Please enter the number of gameplays:'))
r=[]

for i in range(n):
    r.append(random.randint(1,2))

p=r.count(1)

print('Outcomes',r)
print('Favourable outcomes 1=Heads',p)