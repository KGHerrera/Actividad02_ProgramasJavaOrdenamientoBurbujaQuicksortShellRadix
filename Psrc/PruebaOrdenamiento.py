'''
Created on 25/11/2021

@author: Herrera
'''
import time
import math
import random

class AlgoritmosOrdenamiento:
    
    def __init__(self):
        self.intercambios = 0
        self.recorridos = 0
        self.comparaciones = 0 
    
    
    def mostrarDatos(self, inicio, fin, recorridos, intercambios, comparaciones):
        print(f"Tiempo: {fin-inicio}")
        print(f"Recorridos: {self.recorridos}")
        print(f"Intercambios: {self.intercambios}")
        print(f"Comparaciones: {self.comparaciones}")
        self.comparaciones = self.intercambios = self.recorridos = 0
    
    def burbuja1(self, arreglo):
        inicio = time.time()
        self.comparaciones = self.intercambios = self.recorridos = 0
        for i in range(1, len(arreglo)):
            for j in range(0, len(arreglo)-i):
                if arreglo[j]>arreglo[j+1]:
                    aux = arreglo[j]
                    arreglo[j] = arreglo[j+1]
                    arreglo[j+1] = aux
        fin = time.time()
        
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
        
    
    
    def burbuja2(self, arreglo):
        i = 0
        inicio = time.time()
        while i<len(arreglo):
            j=i
            while j<len(arreglo):
                self.comparaciones+=1
                if arreglo[i]>arreglo[j]:
                    aux = arreglo[i]
                   
                    arreglo[i] = arreglo[j]
                    arreglo[j] = aux
                    self.comparaciones+=1
                self.recorridos+=1
                j+=1
            i+=1
        fin = time.time()
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
        
    
    
    def burbuja3(self, numeros): 
        i = 1
        inicio = time.time()
        while(i < len(numeros)):
            for j in range(len(numeros)-i):
                self.comparaciones+=1
                if(numeros[j] > numeros[j+1]):
                    aux = numeros[j]
                    numeros[j] = numeros[j+1]
                    numeros[j+1] = aux
                    self.intercambios+=1
                self.recorridos+=1
            i = 1 + i 
             
        fin = time.time()
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
    
    @staticmethod
    def intercambiar(a, i, j):
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
        
    
    def quicksort(self, a, primero, ultimo):
        central = int((primero + ultimo)/2)
        pivote = a[central]
        i = primero
        j = ultimo
        
        while(i <= j):
            self.comparaciones+=1
            while(a[i] < pivote):
                i+=1
            self.comparaciones+=1
            while(a[j] > pivote):
                j-=1
            self.comparaciones+=1
            if(i <= j):
                self.intercambios+=1
                AlgoritmosOrdenamiento.intercambiar(a, i, j)
                i+=1
                j-=1
            self.recorridos+=1
        if(primero < j):
            AlgoritmosOrdenamiento.quicksort(a, primero, j)
        if(i < ultimo):
            AlgoritmosOrdenamiento.quicksort(a, i, ultimo)
            
    def quicksortLlamada(self, a):
        inicio = time.time()
        AlgoritmosOrdenamiento.quicksort(a, 0, len(a)-1)
        fin = time.time()
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
        
    def shellSort(self, numeros):
        inicio = time.time()
        intervalo = int(len(numeros)/2)
        while(intervalo>0):
            for i in range(int(intervalo), len(numeros)):
                j=i-int(intervalo)
                while(j>=0):
                    k=j+int(intervalo)
                    self.comparaciones+=1
                    if numeros[j]<=numeros[k]:
                        j-=1
                    else:
                        self.intercambios+=1
                        aux=numeros[j]
                        numeros[j]=numeros[k]
                        numeros[k]=aux
                        j-=int(intervalo)
                    self.recorridos+=1
            intervalo=int(intervalo)/2
            
        fin = time.time()
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
        
    def counting_sort(self, A, digit, radix):
        
        B = [0]* len(A)
        C = [0]* int(radix)
        
        for i in range(0, len(A)):
            self.intercambios+=1
            self.comparaciones+=1
            digit_of_Ai = (A[i]/radix ** digit)% radix
            C[int(digit_of_Ai)] = C[int(digit_of_Ai)] +1 
            self.recorridos+=1
            
        for j in range(1, radix):
            self.intercambios+=1
            C[j]= C[j]+ C[j-1]
            self.recorridos+=1
            
        for m in range(len(A)-1, -1, -1):
            self.intercambios+=1
            self.comparaciones+=1
            digit_of_Ai = (A[m]/radix ** digit)% radix
            C[int(digit_of_Ai)]= C[int(digit_of_Ai)]-1
            B[C[int(digit_of_Ai)]] = A[m]
            self.recorridos+=1
        return B 
    
    def radix_sort(self, A, radix):
        inicio = time.time()
        k = max(A)
        
        output = A 
        
        digits = int(math.floor(math.log(k, radix)+1))
        for i in range(digits):
            output= self.counting_sort(output, i, radix)
        
        fin = time.time()
        self.mostrarDatos(inicio, fin, self.recorridos, self.intercambios, self.comparaciones)
        return output
    
vect = []
opcion = 0
a1 = AlgoritmosOrdenamiento()
for i in range(10):
    vect.append(random.randrange(70, 99, 2))

while(opcion != 20):
    print("\nIntroduce metodo de ordenamiento: ");
    print("1) burbuja 1");
    print("2) burbuja 2");
    print("3) burbuja 3");
    print("4) Quicksort");
    print("5) Shellsort");
    print("6) Radix")
    print("7) Salir");
    opcion = int(input("Introduce opcion: "))
    
    vector = vect.copy()
    
    
    if (opcion == 1):
        print("\nVector sin ordenar: ")
        print(vector)
        AlgoritmosOrdenamiento.burbuja1(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    if (opcion == 2):
        print("\nVector sin ordenar: ")
        print(vector)
        AlgoritmosOrdenamiento.burbuja2(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    if (opcion == 3):
        print("\nVector sin ordenar: ")
        print(vector)
        AlgoritmosOrdenamiento.burbuja3(vector)
        print("\nVector ordenado: ")
        print(vector)
    
    if (opcion == 4):
        print("\nVector sin ordenar: ")
        print(vector)
        AlgoritmosOrdenamiento.quicksortLlamada(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    if (opcion == 5):
        print("\nVector sin ordenar: ")
        print(vector)
        AlgoritmosOrdenamiento.shellSort(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    if (opcion == 6):
        print("\nVector sin ordenar: ")
        print(vector)
        
        print("\nVector ordenado: ")
        print(a1.radix_sort(vector, 10))
        
    if (opcion == 7):
        print("\nSaliendo . . .")