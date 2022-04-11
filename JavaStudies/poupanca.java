package com.dawclass;
import java.util.Scanner;

public class poupanca {
	public static void main(String [] args) {
	Scanner util = new Scanner(System.in);
	double balance = 0;
	
	System.out.println("Seu saldo é: " + balance);
	System.out.println("Digite o valor do depósito: ");
	double deposit = util.nextDouble();
	double rende = balance + deposit;
	double rendmes = ((rende * 0.05)+ rende);
	
	System.out.println("Seu saldo agora é de: " + rende);
	System.out.println("O rendimento do próximo mês será: " + rendmes);
	
	
	

	util.close();
	}
	
}
