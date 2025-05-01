import pytest
import re

@pytest.mark.parametrize("data, esperado", [
    ("Vencimento: 10/04/2025","10/04/2025"),
    ("Vencimento: 14.04.2025","14/04/2025"),
    ("Vencimento da fatura dia 10/02/25","10/02/2025"),
])

def test_vencimento(data, esperado):
    padrao = r"Vencimento.*?(\d{1,2}[./]\d{1,2}[./]\d{2,4})"
    resultado = re.search(padrao, data)
    if resultado:
        vencimento = resultado.group(1).replace(".", "/")
        partes = vencimento.split("/")
        if len(partes[2]) == 2:
            partes[2] = "20" + partes[2]
            vencimento = "/".join(partes)
    else:  
        vencimento = None
    assert vencimento == esperado