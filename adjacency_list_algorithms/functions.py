def get_grau(grafo, vertice):
    adjacentes = grafo[vertice]
    grau = len(adjacentes)
    return grau

def get_vertices_do_grau(grafo, grau):
    resposta = []
    for vertice in grafo:
        grau_do_vertice = len(grafo[vertice])
        if grau == grau_do_vertice:
            resposta.append(vertice)
        else:
            pass
            
    return resposta

    def check_is_subgraph(grafo1, grafo2):
        for vertice in grafo2:
            if vertice not in grafo1:
                return False;
            else:
                adjacency_graph1 = grafo1[vertice]
                adjacency_graph2 = graph2[vertice]
                for neighboor in adjacency_graph2:
                    if neighboor not in adjacency_graph1:
                        return False
                    else:
                        pass

        return True