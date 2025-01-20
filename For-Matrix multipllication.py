r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[9,8,7]
s2=[6,5,4]
s3=[3,2,1]

m=[]
m.append(r1)
m.append(r2)
m.append(r3)

n=[]
n.append(s1)
n.append(s2)
n.append(s3)


dim=3
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+m[i][k]*n[k][j]

#print('The matrix multiplication of m and n is',c)


