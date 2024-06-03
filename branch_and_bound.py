import sys

# Função para calcular o custo mínimo usando a técnica de Branch and Bound
class TSPSolver:
    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        self.visited = [False] * n
        self.min_cost = sys.maxsize

    def tsp(self, curr_pos, count, cost, start):
        # Se todas as cidades forem visitadas e houver um caminho de volta para o ponto inicial
        if count == self.n and self.graph[curr_pos][start]:
            self.min_cost = min(self.min_cost, cost + self.graph[curr_pos][start])
            return

        # Visite todas as cidades
        for i in range(self.n):
            if not self.visited[i] and self.graph[curr_pos][i]:
                # Marque a cidade como visitada
                self.visited[i] = True
                self.tsp(i, count + 1, cost + self.graph[curr_pos][i], start)

                # Desmarque a cidade
                self.visited[i] = False

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de gráfico (matriz de adjacência)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    n = len(graph)

    tsp_solver = TSPSolver(graph, n)
    
    # Começando da cidade 0
    tsp_solver.visited[0] = True
    tsp_solver.tsp(0, 1, 0, 0)

    print(f"O custo mínimo da rota do Caixeiro Viajante é: {tsp_solver.min_cost}")
