import re
import pdfplumber
from classes.notaXML import NotaXML
from util.dateConverter import dateConverter
from patterns.notesRegex import NotesRegex

import logging
logging.getLogger("pdfminer").setLevel(logging.ERROR)

def parseNotesPDF(filePDFPath, produtosFornecedor: list):
    print('Nota PDF')
    print(filePDFPath)

    emissao = None
    nNota=""
    valorTotalNF=""
    dVenc=""
    cnpj=""
    maiorGrupo=[0,0]
    codFornecedor=""

    with pdfplumber.open(filePDFPath) as pdf:
        for page in pdf.pages:
            lines = page.extract_text().split('\n')

            for i, line in enumerate(lines):
                lineUpper = line.upper()

                if not emissao:
                    emissao = NotesRegex(lineUpper).matchEmissaoInline
                    
                if not emissao and NotesRegex(lineUpper).matchEmissao and i + 1 < len(lines):
                    nextLine = lines[i + 1].upper()
                    emissao = NotesRegex(nextLine).matchEmissaoDate
                    

                if not nNota:
                    nNota = NotesRegex(lineUpper).matchNotaInline

                if not nNota and NotesRegex(lineUpper).matchNota and i + 1 < len(lines):
                        nextLine = lines[i + 1].upper() 
                        nNota = NotesRegex(nextLine).matchNumeroNota

                if not valorTotalNF:
                    valorTotalNF = NotesRegex(lineUpper).matchValorNotaInline

                if not valorTotalNF and NotesRegex(lineUpper).matchValorNota and i + 1 < len(lines):
                    nextLine = lines[i + 1].upper()
                    valorTotalNF = NotesRegex(nextLine).matchValor   

                if not dVenc:
                    dVenc = NotesRegex(lineUpper).matchVencimentoInline
                    
                if not dVenc and NotesRegex(lineUpper).matchVencimento and i + 1 < len(lines):
                    nextLine = lines[i + 1].upper()
                    dVenc = NotesRegex(nextLine).matchVencimentoDate

                if not cnpj:
                    cnpj = NotesRegex(lineUpper).matchCNPJInline

                if not cnpj and NotesRegex(lineUpper).matchCNPJ and i + 1 < len(lines):
                    nextLine = lines[i + 1].upper()
                    cnpj = NotesRegex(nextLine).matchCNPJ 

    for cnpjFornecedor in produtosFornecedor:
        if cnpjFornecedor.cnpj == cnpj:
            codFornecedor = cnpjFornecedor.codigo

    if not codFornecedor:
        print(f"Fornecedor não encontrado: {cnpj}")        

    emissao = dateConverter(emissao)
    dVenc = dateConverter(dVenc)

    print("Data de Emissão:", emissao)            
    print("Número da Nota:", nNota)
    print("Valor da Nota:", valorTotalNF)
    print("Data de Vencimento:", dVenc)
    print("CNPJ:", cnpj)
    print("Maior Grupo:", maiorGrupo)
    print("Código do Fornecedor:", codFornecedor)

    return NotaXML(emissao, nNota, valorTotalNF, dVenc, cnpj, maiorGrupo, codFornecedor)