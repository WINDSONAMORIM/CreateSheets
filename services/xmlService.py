import re
import xmltodict
from classes.notaXML import NotaXML
from collections import defaultdict
from util.dateConverter import dateDDL, dateConverter
from datetime import datetime, timedelta

def extractDataXML(filePath: str, produtosFornecedor: list):

    with open(filePath, "rb") as xmlNota: #abrir o xml
        nota = xmltodict.parse(xmlNota)

    infNFe = nota.get("nfeProc",{}).get("NFe",{}).get("infNFe",{})

    notaEmissao = infNFe.get("ide",{}).get("dhEmi", {}) 
    emissao = dateConverter(notaEmissao) #converter a data de emissão para datetime

    nNota = infNFe.get("ide",{}).get("nNF", {})   
    cnpj = infNFe.get("emit",{}).get("CNPJ",{})
    valorTotalNF = infNFe.get("total", {}).get("ICMSTot",{}).get("vNF",{})

    dVenc = None

    cobr = infNFe.get("cobr")
    if cobr:
        dup = cobr.get("dup")
        if dup:
            if isinstance(dup, list):
                dVenc = dateConverter(dup[0].get("dVenc"))
            else:
                dVenc = dateConverter(dup.get("dVenc"))

    if not dVenc:
        infAdic = infNFe.get("infAdic", {})
        infCpl = infAdic.get("infCpl", {})

        match = re.search(r"(\d{1,3})\s*(?:dias|ddl)", infCpl, re.IGNORECASE)
        if match and emissao:
            dVenc = dateDDL(match, emissao)

    det = infNFe.get("det",{})

    for cnpjFornecedor in produtosFornecedor:
        if cnpjFornecedor.cnpj == cnpj:
            codFornecedor = cnpjFornecedor.codigo
        else:
            ()        

    # Garante que sempre será uma lista
    if isinstance(det, dict):
        det = [det]

    valorPorGrupo = defaultdict(float)    

    for item in det:
        prod = item.get("prod")
        if prod:
            codigo = prod.get("cProd")
            descricao = prod.get("xProd")
            valor = float(prod.get("vProd"))

            for produtos in produtosFornecedor:
                for cod in produtos.produtos:
                    if cod.codigo == codigo:
                        valorPorGrupo[cod.grupo] += valor
        else:
            print(f"Item {item.get('@nItem', '?')} sem tag <prod>")

    maiorGrupo = max(valorPorGrupo.items(), key=lambda x: x[1])
    
    return NotaXML(emissao, nNota, valorTotalNF, dVenc, cnpj, maiorGrupo, codFornecedor)