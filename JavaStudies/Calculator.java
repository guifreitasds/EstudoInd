package com.lpcclass;
import java.util.Scanner;

public class Calculator {
	public static void main(String[] args) {
		
		float number1, number2, finalresult1, finalresult2, finalresult3, finalresult4;
		
		int op;
		int soma = 1;
		int sub = 2;
		int mult = 3;
		int div = 4;
		
		Scanner operation = new Scanner(System.in);
		
		System.out.println("Vamos calcular?");
		System.out.println("Digite o tipo de opera��o(soma = 1, sub = 2, mult = 3, div = 4): ");
		op = operation.nextInt();
		System.out.println("Digite o primeiro n�mero: ");
		number1 = operation.nextFloat();
		System.out.println("Digite o segundo n�mero: ");
		number2 = operation.nextFloat();
		
		if(op == soma) {
			finalresult1 = (number1 + number2);
			System.out.println("O resultado da soma �: " + finalresult1);
		}
		else if (op == sub) {
			finalresult2 = (number1 - number2);
			System.out.println("O resultado da subtra��o �: " + finalresult2);
			
		}
		else if (op == mult) {
			finalresult3 = (number1 * number2);
			System.out.println("O resultado da multiplica��o �: " + finalresult3);
			
		}
		else if (op == div) {
			finalresult4 = (number1 / number2);
			System.out.println("O resultado da divis�o �: " + finalresult4);
			
		}
		else {
			System.out.println("Opera��o inv�lida!");
		}
		
		operation.close();
	}

}
