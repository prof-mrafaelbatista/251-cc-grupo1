import csv
from os.path import exists

class Handler:
    def __init__(self, banco_de_dados):
        if exists(banco_de_dados):
            self.banco_de_dados = banco_de_dados
            self.bd_termos = []
            with open(self.banco_de_dados, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, quotechar='"', delimiter=',')
                for l in reader:
                    self.bd_termos.append(l)

    
    def escrever_bd(self):
        with open(self.banco_de_dados, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerows(self.bd_termos)
    
    def get_termos(self):
        return self.bd_termos
        

    def atualizar_bd(self):
        self.bd_termos = []
        with open(self.banco_de_dados, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, quotechar='"', delimiter=',')
            for l in reader:
                self.bd_termos.append(l)
        return self.bd_termos


    def adicionar_termo(self, termo, definicao):
        self.bd_termos.append([termo, definicao])
        self.escrever_bd()


    def remover_termo(self, index):
        if 0 <= index < len(self.bd_termos):
            self.bd_termos.pop(index)
        self.escrever_bd()


    def atualizar_termo(self, index, termo, definicao):
        with open(self.banco_de_dados, 'r', newline='', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile, quotechar='"', delimiter=','))
            if 0 <= index < len(reader):
                reader[index] = [termo, definicao]
        
        with open(self.banco_de_dados, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerows(reader)