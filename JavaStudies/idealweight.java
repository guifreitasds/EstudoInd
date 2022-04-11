	package com.dawclass;
	import java.util.Scanner;
	
	public class idealweight {
		public static void main(String [] args) {
			Scanner util = new Scanner(System.in);
			System.out.print("Digite sua altura: ");
			double height = util.nextDouble();
			
			double form = ((72.7 * height) - 58);
			
			System.out.print("Seu peso ideal é: " + form + "Kg");
			
		}
	
	}
