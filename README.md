# teoriadosgrafos
grafo_direcionado = {1 : {3},
                     2 : {1,5},
                     3 : {},
                     4 : {1,6},
                     5 : {3},
                     6 : {3}}

def get_vizinhos_descendetes(grafo, conjunto_vertices):
    vizinhos = set()
    for vertice in conjunto_vertices:
        adjacentes = grafo[vertice]
        vizinhos.union(adjacentes)
        vizinhos -= set(conjunto_vertices)
        return vizinhos
print(get_vizinhos_descendetes(grafo_direcionado, [1,2]))

def get_vizinhos_ascendentes(grafo, conjunto_vertice):
    vizinhos = set()
    for vertice in conjunto_vertice:
        for vertice_partindo in grafo:
            adjacentes = grafo[vertice_partindo]
        if vertice in adjacentes:
                vizinhos |= {vertice_partindo}
    vizinhos -= set(conjunto_vertice)
    return vizinhos
print(get_vizinhos_ascendentes(grafo_direcionado, [3, 2]))

def fecho_transitivo_direto(grafo, vertice):
    w = set





