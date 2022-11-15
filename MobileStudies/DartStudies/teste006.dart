import 'dart:convert';

void main() {

  // Criação do JSON para decodificação e passagem para um tipo mapa
 String json = """ 

    {
      "user": "guifreitasds",
      "pass": "senha123",
      "permissions":[
        "user", "admin"
      ]
    }
   """;

  print(json);
  var resultJson = jsonDecode(json); // Utilização da lib convert com o método decode e passagem do JSONString para JSONMap
  print(resultJson["permissions"]);
}