'''
Created on 25/11/2021

@author: Herrera
'''
import time

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