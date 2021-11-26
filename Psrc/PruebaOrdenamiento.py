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