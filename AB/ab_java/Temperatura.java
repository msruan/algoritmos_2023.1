public class Temperatura{
	public static void main(String [] args){
		System.out.println(Temperatura.converterParaCel(32));
	}
	//20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
	public static double converterParaFar(double celsius){
		return (9 * celsius + 160) / 5;
	}
	//21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9)
	public static double converterParaCel(double far){
		return (5 * far - 160) / 9;
	}
	
}
