import re
from datetime import datetime
from classes.comprovante import Comprovante
from pdfminer.high_level import extract_text
from util.dateConverter import dateConverter

#Limpa terminal de logs do pdfminer
import logging
logging.getLogger("pdfminer").setLevel(logging.ERROR)

def checkCNDS(filePath) -> bool:
    if "CNDS" in filePath.upper():
        return "CNDS" not in filePath.upper()

def extractDataPDF(filePath):
    if checkCNDS(filePath):
        print(f"Arquivo CNDS Pular arquivo")
        return None
    
    fullText = extract_text(filePath, page_numbers=[0, 1])
    pages = fullText.split('\f')

    dataComprovante = datetime.now()
    documento = ""
    valorComprovante = ""
    codBanco = 0

    # Remove a última página se estiver vazia
    if pages and pages[-1].strip() == '':
        pages.pop()

    if "COMPROVANTE" in pages[0].upper():
        firstPage = pages[0].upper()

        matchDataTransferencia = re.search(r"DATA DA TRANSFERENCIA[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", firstPage)
        matchDataDebito = re.search(r"DEBITO EM[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", firstPage)
        matchDataPagamento = re.search(r"DATA DO PAGAMENTO[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", firstPage)

        #tratar apenas 550.712.000.085.393
        matchDocumentoTransferencia = re.findall(r"DOCUMENTO[^\d]*(\d{3}(?:\.\d{3})+)", firstPage)
        #tratar apenas 040401
        matchDocumentoDebito = re.search(r"DOCUMENTO[^\d]*(\d{6})", firstPage)
        #tratar apenas 40.112
        matchDocumentoPagmento = re.search(r"DOCUMENTO[^\d]*(\d{2}\.\d{3})", firstPage)

        #tratar apenas VALOR TOTAL 943,85
        matchValorTransferencia = re.search(r"VALOR TOTAL[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", firstPage)
        #tratar apenas VALOR: R$ 13.786,20
        matchValorDebito = re.search(r"VALOR[:\s]*R?\$?[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", firstPage)
        #tratar apenas VALOR COBRADO 450,00
        matchValorPagamento = re.search(r"VALOR COBRADO[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", firstPage)

        if matchDataTransferencia:
            dataComprovante = dateConverter(matchDataTransferencia.group(1))
            documento = matchDocumentoTransferencia[-1]
            valorComprovante = matchValorTransferencia.group(1)
            codBanco="470"
        
        if matchDataDebito:
            dataComprovante = dateConverter(matchDataDebito.group(1))
            documento = matchDocumentoDebito.group(1)
            valorComprovante = matchValorDebito.group(1)
            codBanco="393"

        if matchDataPagamento:
            dataComprovante = dateConverter(matchDataPagamento.group(1))
            documento = matchDocumentoPagmento.group(1)
            valorComprovante = matchValorPagamento.group(1)
            codBanco="109"

    return Comprovante(dataComprovante, valorComprovante, codBanco, documento)        