void main(){
  try{
    print((2/0).toInt());
  }catch(e){
    print("print do erro ${e}");
    // rethrow; // propagando o erro
    // throw Exception("Erro do tipo A001"); // Jogando um erro com Exception
    throw ErroCustomizado('ERRO');
  }
}

class ErroCustomizado implements Exception{

  final String erro;
  ErroCustomizado(this.erro);
    
}