import 'dart:convert';

void main() {
  //Criação de um JSONMap para passagem para o tipoJson
 Map users = {
   "user1":"Guilherme",
   "user2":"Pedro",
   "user3":"Laura",
   "permissions":["user", "admin"]
   };

  print(users);
  var result = jsonEncode(users); // Utilização do método encode para passagem do tipo map para JSON válido
  print(result);
}