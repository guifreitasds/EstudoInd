import 'dart:convert';

void main() {
 Map users = {
   "user1":"Guilherme",
   "user2":"Pedro",
   "user3":"Laura",
   "permissions":["user", "admin"]
   };

  print(users);
  var result = jsonEncode(users);
  print(result);
}