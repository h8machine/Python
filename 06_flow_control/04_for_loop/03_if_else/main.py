#send an email containing online order details (max. 3 attempts) for confirmed orders.

compra_confirmada = True
dados_compra = 'Compra no valor de R$15.50 e entrega confirmada.'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break
    else:
        print('Falha na compra')