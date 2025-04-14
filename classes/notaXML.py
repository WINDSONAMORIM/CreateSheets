from datetime import datetime

class NotaXML:
    def __init__(self, emissao: datetime = None, nNota: str = "", valorTotalNF: float = 0, dVenc: datetime  = None, cnpj: str = "", maiorGrupo: str = "", codFornecedor: str = ""):
        self.emissao = emissao
        self.nNota = nNota
        self.valorTotalNF = valorTotalNF
        self.dVenc = dVenc
        self.cnpj = cnpj
        self.maiorGrupo = maiorGrupo
        self.codFornecedor = codFornecedor
          