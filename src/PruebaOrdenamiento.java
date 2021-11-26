
class AlgoritmosOrdenamiento{
	
	static long comparaciones = 0;
	static long intercambios = 0;
	static long recorrido = 0;
	
	public static void mostrarDatos(long tFin1, long tInicio1, long recorrido1, long comparaciones1, long intercambios1) {
		System.out.println("\nTiempo de ejecucion en ordenamiento por burbuja: " + (tFin1-tInicio1));
		System.out.println("Recorridos: " + recorrido1);
		System.out.println("Comparaciones: " + comparaciones1);
		System.out.println("Intercambios: " + intercambios1);
		comparaciones = recorrido = intercambios = 0;
	}
	
	public static void burbuja1(int []numeros) {
		 long tInicio = System.currentTimeMillis();
		 
		 for(int i=1; i<=numeros.length-1; i++) {
			for(int j=0; j<=numeros.length-i-1; j++) {
				comparaciones++;
				if(numeros[j]>numeros[j+1]) {
					int aux = numeros[j];
					numeros[j] = numeros[j+1];
					numeros[j+1] = aux;
					intercambios++;
				}
				recorrido++;
			}
		}
		long tFin = System.currentTimeMillis();
		mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
		
	}
	
	public static void burbuja2(int []numeros) {
    	int i = 1;
    	long tInicio = System.currentTimeMillis();
    	while(i<numeros.length) {
    		for(int j = 0; j < numeros.length-i; j++) {
    			comparaciones++;
    			if(numeros[j] > numeros[j+1]) {
    				int aux = numeros[j];
					numeros[j] = numeros[j+1];
					numeros[j+1] = aux;
					intercambios++;
    			}
    			recorrido++;
    		}
    		i = i + 1;
    		
    	}
    	long tFin = System.currentTimeMillis();
        mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
	}
	
	public static void burbuja3(int []numeros) {
	       long tInicio = System.currentTimeMillis();
	       int i=1;
	 	   do {
	 		   
	 		   for(int j=0; j<numeros.length-i; j++) {
					comparaciones++;
					if(numeros[j]>numeros[j+1]) {
						int aux = numeros[j];
						numeros[j] = numeros[j+1];
						numeros[j+1] = aux;
						intercambios++;
					}
					recorrido++;
				}
	 		   
	 		   i=1+i;
	 	   } while(i<numeros.length);
	 	    long tFin = System.currentTimeMillis();
	 	    mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
	    }
	
	private static void quicksort(int a[], int primero, int ultimo) {
		 int i, j, central;
		 int pivote; 
		 central = (primero + ultimo)/2;
		 pivote = a[central];
		 i = primero;
		 j = ultimo;
		 do {
			 comparaciones++;
		 	 while (a[i] < pivote) i++;
		 	comparaciones++;
		 	 while (a[j] > pivote) j--;
		 	 if (i <= j) {
		 		 // Se intercambian
		 		 intercambios++;
		 		 int aux = a[i];
				 a[i] = a[j];
				 a[j] = aux;
		 	 	 i++;
		 	 	 j--;
		 	 }
		 	 recorrido++;
		 } while (i <= j);
		 
		 if (primero < j)
		 	 quicksort(a, primero, j); // mismo proceso con sublista izqda
		 if (i < ultimo)
		 	 quicksort(a, i, ultimo); // mismo proceso con sublista drcha
	}
	
	public static void quicksort(int a[]) {
		long tFin, tInicio = System.currentTimeMillis();
		quicksort(a, 0, a.length-1);
		tFin = System.currentTimeMillis();
		mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
	}
	
	public static void ordenacionShell(int a[]) {
		 int intervalo, i, j, k;
		 int n= a.length;
		 intervalo = n / 2;
		 
		 long tFin, tInicio = System.currentTimeMillis();
		 while (intervalo > 0)
		 {
			 
		 	 for (i = intervalo; i < n; i++)
		 	 {
		 	 	 j = i - intervalo;
		 	 	 while (j >= 0)
		 	 	 {
		 	 	 	 k = j + intervalo;
		 	 	 	 comparaciones++;
		 	 	 	 if (a[j] <= a[k])
		 	 	 	 	 j = -1; 
		 	 	 	 else
		 	 	 	 {
		 	 	 		 intercambios++;
		 	 	 	 	 intercambiar(a, j, j+1);
		 	 	 	 	 j -= intervalo;
		 	 	 	 }
		 	 	 	 recorrido++;
		 	 	 }
		 	 }
		 	 intervalo = intervalo / 2;
		 }
		 tFin = System.currentTimeMillis();
		 System.out.println("\nTiempo de ordenamiento: " + (tFin -tInicio));
		 mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
	}
	
	public static void intercambiar(int []a, int i, int j) {
		 int aux = a[i];
		 a[i] = a[j];
		 a[j]= aux ;
	}
	
	public static void radix(int []nums) {
		int[][] bucket = new int[10][nums.length];
		int[] bucketOfElement = new int[10];
		int max=0;
		
		 long tFin, tInicio = System.currentTimeMillis();
	
		for(int i = 0 ; i < nums.length;i++) {
			comparaciones++;
			if(nums[i]>max){
				intercambios++;
				max = nums[i];
			}
			recorrido++;
		}
		
		int maxLength = (max+"").length();
		for(int m = 0,n=1;m<maxLength;m++,n*=10) {
			recorrido++;
			for(int i = 0 ; i < nums.length;i++) {
				int digit = nums[i]/n%10;
				intercambios++;
				bucket[digit][bucketOfElement[digit]] = nums[i];
				bucketOfElement[digit]++;
			}
			int index = 0;
			
			for(int j = 0;j<10;j++) {
				for(int k = 0 ; k<bucketOfElement[j];k++) {
					intercambios++;
					nums[index] = bucket[j][k];
					index++;
				}
				bucketOfElement[j]=0;
				recorrido++;
			}
		}
		tFin = System.currentTimeMillis();
		mostrarDatos(tFin, tInicio, recorrido, comparaciones, intercambios);
	}
	
}

public class PruebaOrdenamiento {
	public static void main(String[] args) {
		
	}
}
