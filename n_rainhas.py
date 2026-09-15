import time
from aigyminsper.search.graph import State
from aigyminsper.search.search_algorithms import BuscaLargura


class NRainhas(State):
   

    def __init__(self, op, tabuleiro, n):
        super().__init__(op)
        self.tabuleiro = tabuleiro  
        self.n = n

    def _posicao_segura(self, coluna):
        linha_nova = len(self.tabuleiro)
        for linha_existente, coluna_existente in enumerate(self.tabuleiro):
            mesma_coluna = coluna_existente == coluna
            mesma_diagonal = abs(coluna_existente - coluna) == abs(
                linha_existente - linha_nova
            )
            if mesma_coluna or mesma_diagonal:
                return False
        return True

    def successors(self):
        sucessores = []
        linha_nova = len(self.tabuleiro)

        
        if linha_nova >= self.n:
            return sucessores

        for coluna in range(self.n):
            if self._posicao_segura(coluna):
                novo_tabuleiro = self.tabuleiro + [coluna]
                operador = f"Rainha({linha_nova},{coluna})"
                sucessores.append(NRainhas(operador, novo_tabuleiro, self.n))

        return sucessores

    def is_goal(self):
        return len(self.tabuleiro) == self.n

    def description(self):
        return f"Estado com {len(self.tabuleiro)}/{self.n} rainhas: {self.tabuleiro}"

    def cost(self):
        return 1

    def env(self):
        
        return tuple(self.tabuleiro)


def imprime_tabuleiro(tabuleiro, n):
    linhas = []
    for linha in range(n):
        casas = []
        for coluna in range(n):
            casas.append("Q" if tabuleiro[linha] == coluna else ".")
        linhas.append(" ".join(casas))
    return "\n".join(linhas)


def resolve_n_rainhas(n, pruning="without"):
    estado_inicial = NRainhas("estado inicial", [], n)
    algoritmo = BuscaLargura()

    inicio = time.time()
    resultado = algoritmo.search(estado_inicial, pruning=pruning)
    fim = time.time()

    return resultado, fim - inicio


def main():
    tamanhos = [4, 5, 6, 7, 8]

    for n in tamanhos:
        print("=" * 50)
        print(f"Resolvendo o problema das {n}-Rainhas com BFS")
        print("=" * 50)

        resultado, tempo_execucao = resolve_n_rainhas(n)

        if resultado is not None:
            tabuleiro_final = resultado.get_state().tabuleiro
            print(f"Solução encontrada para N={n}:")
            print(imprime_tabuleiro(tabuleiro_final, n))
            print(f"\nSequência de posições: {tabuleiro_final}")
            print(f"Profundidade da solução (nº de rainhas): {resultado.depth}")
        else:
            print(f"Nenhuma solução encontrada para N={n}.")

        print(f"Tempo de execução: {tempo_execucao:.4f} segundos\n")


if __name__ == "__main__":
    main()