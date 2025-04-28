import re

class ProofRegex:
        def __init__(self, firstPage:str):
            self.firstPage = firstPage

        @property
        def matchDataTransferencia(self):
            match = re.search(r"DATA DA TRANSFERENCIA[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", self.firstPage)
            return match.group(1) if match else None
        
        @property
        def matchDataDebito(self):
            match = re.search(r"DEBITO EM[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", self.firstPage)
            return match.group(1) if match else None
        
        @property
        def matchDataPagamento(self):
            match = re.search(r"DATA DO PAGAMENTO[^\d]*(\d{2}[/-]\d{2}[/-]\d{4})", self.firstPage)
            return match.group(1) if match else None

        @property  #tratar apenas 550.712.000.085.393
        def matchDocumentoTransferencia(self):
            match = re.findall(r"DOCUMENTO[^\d]*(\d{3}(?:\.\d{3})+)", self.firstPage)
            return match[-1] if match else None
        
        @property #tratar apenas 040401
        def matchDocumentoDebito(self):
            match = re.search(r"DOCUMENTO[^\d]*(\d{6})", self.firstPage)
            return match.group(1) if match else None    

        @property #tratar apenas 40.112
        def matchDocumentoPagmento(self):
            match = re.search(r"DOCUMENTO[^\d]*(\d{2}\.\d{3})", self.firstPage)
            return match.group(1) if match else None  

        @property #tratar apenas VALOR TOTAL 943,85
        def matchValorTransferencia(self):
            match = re.search(r"VALOR TOTAL[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", self.firstPage)
            return match.group(1) if match else None    

        @property #tratar apenas VALOR: R$ 13.786,20
        def matchValorDebito(self):
            match = re.search(r"VALOR[:\s]*R?\$?[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", self.firstPage)
            return match.group(1) if match else None
    
        @property  #tratar apenas VALOR COBRADO 450,00
        def matchValorPagamento(self):
            match = re.search(r"VALOR COBRADO[^\d]*(\d{1,3}(?:\.\d{3})*,\d{2})", self.firstPage)
            return match.group(1) if match else None    