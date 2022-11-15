void main(){
  Pagamento pagamento = PagamentocomPix();
  pagamento.pagar();

  pagamento = PagamentocomCartao();
  pagamento.pagar();

  pagamento = PagamentoDebito();
  pagamento.pagar();
}

abstract class Pagamento{ // Criação da classe abstrata, para usar subclasses que utilizam os seus métodos e atributos
  void pagar();
}

class PagamentocomPix implements Pagamento{
  void pagar(){
    print("Pagando com pix..."); // Mudança do método da classe abstrata e implementando funcionalidade da subclasse
  }
}

class PagamentocomCartao implements Pagamento{
  void pagar(){
    print("Pagando com cartão...");
  }
}

class PagamentoDebito implements PagamentocomCartao{ // Também é possível implementar classes normais em subclasses
  void pagar(){
    print("Pagando com cartão, no débito...");
  }
}