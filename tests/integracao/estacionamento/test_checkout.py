from app.estacionamento.checkout import emitir_ticket_saida


def test_integracao_ticket_saida_carro():
    resultado = emitir_ticket_saida(
        placa="12345",
        horas=3,
        tipo_veiculo="carro",
        codigo_loja="mercado"
    )

    assert resultado["valido"] is True
    assert resultado["placa"] == resultado["placa"]
    assert resultado["tarifa_base"] == 22.0
    assert resultado["desconto_convenio"] == 4.40
    assert resultado["valor_a_pagar"] == 17.60


def test_integracao_ticket_saida_moto():
    resultado = emitir_ticket_saida(
        placa="ABCDE",
        horas=2,
        tipo_veiculo="moto",
        codigo_loja="FARMACIA"
    )

    assert resultado["valido"] is True
    assert resultado["placa"] == resultado["placa"]
    assert resultado["tarifa_base"] == 8.0
    assert resultado["desconto_convenio"] == 0.80
    assert resultado["valor_a_pagar"] == 7.20


def test_integracao_tipo_veiculo_invalido():
    resultado = emitir_ticket_saida(
        placa=54321,
        horas=2,
        tipo_veiculo="caminhao",
        codigo_loja="mercado"
    )

    assert resultado["valido"] is False
    assert resultado["valor_a_pagar"] == 0.0


def test_integracao_horas_zeradas():
    resultado = emitir_ticket_saida(
        placa="EDCBA",
        horas=-1,
        tipo_veiculo="carro",
        codigo_loja="farmacia"
    )

    assert resultado["valido"] is False
    assert resultado["valor_a_pagar"] == 0.0