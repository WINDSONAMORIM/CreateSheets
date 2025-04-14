import os
import importlib.util
from classes.produto import Produto 

class Fornecedor:
    def __init__(self, cnpj, codigo, produtos = None):
        self.cnpj = cnpj
        self.codigo = codigo
        self.produtos = produtos if produtos else []

def loadSuppliers():
    listSuppliers = []

    for supplierFile in os.listdir("./fornecedores"):
        if supplierFile.endswith(".py"):
            path = os.path.join("fornecedores", supplierFile)
            nome_modulo = supplierFile[:-3]  # remove .py

            spec = importlib.util.spec_from_file_location(nome_modulo, path)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            # Adiciona o fornecedor definido no módulo à lista
            listSuppliers.append(modulo.fornecedor)
    return listSuppliers        

