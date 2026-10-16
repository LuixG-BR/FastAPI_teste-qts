import pytest
from app.estacionamento.checkout import calcular_tarifa_base


@pytest.mark.parametrize(
    "horas, tipo_veiculo, tarifa_esperada",
    [
        (1, "moto", 5.0),
        (3, "moto", 11.0),
        (1, "carro", 10.0),
        (4, "CARRO", 28.0),
        (5, "barco", -1.0),
        (0, "moto", 0.0),
    ]
)
def test_calcular_tarifas(horas, tipo_veiculo, tarifa_esperada):
    resultado = calcular_tarifa_base(horas, tipo_veiculo)
    assert resultado == tarifa_esperada