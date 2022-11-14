void main() {
  TimeFutebol time1 = TimeFutebol(); 
  
  time1.setNomePres("Yuri Romão");
  time1.setNumJogadores(30);
  
  String atribtime1 = time1.toString();
  print(atribtime1);
}

class TimeFutebol{
  late String _nome = "Sport Club do Recife";
  late int _NumJogadores;
  late String _NomePresidente;
  

  String get NomedoClube => _nome;
  
  void setNumJogadores(int numDado) => _NumJogadores = numDado;
  int get NumJogadores => _NumJogadores;
  
  void setNomePres(String nomeDado) => _NomePresidente = nomeDado;
  String get NomePres => _NomePresidente;
  
  String toString(){
    return 'Nome: ${NomedoClube}, Número de jogadores: ${NumJogadores}, Presidente: ${NomePres}';
  }
}
