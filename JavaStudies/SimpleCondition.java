
public class SimpleCondition {
	public static void main(String [] args) {
		double number1 = 10;
		double number2 = 11;
		
		double sum = (number1 + number2);
		double mult = (number1 * number2);
		
		if(number1 == number2) {
			System.out.println("A soma é igual a: " + sum);
		}
		else {
			System.out.println("A multiplicação é igual a: " + mult);
		}
	}

}
