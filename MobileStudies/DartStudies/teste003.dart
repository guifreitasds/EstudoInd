void main(){
  Pagamento pagamento = PagamentocomPix();
  pagamento.pagar();

  pagamento = PagamentocomCartao();
  pagamento.pagar();

  pagamento = PagamentoDebito();
  pagamento.pagar();
}

abstract class Pagamento{
  void pagar();
}

class PagamentocomPix implements Pagamento{
  void pagar(){
    print("Pagando com pix...");
  }
}

class PagamentocomCartao implements Pagamento{
  void pagar(){
    print("Pagando com cartão...");
  }
}

class PagamentoDebito implements PagamentocomCartao{
  void pagar(){
    print("Pagando com cartão, no débito...");
  }
}