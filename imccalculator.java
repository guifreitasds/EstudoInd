
public class imccalculator {
	public static void main(String[] args) {
		double weight = 100.5;
		double height = 1.75;
		double imc;
		
		imc = (weight/(height*height));
		
		System.out.println("O seu IMC � de: " + imc);
		
		if(imc < 18.5){
			System.out.println("Voc� est� abaixo do peso");
		}
		if(imc >= 18.6 && imc <= 24.9) {
			System.out.println("Seu peso � ideal!");
		}
		if(imc >= 25 && imc <= 29.9) {
			System.out.println("Sobrepeso");
		}
		else {
			System.out.println("Obesidade");
		}
	}

}
