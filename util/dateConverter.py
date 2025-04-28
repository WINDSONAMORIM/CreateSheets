from datetime import datetime, timedelta

def dateConverter(data: str) -> datetime | None:
    formatos = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%Y%m%d", "%d/%m/%y", "%d-%m-%y", "%Y-%m-%dT%H:%M:%S", "%Y%m%dT%H:%M:%S"]
    data = data.strip()
    for formato in formatos:
        try:
            return datetime.strptime(data, formato)
        except ValueError:
            continue
    #verifica se o formato da data possui T 2025-04-12'T'14:30:00
    if "T" in data:
        try:
            return datetime.strptime(data[:10], "%Y-%m-%d")
        except Exception as e:
            print(f"[ERRO] Falha ao converter data: '{data}' → {e}")
            return None
        
    print(f"[ERRO] Nenhum formato válido para data: '{data}'")
    return None    
    
def dateDDL(term:str, date: datetime) -> datetime | None:
    try:
       days = int(term.group(1))
       return date + timedelta(days=days)
    except:
        return None