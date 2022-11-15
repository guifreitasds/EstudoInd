import 'dart:convert';

void main() {
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
  var resultJson = jsonDecode(json);
  print(resultJson["permissions"]);
}