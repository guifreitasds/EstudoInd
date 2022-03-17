package com.lpcclass;
import java.util.Scanner;

public class AeroModeljavaversion {
	public static void main(String [] args) {
		// AeroModel w/ Java
	    
		int comando, continue1, continue2, continue3, continue4, continue5;
		System.out.println("Vamos pilotar sua aeronave? Digite os comandos na ordem correta!");
		System.out.println("Comandos: 1 = Acelerar, 2 = Decolar 3 = Piloto Automático, 4 = Freiar, 5 = Pousar, 6 = Desligar o sistema");
		
		Scanner execute = new Scanner(System.in);
		System.out.println("Digite o Comando abaixo:");
		comando = execute.nextInt();
		boolean TurnOn = true;
		
		while (TurnOn) {
			
			while(comando != 1) {
				System.out.println("Digite o Comando válido abaixo:");
				comando = execute.nextInt();
			}
			if (comando == 1) {
				System.out.println("O avião está acelerando!");
				System.out.println("Digite o proximo comando: ");
				continue1 = execute.nextInt();
				
			    while(continue1 != 2) {
				     System.out.println("Digite o Comando válido abaixo:");
				     continue1 = execute.nextInt();
			    }
				
			if (continue1 == 2) {
			    System.out.println("O avião está decolando!");
				System.out.println("Digite o proximo comando: ");
			    continue2 = execute.nextInt();
			    
				while(continue2 != 3) {
					System.out.println("Digite o Comando válido abaixo:");
					continue2 = execute.nextInt();
				}
			    
			if (continue2 == 3) {
			    System.out.println("Você ligou o piloto automático!");
				System.out.println("Digite o proximo comando: ");
			    continue3 = execute.nextInt();
			    
				while(continue3 != 4) {
					System.out.println("Digite o Comando válido abaixo:");
					continue3 = execute.nextInt();
				}
			    
			if (continue3 == 4) {
				System.out.println("O avião está freiando!");
				System.out.println("Digite o proximo comando: ");
				continue4 = execute.nextInt();
				
				while(continue4 != 5) {
					System.out.println("Digite o Comando válido abaixo:");
					continue4 = execute.nextInt();
				}
				
			if (continue4 == 5) {
				System.out.println("O avião está pousando!");
				System.out.println("Digite o proximo comando: ");
				continue5 = execute.nextInt();
				
				while(continue5 != 6) {
					System.out.println("Digite o Comando válido abaixo:");
					continue5 = execute.nextInt();
				}
				
			if (continue5 == 6) {
				System.out.println("O voo foi concluído com sucesso!!!");
				
			}
			execute.close();
		}
	}


}}}}}}
