import pytest
from app.estacionamento.convenio import calcular_desconto_convenio

@pytest.mark.parametrize(
    "valor_bruto, codigo_loja, desconto_esperado",
    [
        (50.0, "MERCADO", 10.0),
        (40.0, "farmacia", 4.0),
        (30.0, "LANHOUSE", 0.0),
        (0.0, "mercado", 0.0),
    ]
)
def test_calcular_desconto_convenio(valor_bruto, codigo_loja, desconto_esperado):
    resultado = calcular_desconto_convenio(valor_bruto, codigo_loja)
    assert resultado == desconto_esperado