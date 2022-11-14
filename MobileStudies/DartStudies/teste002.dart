void main(){
  Gerente gerente01 = Gerente();
  gerente01.salario = 1000;
  print(gerente01.salario);
}

class Funcionario{
  late String nome;
  late double salario;
}

class Gerente extends Funcionario{
  late bool permission;
}