void main() {
  TimeFutebol time1 = TimeFutebol(); 
  
  time1.setNome("Sport Club do Recife");
  time1.setNomePres("Yuri Romão");
  time1.setNumJogadores(30);
  
  String atribtime1 = time1.toString();
  print(atribtime1);
}

class TimeFutebol{
  late String nome;
  late int NumJogadores;
  late String NomePresidente;
  
  void setNome(String nomeDado){
    this.nome = nomeDado;
  }
  String getNome(){
    return this.nome;
  }
  
  void setNumJogadores(int numDado){
    this.NumJogadores = numDado;
  }
  int getNumJogadores(){
    return this.NumJogadores;
  }
  
  void setNomePres(String nomeDado){
    this.NomePresidente = nomeDado;
  }
  String getNomePres(){
    return this.NomePresidente;
  }
  
  String toString(){
    return 'Nome: ${getNome()}, Número de jogadores: ${getNumJogadores()}, Presidente: ${getNomePres()}';
  }
}
