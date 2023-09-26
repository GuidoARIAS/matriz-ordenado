import random
fila=int(3)
columna=int(3)
matriz=[]
for i in range(fila):
    matriz.append([])
    for j in range(columna):
        matriz[i].append(random.randint(0,9))
for i in matriz:  
    print(i,end = "\n")
print("*********")
k=0
l=0
for m in range(9):
    for i in range(3):
        for j in range(3):
            if (matriz[k][l]<matriz[i][j]):
                a= matriz[i][j]
                matriz[i][j]=matriz[k][l]
                matriz[k][l]=a
    l=l+1
    if (l==3):
        l=0
        k=k+1
    if (k==3):
        m=9
for i in matriz:  
    print(i,end = "\n")