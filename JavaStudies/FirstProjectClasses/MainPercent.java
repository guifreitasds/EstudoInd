package com.capclass;
import java.util.Scanner;

public class MainPercent {
	public static void main(String [] args) {
		Number number = new Number();
		Scanner util = new Scanner(System.in);
		
		System.out.println("Vamos tirar uma porcentagem de um valor!");
		System.out.println("Digite o valor:");
		number.setNumber(util.nextDouble());
		System.out.println("Digite a porcentagem:  Ex: 25");
		number.setPercent(util.nextDouble());
		
		System.out.println(number.getPercent() + "% de " + number.getNumber() + " é igual a: " + number.calculatePR());
		
		util.close();
	}
}
