void main() async{
 Map<String, String> Pessoas = {"Nome":"Guilherme", "Sobrenome":"Freitas"};
  print(Pessoas);

  Pessoas.putIfAbsent("Último Nome", ()=>"Santos");

  Pessoas["Idade"] = "17";

  print('${Pessoas["Nome"]} ${Pessoas["Sobrenome"]} dos ${Pessoas["Último Nome"]} tem ${Pessoas["Idade"]} anos');

  Pessoas.update("Idade", (value) => "18");

  print('${Pessoas["Nome"]} ${Pessoas["Sobrenome"]} dos ${Pessoas["Último Nome"]} e agora ele tem ${Pessoas["Idade"]} anos');

  Pessoas.forEach((chave, valor) => print("$chave tem valor $valor"));
  
}