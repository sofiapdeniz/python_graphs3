def add_edge_directed(grafo, u, v):
    if u not in grafo:
        grafo[u] = []
    grafo[u].append(v)

def depth_first_search(grafo, vertice_inicial):
    pilha_visita = [vertice_inicial]
    vertices_visitados = set()

    print(f"**Iniciando Busca em Profundidade (DFS) a partir de {vertice_inicial}:**")
    print("Ordem dos vertices percorridos:", end=' ')

    while len(pilha_visita) > 0:
        vertice_atual = pilha_visita.pop()

        if vertice_atual in vertices_visitados:
            continue

        vertices_visitados.add(vertice_atual)
        print(vertice_atual, end=' -> ')

        lista_vizinhos = grafo.get(vertice_atual, [])

        for vizinho in reversed(lista_vizinhos):
            if vizinho not in pilha_visita and vizinho not in vertices_visitados:
                pilha_visita.append(vizinho)
    print("FIM")

if __name__ == "__main__":
    estrutura_grafo = {}
    add_edge_directed(estrutura_grafo, 'A', 'B')
    add_edge_directed(estrutura_grafo, 'A', 'C')
    add_edge_directed(estrutura_grafo, 'B', 'C')
    add_edge_directed(estrutura_grafo, 'C', 'A')
    add_edge_directed(estrutura_grafo, 'C', 'D')
    add_edge_directed(estrutura_grafo, 'D', 'D')

    depth_first_search(estrutura_grafo, 'C')
