'''
Created on 25/11/2021

@author: Herrera
'''

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