# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Preço Original: R$').strip())
cupom = input('Código de Cupom:').strip()

if cupom in descontos:
    percentual = descontos[cupom]
    desconto = preco*percentual
    preco_final = preco-desconto
    print(f'Valor de Desconto: R${desconto:.2f}')
    print(f'Valor a pagar: R${preco_final:.2f}')

else:
    print('Código informado é inválido')
# TODO: Aplique o desconto se o cupom for válido: