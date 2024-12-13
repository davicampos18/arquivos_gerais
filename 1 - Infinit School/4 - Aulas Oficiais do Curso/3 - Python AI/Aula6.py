# Criar um programa para gerenciar tarefas diárias, com nome, descrição, prioridade e categoria
from tabulate import tabulate
import os, time

banco_de_tarefas = []
geracao_id = 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_tarefas(id, nome_da_tarefa, descricao, categoria, prioridade, banco_de_dados:list):
    banco_de_dados.append({
        "ID":id,
        "Tarefa":nome_da_tarefa,
        "Descrição":descricao,
        "Categoria":categoria,
        "Prioridade":prioridade,
        "Status":False
    })

    print("Tarefa Cadsatrada com Sucesso!")


def localizar_tarefa(id:int, banco_de_dados:list):
    tarefa = banco_de_dados[id - 1]
    print(f"Tarefa: {tarefa["Tarefa"]}\nDescrição: {tarefa["Descrição"]}\nCategoria: {tarefa["Categoria"]}\nPrioridade: {tarefa["Prioridade"]}\nStatus: {"Em andamento" if tarefa["Status"] == False else "Concluído"}")

def excluir_tarfa(id:int, banco_de_dados:list):
    banco_de_dados.pop(id - 1)
    print("Tarefa Excluída com Sucesso!")

limpar_tela()
while True:
    print("""
==================== Lista de Tarefas ====================         

       Digite uma das opções abaixo para prosseguir

1 - Cadastrar Tarefa
2 - Editar Tarefa
3 - Excluir Tarefa
4 - Listar Tarefas
5 - Encerrar Aplicação
""")
    opcao = int(input("==> "))
    print("==========================================================\n")
    match opcao:
        case 1:
            limpar_tela()
            print("=================== Cadastro de Tarefas ==================\n")
            id_cad = geracao_id
            nome_cad = input("Digite o nome da tarefa: ")
            descricao_cad = input("Digite a descrição: ")
            categoria = input("Qual a categoria da tarefa: ")
            print("Selecione o tipo de prioridade:\n1 - Alta\n2 - Média\n3 - Baixa\n")
            prioridade_cad = int(input())
            match prioridade_cad:
                case 1:
                    prioridade_cad = "Alta"
                case 2:
                    prioridade_cad = "Média"
                case 3:
                    prioridade_cad = "Baixa"
            criar_tarefas(id_cad, nome_cad, descricao_cad, categoria, prioridade_cad, banco_de_tarefas)
            geracao_id += 1
            time.sleep(2)
            limpar_tela()
            time.sleep(1)
        case 2:
            limpar_tela()
            print(tabulate(banco_de_tarefas, headers="keys", tablefmt="grid"))
            escolha = int(input("Qual o ID da tarefa que deseja editar? "))
            localizar_tarefa(escolha, banco_de_tarefas)
            time.sleep(1)
            limpar_tela()
        case 3:
            limpar_tela()
            print(tabulate(banco_de_tarefas, headers="keys", tablefmt="grid"))
            escolha = int(input("Qual o ID da tarefa que deseja excluir? "))
            excluir_tarfa(escolha, banco_de_tarefas)
            time.sleep(2)
            limpar_tela()
        case 4:
            limpar_tela()
            print(tabulate(banco_de_tarefas, headers="keys", tablefmt="grid"))
        case 5:
            limpar_tela()
            break

