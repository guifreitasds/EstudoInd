package com.dawclass;
import java.util.Scanner;

public class Products {
	public static void main (String [] args) {
		double local, value, finalvalue;
		double local1 = 1;
		double local2 = 2;
		double cotation = 5.09;
		String name;
		Scanner util = new Scanner(System.in);
		
		do {
		System.out.println("Checagem de Produtos");
		System.out.println("Insira o nome do seu produto: ");
		name = util.nextLine();
		} while(name.isBlank());
		
		
		do {
		System.out.println("Insira o valor do produto: ");
		value = util.nextDouble();
		}while(value < 0);
		
		
		do {
		System.out.println("Insira 1 para produto importado e 2 para produto nacional");
		local = util.nextDouble();
		}while(local != 1 && local != 2);
		
		
		if(local == local1) {
			finalvalue = (value * cotation);
			System.out.println("O valor final de " + name + " é: R$" + finalvalue);
		}
		else if(local == local2) {
			System.out.println("O valor final de " + name + " é: R$" + value);
			
		}
		else {
			System.out.println("Insira um valor de local válido!");
		}
		util.close();
	}
}
