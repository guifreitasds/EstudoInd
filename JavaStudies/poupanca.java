package com.dawclass;
import java.util.Scanner;

public class poupanca {
	public static void main(String [] args) {
	Scanner util = new Scanner(System.in);
	double balance = 0;
	
	System.out.println("Seu saldo �: " + balance);
	System.out.println("Digite o valor do dep�sito: ");
	double deposit = util.nextDouble();
	double rende = balance + deposit;
	double rendmes = ((rende * 0.05)+ rende);
	
	System.out.println("Seu saldo agora � de: " + rende);
	System.out.println("O rendimento do pr�ximo m�s ser�: " + rendmes);
	
	
	

	util.close();
	}
	
}
