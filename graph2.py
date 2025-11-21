def add_edge_undirected(mapa_grafo, vertice_a, vertice_b):
    if vertice_a not in mapa_grafo:
        mapa_grafo[vertice_a] = []
    if vertice_b not in mapa_grafo:
        mapa_grafo[vertice_b] = []

    mapa_grafo[vertice_a].append(vertice_b)
    mapa_grafo[vertice_b].append(vertice_a)

def check_for_cycle(mapa_grafo):
    todos_visitados = set()
    lista_vertices = list(mapa_grafo.keys())

    for vertice_inicial in lista_vertices:
        if vertice_inicial not in todos_visitados:
            print(f"\nIniciando busca por ciclo no componente a partir de: {vertice_inicial}")
            if iterative_cycle_finder(mapa_grafo, vertice_inicial, todos_visitados):
                return True
    return False

def iterative_cycle_finder(mapa_grafo, vertice_inicial, conjunto_visitados_global):
    pilha_dfs = [(vertice_inicial, None)]
    caminho_visitado_local = set()

    while len(pilha_dfs) > 0:
        dados_vertice = pilha_dfs.pop()
        vertice_atual, vertice_pai = dados_vertice

        if vertice_atual in caminho_visitado_local:
            continue

        caminho_visitado_local.add(vertice_atual)
        conjunto_visitados_global.add(vertice_atual)

        vertices_adjacentes = mapa_grafo.get(vertice_atual, [])

        for vizinho in vertices_adjacentes:

            if vizinho != vertice_pai and vizinho in caminho_visitado_local:
                print(f"*** CICLO ENCONTRADO! Conexão de {vertice_atual} para {vizinho} forma um ciclo. ***")
                return True

            if vizinho not in caminho_visitado_local:
                pilha_dfs.append((vizinho, vertice_atual))

    return False

if __name__ == "__main__":

    grafo_com_ciclo = {}
    add_edge_undirected(grafo_com_ciclo, 'P', 'Q')
    add_edge_undirected(grafo_com_ciclo, 'Q', 'R')
    add_edge_undirected(grafo_com_ciclo, 'R', 'P')

    print("--- Verificando Grafo 1 (Esperado: SIM) ---")
    resultado_1 = check_for_cycle(grafo_com_ciclo)
    print(f"Resultado final: O Grafo 1 tem ciclo? {'SIM' if resultado_1 else 'NÃO'}")

    print("\n" + "="*40 + "\n")

    grafo_sem_ciclo = {}
    add_edge_undirected(grafo_sem_ciclo, 'G1', 'G2')
    add_edge_undirected(grafo_sem_ciclo, 'G2', 'G3')
    add_edge_undirected(grafo_sem_ciclo, 'G1', 'G4')

    print("--- Verificando Grafo 2 (Esperado: NÃO) ---")
    resultado_2 = check_for_cycle(grafo_sem_ciclo)
    print(f"Resultado final: O Grafo 2 tem ciclo? {'SIM' if resultado_2 else 'NÃO'}")
