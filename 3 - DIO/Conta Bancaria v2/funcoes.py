#Seção de Importações

from datetime import datetime, timedelta
import random

hora_para_novas_transacoes = datetime.now() + timedelta(days=1)

usuarios = [{
          "40123":[{"INFORMACOES_PESSOAIS":[{
               "NOME":"Samuel",
               "CPF":"1234567",
               "DATA_DE_NASCIMENTO":"18/08/2000",
               "ENDERECO":"Rua da Patrias, n° 176, São Paulo",
               "NOME_DA_MAE":"Lindoia Meirelles"
                }],"INFORMACOES_DA_CONTA":[{
                     "CONTA":"40123",
                     "TIPO_DE_CONTA":"Corrente",
                     "AGENCIA":"2001",
                     "BANCO":"287",
                     "SALDO":[20],
                     "EXTRATO":[{'Valor': 20.00, 'Data': '02/11/2024, 15:33:45'}],
                     "LIMITE_SAQUE":[10],
                     "STATUS_DA_CONTA":"ATIVA"
                }]}]
     },{       "4123":[{"INFORMACOES_PESSOAIS":[{
               "NOME":"Samuel",
               "CPF":"1234567",
               "DATA_DE_NASCIMENTO":"18/08/2000",
               "ENDERECO":"Rua da Patrias, n° 176, São Paulo",
               "NOME_DA_MAE":"Lindoia Meirelles"
                }],"INFORMACOES_DA_CONTA":[{
                     "CONTA":"4123",
                     "TIPO_DE_CONTA":"Corrente",
                     "AGENCIA":"2001",
                     "BANCO":"287",
                     "SALDO":[10],
                     "EXTRATO":[{'Valor': 10.00, 'Data': '02/11/2024, 15:33:45'}],
                     "LIMITE_SAQUE":[10],
                     "STATUS_DA_CONTA":"ATIVA"
                }]}]}]
# Funções

contas_geradas = set()
indices_das_contas = [{"40123":0}, {"4123":1}]
quantidade_de_contas = [2]

def gerar_numero_da_conta():
    while True:
        numero_conta = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        if numero_conta not in contas_geradas:
            contas_geradas.add(numero_conta)
            return numero_conta
        
def gera_numero_da_agencia():
    return ''.join([str(random.randint(0, 9)) for _ in range(4)])

def cadastrar_usuario(banco_de_dados:list, cpf:str, nome:str, data_de_nascimento:str, endereco:str, nome_da_mae:str, tipo_conta:str, saldo:float):
    conta = gerar_numero_da_conta()
    agencia = gera_numero_da_agencia()
    usuario = {
        conta:[{"INFORMACOES_PESSOAIS":[{
                "NOME":nome,
                "CPF":cpf,
                "DATA_DE_NASCIMENTO":data_de_nascimento,
                "ENDERECO":endereco,
                "NOME_DA_MÃE":nome_da_mae
                    }],"INFORMACOES_DA_CONTA":[{
                        "CONTA":conta,
                        "TIPO_DE_CONTA":tipo_conta,
                        "AGENCIA":agencia,
                        "BANCO":"Banco Campos",
                        "SALDO":[saldo],
                        "EXTRATO":[],
                        "LIMITE_SAQUE":[10],
                        "STATUS_DA_CONTA":"ATIVA"
                    }]}]
        }
    indice = quantidade_de_contas[0]
    nova_conta = {
        conta: indice
    }
    banco_de_dados.append(usuario)
    indices_das_contas.append(nova_conta)
    indice = quantidade_de_contas[0] + 1
    quantidade_de_contas[0] = indice
    return f"""
    
\nSeguem os dados da conta cadastrada:

---- INFORMACOES PESSOAIS ----

NOME: {nome}
CPF: {cpf}
DATA DE NASCIMENTO: {data_de_nascimento}
ENDEREÇO: {endereco}
NOME DA MÃE: {nome_da_mae}

---- INFORMACOES DA CONTA ----

CONTA: {conta}
TIPO DE CONTA: {tipo_conta}
AGÊNCIA: {agencia}
BANCO: Banco Campos
SALDO: R$ {saldo:.2f}
STATUS DA CONTA: ATIVA
\n
"""

def pesquisar_indice(banco_de_dados:list, conta:str):
    tg = 1
    for indice in range(0, quantidade_de_contas[0]):
        usuario = banco_de_dados[indice]
        if conta in usuario:
            usuario[conta]
            tg =- 1
            return indice
    if tg == 0:
        return -1

class Operacoes:
    def __init__(self, banco_de_dados:list, conta:str, indice:int, valor:float):
        self.__banco_de_dados = banco_de_dados
        self.__conta = conta
        self.indice = indice
        self.__valor = valor

    def deposito(self):
        saldo = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["SALDO"][0]
        extrato = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["EXTRATO"]

        saldo += self.__valor
        self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["SALDO"][0] = saldo

        depositar =  {"Valor":self.__valor,
                  "Data":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                  }
        extrato.append(depositar)
        return f"\nO valor de R$ {self.__valor:.2f} foi adicionado a conta {self.__conta}"
    
    def saque(self):
        saldo = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["SALDO"][0]
        extrato = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["EXTRATO"]
        limite_saque = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["LIMITE_SAQUE"][0]

        if saldo == 0:
            return f"Seu saldo é de R$ {saldo:.2f} depósite algum valor para continuar com a operação."
        elif limite_saque == 0:
            return f"Infelizmente você não poderá realizar nenhuma operação de saque hoje, tente novamente amanhã {hora_para_novas_transacoes}."
        elif saldo >= self.__valor and limite_saque != 0:
            saldo -= self.__valor
            self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["SALDO"][0] = saldo
            valor_de_saque = self.__valor - (self.__valor * 2)

            saque =  {"Valor":valor_de_saque,
                    "Data":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                    }
            extrato.append(saque)
            limite_saque -= 1
            limite_saque = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["LIMITE_SAQUE"][0] = limite_saque
            return f"\nO valor de R$ {self.__valor:.2f} foi retirado da conta {self.__conta}, você ainda tem mais {limite_saque} saques disponível hoje."
        elif saldo > 0 and saldo < self.__valor and limite_saque != 0:
            return f"Infelimente seu saldo é menor do que o valor que deseja sacar, depósite um valor a conta ou saque um valor menor ou igual ao que tem.\nSeu saldo é de R$ {saldo:.2f}"
    
    def tirar_extrato(self):
        saldo = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["SALDO"][0]
        extrato = self.__banco_de_dados[self.indice][self.__conta][0]["INFORMACOES_DA_CONTA"][0]["EXTRATO"]

        data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
 
        if len(extrato) > 0:
            print("\n========================= EXTRATO =========================\n")
            for informacoes_extrato in range(0, len(extrato)):
                valor_em_analise = extrato[informacoes_extrato]["Valor"]
                data_em_analise = extrato[informacoes_extrato]["Data"]
                if valor_em_analise > 0:
                    print(f"Valor Depósitado R$ {valor_em_analise:.2f} ({data_em_analise})")
                elif valor_em_analise < 0:
                    print(f"Valor Sacado R$ {valor_em_analise:.2f} ({data_em_analise})")
            return f"\nSaldo Atual R$ {saldo:.2f} - {data_atual}\n"
        else:
            return f"Você não fez nenhuma movimentação em sua conta.\n"