import pytest
import re

@pytest.mark.parametrize("data, esperado", [
    # ("NÚMERO DA NOTA 15","15"),
    # ("NÚMERO DA NOTA: 18", "18"), 
    # ("Número da NFS-e - 20","20"),
    ('NOTA FISCAL ELETRÔNICA DE SERVIÇOS 000030', '000030'),
])

def test_nNota(data, esperado):
    # padrao = r'N[ÚU]MERO DA (?:NOTA\.?|NFS-e)[^0-9]*?(\d+)'
    padrao =r'NOTA FISCAL ELETRÔNICA DE SERVIÇOS\s+(\d{6})'
    resultado = re.search(padrao, data, re.IGNORECASE)
    if resultado:
        nNota = resultado.group(1)
    else:  
        nNota = None
    assert nNota == esperado