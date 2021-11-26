import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

class AlgoritmosOrdenamiento{
	
	static long comparaciones = 0;
	static long intercambios = 0;
	static long recorrido = 0;
	
	public static void mostrarDatos(long tFin1, long tInicio1, long recorrido1, long comparaciones1, long intercambios1) {
		System.out.println("\nTiempo de ejecucion: " + (tFin1-tInicio1));
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
		
		Random random = new Random();
		int [] vect = new int[1000];
		for (int i = 0; i < vect.length; i++) {
			vect[i] = random.nextInt(100) + 1;
		}
		
		
		int opcion = 0;
		Scanner entrada = new Scanner(System.in);
		
		do {
			System.out.println("\nIntroduce metodo de ordenamiento: ");
			System.out.println("1) burbuja 1");
			System.out.println("2) burbuja 2");
			System.out.println("3) burbuja 3");
			System.out.println("4) Quicksort");
			System.out.println("5) Shellsort");
			System.out.println("6) Radix");
			System.out.println("7) cambiar longitud de vector");
			System.out.println("8) Salir");
			System.out.println("Introduce opcion: ");
			opcion = entrada.nextInt();
			
			
			int vector[] = vect.clone(); 
			
			
			switch (opcion) {
				
			case 1:
				
				AlgoritmosOrdenamiento.burbuja1(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
				
			case 2:
				
				AlgoritmosOrdenamiento.burbuja2(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
				
			case 3:
				
				AlgoritmosOrdenamiento.burbuja3(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
				
			case 4:
				
				AlgoritmosOrdenamiento.quicksort(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
				
			case 5:
		
				AlgoritmosOrdenamiento.ordenacionShell(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
			case 6:
				
				
				AlgoritmosOrdenamiento.radix(vector);
				System.out.println("\nEl vector a sido ordenado");
				System.out.println(Arrays.toString(vector));
				
				break;
			
			case 7:
				System.out.println("\nIntroduce nueva longitud: ");
				int longitud = entrada.nextInt();
				int nuevoVector[] = new int[longitud];
				for (int i = 0; i < nuevoVector.length; i++) {
					nuevoVector[i] = random.nextInt(100)+1;
				}
				
				vect = nuevoVector;
				break;
			case 8:
				System.out.println("\nSaliendo . . .");
				break;
			default:
				System.out.println("\nOpcion incorrecta");
				break;
			}
			
		} while(opcion != 8);
	}
	
	/*
		Crear vectores con números aleatorios con los siguientes tamaños:
        - 1000
        - 10000
        - 100000
        - 1000000

		Mostrar los tiempos de ejecución.
		Mostrar cantidad de recorridos, comparaciones e intercambios
		Crear una TABLA comparativa con los resultados.
		
		
		prueba vector con 1000 elementos
		
		metodo				tiempo			recorridos			comparaciones			intercambios
		
		burbuja 1			20				499500				499500					241532
		
		burbuja 2			18				499500				499500					241532
		
		burbuja 3			17				499500				499500					241532
		
		quicksort			1				3141				6282					3061
		
		shellsort			17				252673				252673					246008
		
		radixsort			1				1033				1000					6004
		
		
		prueba vector con 10000 elementos
		
		metodo				tiempo			recorridos			comparaciones			intercambios
		
		burbuja 1			299				49995000			49995000				24801380
		
		burbuja 2			241				49995000			49995000				24801380
		
		burbuja 3			239				49995000			49995000				24801380
		
		quicksort			25				46532				93064					46326
		
		shellsort			161				24982519			24982519				24877598
		
		radixsort			23				10033				10000					60009
		
		
		prueba vector con 100000 elementos
		
		metodo				tiempo			recorridos			comparaciones			intercambios
		
		burbuja 1			29019			4999950000			4999950000				2485512471
		
		burbuja 2			24438			4999950000			4999950000				2485512471
		
		burbuja 3			23660			4999950000			4999950000				2485512471
		
		quicksort			61				626573				1253146					626264
		
		shellsort			10822			2487892699			2487892699				2486543695
		
		radixsort			32				10033				10000					60009
		
		
		prueba vector con 1000000 elementos
		
		metodo				tiempo			recorridos			comparaciones		intercambios
		
		burbuja 1			2890129			49999500000			49999500000			2485512471
		
		burbuja 2			2434384 		49999500000			49999500000			2485512471
		
		burbuja 3			2338609			49999500000			49999500000			2485512471
		
		quicksort			137				7884527				15769054			7884074
		
		shellsort			128282			248738913699		25417892639			24187543595
		
		radixsort			104				1000033				1000000				6000005
	
	 */
	
	
	
}
