# MiniGit - Estrutura de Dados

## Apresentação

Este projeto foi desenvolvido para colocar em prática os conhecimentos de estruturas de dados utilizando Python. O MiniGit simula algumas funções básicas do Git, trabalhando com commits, branches, histórico e merge.

Foram utilizados dicionários, listas, tuplas e filas para armazenar e consultar as informações.

## Funcionalidades

- Criar commits com identificadores automáticos.
- Consultar mensagens dos commits.
- Consultar os pais de cada commit.
- Criar e trocar branches.
- Realizar merge entre branches.
- Consultar o histórico com log.
- Buscar palavras nas mensagens.
- Identificar commits de merge.
- Contabilizar os passos das operações.

## Tabela de medição

| Quantidade de commits | Passos do commitar | Passos do log |
|---|---:|---:|
| 10 | 2 | 10 |
| 100 | 2 | 100 |
| 1000 | 2 | 1000 |

## Respostas das questões

### 1. Por que o commitar gasta sempre 2 passos, e o log gasta mais conforme o histórico cresce?

O commitar realiza apenas duas ações: criar o commit e atualizar o ponteiro da branch atual. O log precisa percorrer os commits existentes para encontrar todo o histórico, por isso o número de passos aumenta conforme a quantidade de commits cresce.

### 2. Por que mensagem(commit) gasta 1 passo e buscar(texto) pode gastar muitos?

A mensagem utiliza o identificador como chave do dicionário, permitindo encontrar o conteúdo diretamente. Já a busca por texto precisa verificar as mensagens uma por uma, porque o dicionário não oferece uma procura direta pelo valor armazenado.

### 3. Por que o merge é um commit com dois pais, e por que isso faz do histórico um grafo, e não uma lista?

O merge une duas branches e precisa guardar os dois commits de origem como pais. Dessa maneira, o histórico pode ter diferentes caminhos e ligações entre commits, formando um grafo em vez de uma sequência única como acontece em uma lista.

### 4. Por que o método pais devolve uma tupla, e não a lista que está guardada dentro do dicionário?

A tupla protege as informações internas da classe, pois não permite alterações nos pais por quem chama o método. Assim, o histórico permanece protegido contra modificações externas.

## Conclusão

A realização deste projeto ajudou a compreender melhor o funcionamento das estruturas de dados e a diferença entre os custos de leitura e escrita. Também foi possível entender como o Git organiza seus commits, branches e merges por meio de um grafo.