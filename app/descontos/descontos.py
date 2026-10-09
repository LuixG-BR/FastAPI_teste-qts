def calcular_desconto(valor: float, cliente_vip: bool):
    if valor <= 0:
        return "Valor Invalido"
    if cliente_vip == True:
        return valor - (valor * 0.20)
    elif cliente_vip == False:
        return valor - (valor * 0.10) 