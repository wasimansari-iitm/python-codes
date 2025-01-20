name=input('Enter any word to reverse:')

d=len(name)

print('Length of the word is',d)

for i in range(len(name)):
    print(name[d-i-1],end='')
