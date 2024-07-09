n=input("Digite um número: ")
f=len(n)-1
c=0
lista=[]
R1=""
while f>=0:
	lista.append(int(n[f])*(10**c))
	lista.append("+")
	f=f-1
	c=c+1
f=len(lista)-1
lista[f]=""
lista=lista[::-1]
lista.append("=")
lista.append(n)
for k in lista:
	R1=R1+str(k)
print(R1)
