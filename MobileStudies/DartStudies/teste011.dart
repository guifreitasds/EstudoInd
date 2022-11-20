void main() {
  var pagamento = Pagamento();
  pagamento.pagando(PagamentoRestrito.PIX);
}

enum PagamentoRestrito{
  PIX('Pix'),
  CARTAO('Cartao'),
  BOLETO('Boleto');

  final String value;

  const PagamentoRestrito(this.value);
}


class Pagamento{

  void pagando(PagamentoRestrito pague){
    if(pague.value=='Pix'){
      print('Pagando com pix...');
    } else if (pague.value=='Boleto'){
      print('Pagando com boleto...');
    } else if (pague.value=='Cartao'){
      print('Pagando com cartão');
    }
  }
}
