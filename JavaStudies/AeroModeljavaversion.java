package com.lpcclass;
import java.util.Scanner;

public class AeroModeljavaversion {
	public static void main(String [] args) {
		// AeroModel w/ Java
	    
		int comando, continue1, continue2, continue3, continue4, continue5;
		System.out.println("Vamos pilotar sua aeronave? Digite os comandos na ordem correta!");
		System.out.println("Comandos: 1 = Acelerar, 2 = Decolar 3 = Piloto Autom�tico, 4 = Freiar, 5 = Pousar, 6 = Desligar o sistema");
		
		Scanner execute = new Scanner(System.in);
		System.out.println("Digite o Comando abaixo:");
		comando = execute.nextInt();
		boolean TurnOn = true;
		
		while (TurnOn) {
			
			while(comando != 1) {
				System.out.println("Digite o Comando v�lido abaixo:");
				comando = execute.nextInt();
			}
			if (comando == 1) {
				System.out.println("O avi�o est� acelerando!");
				System.out.println("Digite o proximo comando: ");
				continue1 = execute.nextInt();
				
			    while(continue1 != 2) {
				     System.out.println("Digite o Comando v�lido abaixo:");
				     continue1 = execute.nextInt();
			    }
				
			if (continue1 == 2) {
			    System.out.println("O avi�o est� decolando!");
				System.out.println("Digite o proximo comando: ");
			    continue2 = execute.nextInt();
			    
				while(continue2 != 3) {
					System.out.println("Digite o Comando v�lido abaixo:");
					continue2 = execute.nextInt();
				}
			    
			if (continue2 == 3) {
			    System.out.println("Voc� ligou o piloto autom�tico!");
				System.out.println("Digite o proximo comando: ");
			    continue3 = execute.nextInt();
			    
				while(continue3 != 4) {
					System.out.println("Digite o Comando v�lido abaixo:");
					continue3 = execute.nextInt();
				}
			    
			if (continue3 == 4) {
				System.out.println("O avi�o est� freiando!");
				System.out.println("Digite o proximo comando: ");
				continue4 = execute.nextInt();
				
				while(continue4 != 5) {
					System.out.println("Digite o Comando v�lido abaixo:");
					continue4 = execute.nextInt();
				}
				
			if (continue4 == 5) {
				System.out.println("O avi�o est� pousando!");
				System.out.println("Digite o proximo comando: ");
				continue5 = execute.nextInt();
				
				while(continue5 != 6) {
					System.out.println("Digite o Comando v�lido abaixo:");
					continue5 = execute.nextInt();
				}
				
			if (continue5 == 6) {
				System.out.println("O voo foi conclu�do com sucesso!!!");
				
			}
			execute.close();
		}
	}


}}}}}}
