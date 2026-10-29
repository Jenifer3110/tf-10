
# MiniGit - Estrutura de Dados

## Apresentacao

Este projeto foi desenvolvido para colocar em pratica os conhecimentos de estruturas de dados utilizando Python.

O MiniGit simula algumas funcionalidades basicas do Git, trabalhando com commits, branches, historico e merge.

Foram utilizados dicionarios, listas, tuplas e filas para armazenar e consultar as informacoes.

## Funcionalidades

- Criar commits com identificadores automaticos.
- Consultar mensagens dos commits.
- Consultar os pais de cada commit.
- Criar e trocar branches.
- Realizar merge entre branches.
- Consultar o historico com log.
- Buscar palavras nas mensagens.
- Identificar commits de merge.
- Contabilizar os passos das operacoes.
- Validar nomes de branches antes da criacao.

## Estruturas de dados utilizadas

- **Dicionarios:** armazenam commits, mensagens e branches.
- **Listas:** armazenam os pais de cada commit.
- **Tuplas:** retornam os pais e os resultados das consultas sem permitir alteracoes na estrutura original.
- **Fila:** utilizada na consulta do historico com a operacao log.

## Tabela de medicao

| Quantidade de commits | Passos do commitar | Passos do log |
|---:|---:|---:|
| 10 | 2 | 10 |
| 100 | 2 | 100 |
| 1000 | 2 | 1000 |

## Respostas das questoes

**1. Qual a diferenca entre commitar e log em relacao ao custo?**

A operacao commitar possui custo constante, pois realiza uma quantidade fixa de operacoes para criar o commit e atualizar o ponteiro da branch. Ja a operacao log percorre os commits alcancaveis, fazendo com que seu custo aumente conforme a quantidade de commits.

**2. Qual a diferenca entre mensagem e buscar?**

A operacao mensagem consulta diretamente um commit pelo identificador, utilizando um dicionario. A operacao buscar percorre as mensagens ate encontrar o texto informado.

**3. Como funciona o merge?**

O merge cria um novo commit que possui dois pais, representando a uniao do historico de duas branches. Assim, o historico pode formar um grafo com diferentes caminhos.

**4. Por que utilizar tuplas na operacao pais?**

As tuplas permitem retornar os pais de um commit sem disponibilizar a lista interna para modificacoes externas, protegendo os dados do MiniGit.

## Testes e validacoes

Foram realizados testes para verificar:

- Criacao e consulta de commits.
- Criacao e troca de branches.
- Merge entre branches.
- Consulta do historico.
- Busca de mensagens.
- Identificacao de commits de merge.
- Tentativas de operacoes invalidas.
- Tentativa de criar uma branch com nome vazio.

Quando uma operacao invalida e executada, o programa apresenta uma mensagem de erro.

## Conclusao

O desenvolvimento do MiniGit permitiu praticar o uso de diferentes estruturas de dados em Python e compreender como funciona a organizacao de historicos de commits, branches e merges.

Tambem foi possivel observar a diferenca de custo entre operacoes de escrita e leitura por meio da contagem de passos.
