n=int(input("Ingresa cantidad de numeros a ordenar: "))
A=[0 for i in range(n)]

#Ingresando los valores de los numeros
for i in range(n):
    A[i]=int(input("Ingrese un valor :"))

#Metodo burbuja
for i in range(n-1):
    for j in range(n-1):
        if(A[j]>A[j+1]):

            aux=A[j]
            A[j]=A[j+1]
            A[j+1]=aux
#Ordenando los numeros
print("\nNumeros de menor a mayor: ")
for i in range (n):
    print(A[i])

input('\nPress ENTER to exit')