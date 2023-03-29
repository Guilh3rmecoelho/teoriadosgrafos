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