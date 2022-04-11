package com.dawclass;
import java.util.Scanner;

public class productverifierv2 {
public static void main(String [] args){

  Scanner util = new Scanner(System.in);
  System.out.println("Insira o Valor do produto: ");
  double valor = util.nextDouble();
  System.out.println("Insira a sua região: ");
  String region = util.nextLine(); 
  
  
  while(!(region.equalsIgnoreCase("Norte") || (region.equalsIgnoreCase("Sul") || (region.equalsIgnoreCase("Sudeste") || (region.equalsIgnoreCase("Nordeste") || (region.equalsIgnoreCase("Centro Oeste"))))))) {
	  System.out.println("Opção de região inválida, tente digitar com a primeira maiuscula. Ex: Sul");
	  region = util.nextLine(); 
  }
  
  if(region.equals("Norte")){
    double Northdiscount = (valor - (valor * 0.05));
    System.out.println("O valor final do produto é: R$" + Northdiscount);
  }
  else if(region.equals("Sul")) {
	double Southdiscount = (valor - (valor * 0.15));
    System.out.println("O valor final do produto é: R$" + Southdiscount);

  }
  else if(region.equals("Sudeste")) {
	double Southeastdiscount = (valor - (valor * 0.07));
    System.out.println("O valor final do produto é: R$" + Southeastdiscount);

  }
  else if(region.equals("Nordeste")) {
	double Northeastdiscount = (valor - (valor * 0.12));
    System.out.println("O valor final do produto é: R$" + Northeastdiscount);

  }
  else if(region.equals("Centro Oeste")) {
	double Centereastdiscount = (valor - (valor * 0.20));
    System.out.println("O valor final do produto é: R$" + Centereastdiscount);

  }
  
  util.close();
}


}