import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, resultado_esperado",
    [
        (0, 123, True, "renda invalida"),
        (0, -1, True, "renda invalida"),
        (1, -1, False, "score invalido"),
        (18, 1100, False, "score invalido"),
        (18, 800, True, "reprovado"),
        (18, 350, False, "reprovado"),
        (18, 500, False, "aprovado padrao"),
        (18, 800, False, "aprovado premium")
    ]
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, resultado_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == resultado_esperado

# Passo 2 - testes de borda
@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, resultado_esperado",
    [
        (0, 123, True, "renda invalida"),
        (0.01, 123, True, "reprovado"),
        (0.01, 123, False, "reprovado"),
        (1500, -1, False, "score invalido"),
        (67, 0, False, "reprovado"),
        (67, 399, False, "reprovado"),
        (67, 400, False, "aprovado padrao"),
        (67, 699, False, "aprovado padrao"),
        (67, 700, False, "aprovado premium"),
        (67, 1000, False, "aprovado premium"),
        (67, 1001, False, "score invalido"),
    ]
)
def test_borda_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, resultado_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == resultado_esperado
