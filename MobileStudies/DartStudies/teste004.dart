void main() async{
  ClassExterna externo = ClassExterna();

  Future<String> coisaExterna = externo.getAlgoExterno();

  String coisa = await coisaExterna;

  print(coisa);
}

class ClassExterna{
  Future<String> getAlgoExterno(){
    return Future.value("Algo Externo");
  }
}