
from collections import deque


class MiniGit:
    """
    Simula um historico Git usando dicionarios,
    listas, tuplas e fila.
    """

    __slots__ = (
        "__pais",
        "__mensagens",
        "__branches",
        "__branch_atual",
        "__contador",
        "__passos"
    )

    def __init__(self):
        # Inicia o repositorio vazio, com a branch main.
        # Custo: 0 passos.
        self.__pais = {}
        self.__mensagens = {}
        self.__branches = {"main": None}
        self.__branch_atual = "main"
        self.__contador = 0
        self.__passos = 0

    @property
    def passos(self):
        # Devolve os passos da ultima operacao.
        # Custo: 0 passos.
        return self.__passos

    @property
    def branch_atual(self):
        # Devolve o nome da branch selecionada.
        # Custo: 0 passos.
        return self.__branch_atual

    def commitar(self, mensagem):
        # Cria um commit e move o ponteiro da branch atual.
        # Custo: 2 passos.
        if not mensagem:
            self.__passos = 0
            raise ValueError("A mensagem nao pode ser vazia")

        self.__contador += 1
        identificador = "c" + str(self.__contador)

        commit_anterior = self.__branches[self.__branch_atual]
        lista_pais = []

        if commit_anterior is not None:
            lista_pais.append(commit_anterior)

        self.__pais[identificador] = lista_pais
        self.__mensagens[identificador] = mensagem
        self.__passos = 1

        self.__branches[self.__branch_atual] = identificador
        self.__passos += 1

        return identificador

    def mensagem(self, commit):
        # Busca a mensagem diretamente pela chave do dicionario.
        # Custo: 1 passo.
        self.__passos = 1

        if commit not in self.__mensagens:
            raise ValueError("Commit nao existe")

        return self.__mensagens[commit]

    def pais(self, commit):
        # Devolve os pais como tupla para proteger a lista interna.
        # Custo: 1 passo.
        self.__passos = 1

        if commit not in self.__pais:
            raise ValueError("Commit nao existe")

        return tuple(self.__pais[commit])

    def criar_branch(self, nome):
        # Cria uma branch apontando para o commit atual.
        # Custo: 1 passo.
        self.__passos = 0

        if nome in self.__branches:
            raise ValueError("Essa branch ja existe")

        commit_atual = self.__branches[self.__branch_atual]

        if commit_atual is None:
            raise ValueError("Nao existem commits para criar a branch")

        self.__branches[nome] = commit_atual
        self.__passos = 1

    def trocar_branch(self, nome):
        # Seleciona outra branch existente.
        # Custo: 1 passo.
        self.__passos = 0

        if nome not in self.__branches:
            raise ValueError("Branch nao existe")

        self.__branch_atual = nome
        self.__passos = 1

    def mesclar(self, nome):
        # Cria um commit com dois pais e move o ponteiro.
        # Custo: 2 passos.
        self.__passos = 0

        if nome not in self.__branches:
            raise ValueError("Branch nao existe")

        if nome == self.__branch_atual:
            raise ValueError("Nao pode mesclar a propria branch")

        primeiro_pai = self.__branches[self.__branch_atual]
        segundo_pai = self.__branches[nome]

        if primeiro_pai is None or segundo_pai is None:
            raise ValueError("Uma das branches nao possui commits")

        self.__contador += 1
        identificador = "c" + str(self.__contador)

        self.__pais[identificador] = [primeiro_pai, segundo_pai]
        self.__mensagens[identificador] = "merge de " + nome
        self.__passos = 1

        self.__branches[self.__branch_atual] = identificador
        self.__passos += 1

        return identificador

    def log(self):
        # Percorre os commits alcancaveis usando uma fila.
        # Cada commit diferente visitado custa 1 passo.
        self.__passos = 0

        commit_inicial = self.__branches[self.__branch_atual]

        if commit_inicial is None:
            return ()

        fila = deque()
        fila.append(commit_inicial)

        visitados = {}
        resultado = []

        while fila:
            commit = fila.popleft()

            if commit in visitados:
                continue

            visitados[commit] = True
            resultado.append(commit)
            self.__passos += 1

            for pai in self.__pais[commit]:
                fila.append(pai)

        return tuple(resultado)

    def buscar(self, texto):
        # Procura o texto nas mensagens pela ordem de criacao.
        # Custo: 1 passo por mensagem consultada.
        self.__passos = 0

        for identificador in self.__mensagens:
            self.__passos += 1

            if texto in self.__mensagens[identificador]:
                return identificador

        return None

    def merges(self):
        # Localiza commits que possuem mais de um pai.
        # Custo: 1 passo por commit existente.
        self.__passos = 0

        resultado = []

        for identificador in self.__pais:
            self.__passos += 1

            if len(self.__pais[identificador]) > 1:
                resultado.append(identificador)

        return tuple(resultado)


def tentar(acao):
    # Executa uma operacao e mostra erros esperados.
    try:
        acao()
    except ValueError as erro:
        print("erro:", erro)


def medir(quantidade):
    # Mede os passos de escrita e leitura.
    git = MiniGit()

    for numero in range(quantidade):
        git.commitar("commit " + str(numero))

    passos_commitar = git.passos

    git.log()
    passos_log = git.passos

    return passos_commitar, passos_log


# TESTES PRINCIPAIS

git = MiniGit()

git.commitar("primeiro commit")
print(git.passos)

git.commitar("segundo commit")
git.criar_branch("feature")
print(git.passos)

git.commitar("terceiro commit")
git.trocar_branch("feature")
git.commitar("quarto commit")
git.trocar_branch("main")
git.mesclar("feature")

print(git.pais("c5"))
print(git.log(), git.passos)
print(git.mensagem("c3"), git.passos)
print(git.buscar("quarto"), git.passos)
print(git.merges())

git.trocar_branch("feature")
print(git.log(), git.passos)

git.trocar_branch("main")


# TESTES DE ERRO

tentar(lambda: git.trocar_branch("inexistente"))
tentar(lambda: git.criar_branch("main"))
tentar(lambda: git.mesclar("main"))
tentar(lambda: git.pais("c99"))


# MEDICAO DE LEITURA E ESCRITA

print()
print("commits   passos do commitar   passos do log")

for quantidade in (10, 100, 1000):
    passos_commitar, passos_log = medir(quantidade)

    print(
        quantidade,
        "       ",
        passos_commitar,
        "                    ",
        passos_log
    )
