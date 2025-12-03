📒 Agenda de Contatos — Python (Modo Terminal)

Este projeto é uma agenda simples de contatos feita em Python, executada diretamente no terminal.
O objetivo é praticar:

Estruturas de dados (listas e dicionários)

Funções

Manipulação de terminal (os.system("cls"))

Estrutura de menus

Lógica de CRUD (mesmo que incompleto por enquanto)

🎯 Funcionalidades Atuais

No estado atual do projeto, já foi implementado:

✔ 1. Adicionar Contato

O usuário informa nome e telefone

Os dados são armazenados como dicionário dentro de uma lista

contato = {
    "nome": "...",
    "telefone": 00000000
}

✔ 2. Listar Todos os Contatos

Mostra todos os contatos cadastrados no formato:

Nome -> Telefone

✔ 3. Menu Interativo

Interface pelo terminal

Limpa a tela automaticamente

Aguarda tecla para voltar ao menu

🚧 Funcionalidades Pendentes (a implementar)

❌ Remover contatos

❌ Buscar contatos

❌ Verificação de erros (nome vazio, telefone inválido, etc.)

❌ Salvar contatos em arquivo

Você poderá implementá-las ao longo dos próximos desafios.

📁 Estrutura Atual do Código
import os

def adicionar_contatos(lista_contatos):
    ...

def listar_contato(lista_Contatos):
    ...

def perguntar_e_limpar():
    ...

def remover_contato(lista_Contatos):
    pass

def buscar_contato(lista_Contatos):
    pass

▶ Como Executar

Instale o Python 3+

Salve o arquivo como agenda.py

Execute:

python agenda.py

🧠 Objetivo do Desafio

Esse projeto faz parte do Desafio 1 – Agenda Simples, do seu cronograma de estudo.
Ele tem como finalidade treinar:

Manipulação de listas

Dicionários

Funções

Lógica de menus

CRUD básico

Depois de completar essa versão simples, você poderá evoluir para:

✔ Busca inteligente
✔ Remoção por nome
✔ Salvar em arquivo (JSON)
✔ Ordenação alfabética
✔ Interface mais limpa

💡 Próximos Passos Sugeridos

Implementar a função remover_contato

Implementar buscar_contato

Evitar números repetidos

Transformar em classe futuramente (POO)