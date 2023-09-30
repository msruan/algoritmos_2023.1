public class Tempo{
	public static void main(String args[]){
		//Tempo.converter_to_Horas_e_Minutos(142);
		Tempo.converter_seg_to_hms(3661);
	}
	//2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
	public static int converter_Horas_e_Minutos_to_Minutos(int horas,int minutos){
		return (horas*60)+minutos;
	}
	/*3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.*/
	public static void converter_Minutos_to_Horas_e_Minutos(int minutos){
		int horas = (minutos - minutos % 60) / 60;
		minutos -= (horas * 60);
		System.out.println("\nHoras:"); 
		System.out.println(horas);
		System.out.println("Minutos:");
		System.out.println(minutos);
	}
	/*27.Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
	segundos ele corresponde.*/
	public static void converter_seg_to_hms(int segundos){
		int horas = (segundos  - (segundos % 3600))/3600;
		int minutos = (segundos / 60) - (horas * 60);	
		segundos -= (horas * 3600 + minutos * 60);
		System.out.println("Horas: ");
		System.out.println(horas);
		System.out.println("Minutos:");
		System.out.println(minutos);
		System.out.println("Segundos:");
		System.out.println(segundos);
	}
}
