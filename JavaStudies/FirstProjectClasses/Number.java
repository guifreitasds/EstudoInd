package com.capclass;

public class Number {
	private double number;
	private double percent;
	
	// Metodos acessores
	public double getNumber() {
		return number;
	}

	public void setNumber(double number) {
		this.number = number;
	}

	public double getPercent() {
		return percent;
	}

	public void setPercent(double percent) {
		this.percent = percent;
	}
	
	public double calculatePR() {
		double percentreal = (percent/100);
		double total = (number * percentreal);
		return total;
	}


}
