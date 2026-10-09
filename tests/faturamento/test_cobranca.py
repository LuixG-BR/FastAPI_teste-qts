import pytest
import time

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_final",
    [
        (0, "BRONZE", 1, -1),
        (-25, "BRONZE", 2, -1),
        (100, "bronze", -1, -1),
        (100, "", 2, -2),
        (100, "OU RO", 0, -2),
        (100, "diamante", 3, -2),
        (100, "BRONZE", 0, 100),
        (100, "PRATA", 0, 85),
        (100, "ouro", 0, 75),
        (100, "BRONZE", 5, 110),
        (100, "pRata", 7, 95.38),
        (100, "OuRo", 9, 85.7),
        (100, "BronZe", 22, 147.6),
        (100, "prata", 21, 129.28),
        (100, "OURo", 27, 121.2)
    ]
)
def test_calcular_valor_final(valor_base, plano, dias_atraso, valor_final):
    assert processar_cobranca(valor_base, plano, dias_atraso) == valor_final


def test_tempo_processamento_cobranca():
    inicio = time.perf_counter()
    resultado = processar_cobranca(350, "OURO", 27)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado == 349.2
    assert tempo_decorrido < 0.8