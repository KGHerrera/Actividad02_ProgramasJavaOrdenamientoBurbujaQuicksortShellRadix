
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
	
	
	
	
	
}

public class PruebaOrdenamiento {
	public static void main(String[] args) {
		
	}
}
