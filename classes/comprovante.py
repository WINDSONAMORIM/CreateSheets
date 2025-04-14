from datetime import datetime

class Comprovante:
    def __init__(self, dataPagto: datetime = None, vPagamento: str = "", codBanco: str = "", nDocumento: str = ""):
        self.dataPagto = dataPagto
        self.vPagamento = vPagamento
        self.codBanco = codBanco
        self.nDocumento = nDocumento
        
          