n,k=input().split(" ")
lista=[]
c=0

for i in range(int(n)):
    a, p = input().split(" ")
    lista.append([int(a) ,int(p) ])

lista=sorted( lista, key=lambda x: (x[0]), reverse=True)
for j in lista:
    if j == lista[int(k)-1]:
        c+=1
print(c)