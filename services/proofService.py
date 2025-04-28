import re
from datetime import datetime
from util.dateConverter import dateDDL, dateConverter
from classes.comprovante import Comprovante
from classes.notaXML import NotaXML
from pdfminer.high_level import extract_text
from util.dateConverter import dateConverter
from patterns.proofRegex import ProofRegex

#Limpa terminal de logs do pdfminer
import logging
logging.getLogger("pdfminer").setLevel(logging.ERROR)

def parseProofPDF(filePath):
    print("Comprovante PDF")
    print(filePath)
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
        regex = ProofRegex(firstPage)

        if regex.matchDataTransferencia:
            dataComprovante = dateConverter(regex.matchDataTransferencia)
            documento = regex.matchDocumentoTransferencia
            valorComprovante = regex.matchValorTransferencia
            codBanco="470"
        
        if regex.matchDataDebito:
            dataComprovante = dateConverter(regex.matchDataDebito)
            documento = regex.matchDocumentoDebito
            valorComprovante = regex.matchValorDebito
            codBanco="393"

        if regex.matchDataPagamento:
            dataComprovante = dateConverter(regex.matchDataPagamento)
            documento = regex.matchDocumentoPagmento
            valorComprovante = regex.matchValorPagamento
            codBanco="109"

    return Comprovante(dataComprovante, valorComprovante, codBanco, documento)        

# def extractDataNotaPDF(filePath):
#     nNota = None

#     if "CNDS" in filePath.upper():
#         # print(f"Arquivo: {filePath} CNDS Pular arquivo")
#         return None
#     # print("teste passou do if CNDS")
    
#     fullText = extract_text(filePath, page_numbers=[0, 1])
#     pages = fullText.split('\f')

#     if not "COMPROVANTE" in pages[1].upper():
#         secondPage = pages[1].upper()
#         # print("Segunda página:", secondPage)

#     if "NÚMERO DA NOTA" in secondPage:
#         # Tenta encontrar o número da nota
#         print("Entrou no if NÚMERO DA NOTA")
#         matchNota = re.search(r"(\d{6,})\s*NÚMERO DA NOTA", secondPage)
#         if matchNota:
#             nNota = matchNota.group(1)
#             print("Número da nota encontrada:", nNota)
#         else:
#             print("Regex não encontrou o número da nota nesta linha.")   
#             print("Segunda página:", secondPage)   

#     # Quebra em linhas
#     linhas = secondPage.splitlines()

#     for linha in linhas:
#         if "EMISSÃO" in linha or "DATA E HORA DA EMISSÃO" in linha:
#             # Tenta encontrar a data e hora de emissão
#             matchEmissao = re.search(r"(\d{2}[\/-]\d{2}[\/-]\d{4})\s+ÀS\s+(\d{2}:\d{2})", linha)
#             if matchEmissao:
#                 data = matchEmissao.group(1)
#                 emissao = dateConverter(data)
#                 if emissao.day > 15:
#                     dia = 15
#                     mes = emissao.month + 1 if emissao.month < 12 else 1
#                     ano = emissao.year + 1 if emissao.month == 12 else emissao.year
#                 else:
#                     dia = 15
#                     mes = emissao.month
#                     ano = emissao.year
                
#                 dVenc = dateConverter(f"{dia}/{mes}/{ano}")
#             else:
#                 print("Regex não encontrou a data e hora nesta linha.")

          
        
#     # nNota=""
#     valorTotalNF=""
#     # dVenc=""
#     cnpj=""
#     maiorGrupo=[1,2]
#     codFornecedor=""    
    
#     return NotaXML(emissao, nNota, valorTotalNF, dVenc, cnpj, maiorGrupo, codFornecedor)