class Velocidade{
	public static void main(String []args){
	}
	//1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
	public static float ms_to_kmh(float ms){
		return (ms * 3.6f);
	}
	//6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
	public static float kmh_to_ms(float kmh){
		return (kmh / 3.6f);
	}
}
