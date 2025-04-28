import os
import csv
from pathlib import Path
from services.xmlService import extractDataXML
# from services.pdfService import extractDataPDF, extractDataNotaPDF
from services.proofService import parseProofPDF
from services.notesService import parseNotesPDF
from classes.fornecedor import loadSuppliers

pathFolder = r".\20250404"

produtosFornecedor = loadSuppliers()
csvData = []

for subFolder in os.listdir(pathFolder):
    subfolder_path = os.path.join(pathFolder, subFolder)
    notaXML = False

    for file in sorted(os.listdir(subfolder_path)):
        filePath = os.path.join(subfolder_path, file)
        
        if file.endswith(".xml"):
            nota = extractDataXML(filePath, produtosFornecedor)    
            notaXML = True

        if file.endswith(".pdf") and not "CNDS" in filePath.upper():            
            comp = parseProofPDF(filePath)
            if not notaXML:
                nota = parseNotesPDF(filePath, produtosFornecedor)

            #   if nota is None:
            #     print(f"⚠️ Não foi possível extrair a nota do PDF: {file_path}")
            #     continue
            #   print(f"nota: {nota.nNota}")

    csvData.append({
        "DataEmissao": nota.emissao.strftime("%d/%m/%Y"),
        "NumeroDocumento": nota.nNota,
        "ValorDespesa": comp.vPagamento,
        "CodigoCargo": "", 
        "CpfProfissional": "",
        "NomeProfissional": "",
        "CodigoDespesa": nota.maiorGrupo[0],
        "NumeroParcelas": 1,
        "DataVencimento": nota.dVenc.strftime("%d/%m/%Y"),
        "CodigoFornecedor": nota.codFornecedor,
        "NumeroContrato": "001/2023",
        "CodigoUnidade": "0102105E",
        "CodigoServico": "0100",
        "NumeroProfissionais": "0",
        "NumeroDocumentoPagamento": comp.nDocumento,
        "DataPagamento": comp.dataPagto.strftime("%d/%m/%Y"),
        "CodigoBancario": comp.codBanco,
        "CodigoFonteRecurso": "00",
        "Comentario": ""
    })    

header = [
    "DataEmissao", "NumeroDocumento", "ValorDespesa", "CodigoCargo",
    "CpfProfissional", "NomeProfissional", "CodigoDespesa", "NumeroParcelas",
    "DataVencimento", "CodigoFornecedor", "NumeroContrato", "CodigoUnidade",
    "CodigoServico", "NumeroProfissionais", "NumeroDocumentoPagamento",
    "DataPagamento", "CodigoBancario", "CodigoFonteRecurso", "Comentario"
]
    
with open ("cargaWebSAASS.csv", mode='w', newline="", encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=';', extrasaction='ignore')
    writer.writeheader() #escreve o cabeçalho no arquivo CSV
    for item in csvData:
        writer.writerow(item)      
