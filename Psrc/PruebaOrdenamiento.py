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
        print(f"Comparaciones: {self.comparaciones}")
        print(f"Intercambios: {self.intercambios}")
        
        self.comparaciones = self.intercambios = self.recorridos = 0
    
    def burbuja1(self, arreglo):
        inicio = time.time()
        self.comparaciones = self.intercambios = self.recorridos = 0
        for i in range(1, len(arreglo)):
            for j in range(0, len(arreglo)-i):
                self.comparaciones+=1
                if arreglo[j]>arreglo[j+1]:
                    self.intercambios +=1
                    aux = arreglo[j]
                    arreglo[j] = arreglo[j+1]
                    arreglo[j+1] = aux
                self.recorridos+=1
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
                    self.intercambios+=1
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
            self.quicksort(a, primero, j)
        if(i < ultimo):
            self.quicksort(a, i, ultimo)
            
    def quicksortLlamada(self, a):
        inicio = time.time()
        self.quicksort(a, 0, len(a)-1)
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
    print("7) cambiar longitud del vector")
    print("8) Salir")
    opcion = int(input("Introduce opcion: "))
    
    vector = vect.copy()
    
    
    if (opcion == 1):
        print("\nVector sin ordenar: ")
        print(vector)
        a1.burbuja1(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    elif (opcion == 2):
        print("\nVector sin ordenar: ")
        print(vector)
        a1.burbuja2(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    elif (opcion == 3):
        print("\nVector sin ordenar: ")
        print(vector)
        a1.burbuja3(vector)
        print("\nVector ordenado: ")
        print(vector)
    
    elif (opcion == 4):
        print("\nVector sin ordenar: ")
        print(vector)
        a1.quicksortLlamada(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    elif (opcion == 5):
        print("\nVector sin ordenar: ")
        print(vector)
        a1.shellSort(vector)
        print("\nVector ordenado: ")
        print(vector)
        
    elif (opcion == 6):
        print("\nVector sin ordenar: ")
        print(vector)
        
        print("\nVector ordenado: ")
        print(a1.radix_sort(vector, 10))
    
    elif (opcion == 7): 
        longitud = int(input("\nIntroduce nueva longitud: "))   
        nuevoVector = [0]*longitud
        
        for i in range(len(nuevoVector)):
            nuevoVector[i] = (random.randrange(70, 99, 2))
            
        vect = nuevoVector
        
    
    elif (opcion == 8):
        print("\nSaliendo . . .")
    
    '''
        Crear vectores con números aleatorios con los siguientes tamaños:
        - 1000
        - 10000
        - 100000
        - 1000000

        Mostrar los tiempos de ejecución.
        Mostrar cantidad de recorridos, comparaciones e intercambios
        Crear una TABLA comparativa con los resultados.
        
        
        prueba vector con 1000 elementos
        
        metodo                tiempo            recorridos            comparaciones            intercambios
        
        burbuja 1            0.513988733291    499500                499500                    232362
        
        burbuja 2            0.313989400863    5000500               5000500                   6937
        
        burbuja 3            0.296975851058    499500                499500                    232362
        
        quicksort            0.010014772415    3701                  11103                     3676
        
        shellsort            2.409994125366    3937042               3937042                   3431
        
        radixsort            0.008032321929    4018                  4000                      4018
        
        
        prueba vector con 10000 elementos
        
        metodo                tiempo            recorridos            comparaciones           intercambios
        
        burbuja 1            30.06298732757     49995000            49995000                23439016
        
        burbuja 2            23.4179892539      50005000            50005000                68981
        
        burbuja 3            29.434995651       49995000            49995000                23439016
        
        quicksort            0.106981277        53389               160167                  53343
        
        shellsort            322.3981614        592668512           592668512               43895
        
        radixsort            0.06198191642      40018               40000                   40018
        
        
        prueba vector con 100000 elementos
        
        metodo                tiempo            recorridos            comparaciones           intercambios
        
        burbuja 1            321.8274017        499950000            499950000                2334201632
        
        burbuja 2            243.412426239      500050000            500050000                65286481
        
        burbuja 3            295.5289351        499950000            499950000                2123589016
        
        quicksort            0.957989454        696600               2089800                  696545
        
        shellsort            892.153284         59266812312          59416563512              56584691 
        
        radixsort            0.475990772       400018                400000                   400018
        
        
        prueba vector con 1000000 elementos
        
        metodo                tiempo            recorridos            comparaciones           intercambios
        
        quicksort            11.46198987        8624685              25874055                 8624618
        
        radixsort            4.721994638442     4000018              4000000                  4000018
        
        
    
    '''