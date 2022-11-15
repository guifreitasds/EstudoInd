void main() async{ // Declaração do método main de forma assíncrona para utilização do await
  ClassExterna externo = ClassExterna();

  Future<String> coisaExterna = externo.getAlgoExterno(); // Criação de uma variável futura

  String coisa = await coisaExterna; // Utilização do await para esperar o término da requisição externa, para prosseguimento do código

  print(coisa);
}

class ClassExterna{ // Criação da classe que possui o método de requisição externa
  Future<String> getAlgoExterno(){
    return Future.value("Algo Externo");
  }
}