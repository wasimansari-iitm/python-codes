num=(int(input('Enter a number:'))) # example 123

absnum=abs(num) #converts -ve num to +ve

rev=absnum%10 # gives 3

absnum=absnum//10 #gives 12

while (absnum>0):
    r=absnum%10 #gives 2
    absnum=absnum//10 #gives 1
    rev=rev*10+r # gives(30+2)
    #Hence loop repeats from here

if (num>=0):
    print(rev) #print reverse
else:
    print(rev-2*rev) #print -ve reverse

if num==rev or num==(rev-2*rev): #checks num=reverse
    print('Palindrome')
else:
    print('Not Palindrome')