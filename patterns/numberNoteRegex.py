import re

class NumberNoteRegex:
    def __init__(self, line:str):
         self.line = line   

    @property
    def matchNumberNoteInline(self):
        match = re.search(r'N[ÚU]MERO DA (?:NOTA\.?|NFS-e)[^0-9]*?(\d+)', self.line, re.IGNORECASE)
        return match.group(1) if match else None

    @property
    def matchDescribeNoteFotterInline(self):
        match = re.search(r'NOTA FISCAL ELETRÔNICA DE SERVIÇOS\s+(\d{6})', self.line, re.IGNORECASE)
        return match.group(1) if match else None     
    
    # @property
    # def matchDescribeNoteFotter(self):
    #     match = re.search(r'NOTA FISCAL ELETRÔNICA DE SERVIÇOS[^0-9]*?', self.line, re.IGNORECASE)
    #     return match.group(0) if match else None
    
    @property
    def matchDescribeNote(self):
        match = re.search(r'N[ÚU]MERO DA (?:NOTA\.?|NFS-e)[^0-9]*?', self.line, re.IGNORECASE)
        return match.group(0) if match else None

    # @property
    # def matchNumberFooter(self):
    #     match = re.search(r'\d{6}', self.line)
    #     return match.group(0) if match else None
    
    @property 
    def matchNumberNote(self):
        match = re.search(r'(\d+)', self.line)
        return match.group(0) if match else None