import re

class NotesRegex:
        def __init__(self, line:str):
            self.line = line

        @property
        def matchEmissao(self):
            match = re.search(r'EMISS[AÃ]O.*?', self.line, re.IGNORECASE)
            return match.group(0) if match else None    

        @property
        def matchEmissaoDate(self):
            match = re.search(r'\d{2}/\d{2}/\d{4}', self.line)
            return match.group(0) if match else None

        @property
        def matchEmissaoInline(self):
            match = re.search(r'EMISS[AÃ]O.*?(\d{1,2}[./]\d{1,2}[./]\d{2,4})', self.line, re.IGNORECASE)
            return match.group(0) if match else None  
        
        @property
        def matchNota(self):
            match = re.search(r'N[ÚU]MERO DA (?:NOTA\.?|NFS-e)[^0-9]*?', self.line, re.IGNORECASE)
            return match.group(0) if match else None
        
        @property 
        def matchNumeroNota(self):
            match = re.search(r'(\d+)', self.line)
            return match.group(0) if match else None

        @property
        def matchNotaInline(self):
            match = re.search(r'N[ÚU]MERO DA (?:NOTA\.?|NFS-e)[^0-9]*?(\d+)', self.line, re.IGNORECASE)
            return match.group(0) if match else None

        @property
        def matchVencimento(self):
            match = re.search(r'VENCIMENTO.*?', self.line, re.IGNORECASE)
            return match.group(0) if match else None    

        @property
        def matchVencimentoDate(self):
            match = re.search(r'\d{2}/\d{2}/\d{2,4}', self.line)
            return match.group(0) if match else None

        @property
        def matchVencimentoInline(self):
            match = re.search(r'VENCIMENTO.*?(\d{1,2}[./]\d{1,2}[./]\d{2,4})', self.line, re.IGNORECASE)
            return match.group(1) if match else None  
        
        @property
        def cleanCNPJ(self) -> str:
            return re.sub(r'\D','', self.line)
        
        @property
        def matchCNPJ(self):
            match = re.search(r'(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})', self.line)
            return match.group(0) if match else None
        
        @property
        def matchCNPJInline(self):
            match = re.search(r'CPF/CNPJ[:\s]*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})', self.line, re.IGNORECASE)
            return match.group(1) if match else None 
        