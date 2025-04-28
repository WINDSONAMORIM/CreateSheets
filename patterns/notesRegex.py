import re

class NotesRegex:
        def __init__(self, line:str):
            self.line = line

        @property
        def matchEmissao(self):
            match = re.search(r'EMISS[AÃ]O', self.line)
            return match.group(0) if match else None    

        @property
        def matchEmissaoDate(self):
            match = re.search(r'\d{2}/\d{2}/\d{4}', self.line)
            return match.group(0) if match else None

        @property
        def matchEmissaoInline(self):
            match = re.search(r'EMISS[AÃ]O\s*\d{2}/\d{2}/\d{4}', self.line)
            return match.group(0) if match else None  
        
        @property
        def matchNota(self):
            match = re.search(r'N[ÚU]MERO DA NOTA', self.line)
            return match.group(0) if match else None
        
        @property 
        def matchNumeroNota(self):
            match = re.search(r'(\d{6,})', self.line)
            return match.group(0) if match else None

        @property
        def matchNotaInline(self):
            match = re.search(r'N[ÚU]MERO DA NOTA\s*\d{6,}', self.line)
            return match.group(0) if match else None

        @property
        def matchValorNotaInline(self):
            match = re.search(r'VALOR L[ÍI]QUIDO DA NOTA\s*\d{1,3}(?:\.\d{3})*,\d{2}', self.line)
            return match.group(0) if match else None    

        @property
        def matchValorNota(self):
            match = re.search(r'VALOR L[ÍI]QUIDO DA NOTA', self.line)
            return match.group(0) if match else None

        @property
        def matchValor(self):
            match = re.search(r'\d{1,3}(?:\.\d{3})*,\d{2}', self.line)
            return match.group(0) if match else None

        @property
        def matchVencimento(self):
            match = re.search(r'VENCIMENTO(?:\s+\w+)*', self.line)
            return match.group(0) if match else None    

        @property
        def matchVencimentoDate(self):
            match = re.search(r'\d{2}/\d{2}/\d{2,4}', self.line)
            return match.group(0) if match else None

        @property
        def matchVencimentoInline(self):
            match = re.search(r'VENCIMENTO(?:\s+\w+)*\s+\w*\s*(\d{2}[/-]\d{2}[/-]\d{2,4})', self.line)
            return match.group(1) if match else None  
        
        @property
        def matchCNPJ(self):
            match = re.search(r'(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})', self.line)
            return match.group(0) if match else None
        
        @property
        def matchCNPJInline(self):
            match = re.search(r'CPF/CNPJ[:\s]*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})', self.line)
            return match.group(1) if match else None 