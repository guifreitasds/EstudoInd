void main() {
  TimeFutebol time1 = TimeFutebol(); 
  
  time1.setNomePres("Yuri Romão");
  time1.setNumJogadores(30);
  
  String atribtime1 = time1.toString();
  print(atribtime1);
}

class TimeFutebol{  // Criação da classe para uso dos atributos e metodos

  // Declaração de atributos privados, ao usar underline(_)
  late String _nome = "Sport Club do Recife";
  late int _NumJogadores;
  late String _NomePresidente; 
  
  

  String get NomedoClube => _nome; // Uso de arrow function para criação do metodo get
  
  void setNumJogadores(int numDado) => _NumJogadores = numDado; // Uso de arrow function para criação do método set
  int get NumJogadores => _NumJogadores;
  
  void setNomePres(String nomeDado) => _NomePresidente = nomeDado;
  String get NomePres => _NomePresidente;
  
  String toString(){ // Método toString para print da classe
    return 'Nome: ${NomedoClube}, Número de jogadores: ${NumJogadores}, Presidente: ${NomePres}';
  }
}
