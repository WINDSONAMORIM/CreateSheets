import pytest
import re

@pytest.mark.parametrize("data, esperado", [
    ("Vl. Líquido da Nota Fiscal R$ 180.505,09","180505,09"),
    ("VALOR LÍQUIDO DA NOTA R$ 180.505,09", "180505,09"),
    ("Valor Líquido da NFS-e: R$ 20.000,00", "20000,00"),
])

def test_valorNota(data, esperado):
    padrao = r"(?:Vl\.?|Valor)\s+L[ÍI]QUIDO DA (?:NOTA\.?|NFS-e).*?(\d{1,3}(?:\.\d{3})*,\d{2})"
    resultado = re.search(padrao, data, re.IGNORECASE)
    if resultado:
        valor = resultado.group(1).replace(".", "")
    else:  
        valor = None
    assert valor == esperado