# Preço da viagem

trip = float(input('Digite a quilometragem da viagem: '))

if trip <= 200:
    print(f'O valor total da viagem foi R${trip*0.5}')
else:
    print(f'O valor total da viagem foi R${trip*0.45}')
    