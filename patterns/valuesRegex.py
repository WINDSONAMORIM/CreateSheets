import re

class ValuesRegex:
    def __init__(self, line:str):
         self.line = line       

    @property
    def matchValueNoteInline(self):
        match = re.search(r"(?:Vl\.?|Valor)\s+L[ÍI]QUIDO DA NOTA.*?(\d{1,3}(?:\.\d{3})*,\d{2})", self.line, re.IGNORECASE)
        return match.group(0) if match else None    

    @property
    def matchDescribeValue(self):
        match = re.search(r"(?:Vl\.?|Valor)\s+L[ÍI]QUIDO DA NOTA.*?", self.line, re.IGNORECASE)
        return match.group(0) if match else None

    @property
    def matchValue(self):
        match = re.search(r'\d{1,3}(?:\.\d{3})*,\d{2}', self.line)
        return match.group(0) if match else None
    
    @property
    def matchArrayValueNote(self):
        match = re.findall(r'\d{1,3}(?:\.\d{3})*,\d{2}', self.line)
        return match if match else None