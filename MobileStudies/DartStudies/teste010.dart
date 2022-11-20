void main() {
  int anonasc = 2000; // Valor dado ao usuário de ano de nascimento

  print(anonasc.IntYeartoAge());
}

extension UtilsInt on int { // Método que retorna a idade a partir de um valor int do ano de nascimento
  int IntYeartoAge() {
    var currDt = DateTime.now(); // Criando objeto de datas
    return (currDt.year - this); // Calculo referenciando o ano atual menos o valor passado pelo usuário
  }
}
