import java.util.Scanner;
public class TConversion {
	public static void main(String[] args) {
		
		double C, F, K, Re, Ra;
		
		Scanner Celsius = new Scanner(System.in);
		System.out.println("Digite a temperatura: ");
		C = Celsius.nextDouble();
		
		
		F = (C * 1.8 + 32);
		K = (C + 273.15);
		Re = (C * 0.8);
		Ra = (C * 1.8 + 32 + 459.67);
		
		System.out.println("O valor da temperatura em Fahrenheit �: " + F);
		System.out.println("O valor da temperatura em Kelvin �: " + K);
		System.out.println("O valor da temperatura em R�aumur �: " + Re);
		System.out.println("O valor da temperatura em Rankine �: " + Ra);
		
		Celsius.close();
	}

}
