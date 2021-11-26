
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
	
	
	
}

public class PruebaOrdenamiento {
	public static void main(String[] args) {
		
	}
}
