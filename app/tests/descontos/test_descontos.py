from app.descontos.descontos import calcular_desconto

# Cliente VIP com valor invalido
def test_valor_abaixo_de_zero():
    assert calcular_desconto(-1,True) == "Valor Invalido"
def test_valor_zero():
    assert calcular_desconto(0, True) == "Valor Invalido"

# Cliente não VIP com valor valido
def test_valor_valido_sem_clienteVIP():
    assert calcular_desconto(100, False) == 90
def test_valor_valido_com_clienteVIP():
    assert calcular_desconto(100, True) == 80
    
# Valores muito alto ou muito baixo
def test_valor_proximo_de_zero():
    assert calcular_desconto(0.01, True) == 0.008
def test_valor_alto():
    assert calcular_desconto(1500, False) == 1350