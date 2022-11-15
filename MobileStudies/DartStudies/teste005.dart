void main() async{
 Map<String, String> Pessoas = {"Nome":"Guilherme", "Sobrenome":"Freitas"}; // Declaração simples de mapa, passando como atributos String, String (tipo da chave, tipo do dado)
  print(Pessoas);

  Pessoas.putIfAbsent("Último Nome", ()=>"Santos"); // Utilização do método put para colocar um novo valor no mapa

  Pessoas["Idade"] = "17";

  print('${Pessoas["Nome"]} ${Pessoas["Sobrenome"]} dos ${Pessoas["Último Nome"]} tem ${Pessoas["Idade"]} anos');

  Pessoas.update("Idade", (value) => "18"); // Utilização do método uptade para atualização do valor em uma chave específica

  print('${Pessoas["Nome"]} ${Pessoas["Sobrenome"]} dos ${Pessoas["Último Nome"]} e agora ele tem ${Pessoas["Idade"]} anos');

  Pessoas.forEach((chave, valor) => print("$chave tem valor $valor")); // Utilização do método forEach para mostragem do mapa de uma forma organizada e prática
  
}