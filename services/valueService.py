import re
from patterns.valuesRegex import ValuesRegex

exampleHeader = [
    "PIS", "COFINS", "INSS", "IRRF", "CSLL", 
    "OUTRAS RETENÇÕES", 
    "VL. ISSQN RETIDO", 
    "VL. LÍQUIDO DA NOTA"
]

def extractValor(linCurrent, linNext):

    valor = ValuesRegex(linCurrent).matchValueNoteInline

    if valor:
        return valor
    
    header = ValuesRegex(linCurrent).matchDescribeValue

    if header:
        valores = ValuesRegex(linNext).matchArrayValueNote
        valores = [v.replace("R$", "").strip().replace(".", "") for v in valores]

        dados = dict(zip(exampleHeader, valores))

        valor = dados[header]

        print(f"Header: {header} - Valor: {valor}")
        if valor:
            return valor
    return None

