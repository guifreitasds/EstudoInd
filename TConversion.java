
public class TConversion {
	public static void main(String[] args) {
		double C, F, K, Re, Ra;
		
		C = 30;
		
		F = (C * 1.8 + 32);
		K = (C + 273.15);
		Re = (C * 0.8);
		Ra = (C * 1.8 + 32 + 459.67);
		
		System.out.println("O valor da temperatura em Fahrenheit é: " + F);
		System.out.println("O valor da temperatura em Kelvin é: " + K);
		System.out.println("O valor da temperatura em Réaumur é: " + Re);
		System.out.println("O valor da temperatura em Rankine é: " + Ra);
	}

}
