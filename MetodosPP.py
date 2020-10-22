
#Faz a leitura de um arquivo txt que contenha o grafo
def lerGrafo(path):
    with open(path, "r") as file:
        vertices = []
        for line in file:
            line_split = line.strip().split("\t")
            vertices.append(line_split[0])

    grafo = [[0 for i in range(len(vertices))] for i in range(len(vertices))]

    with open(path, "r") as file:
        for line in file:
            line_split = line.strip().split("\t")
            origem = line_split[0]
            for adjacente in line_split[1::]:
                i, j = vertices.index(origem), vertices.index(adjacente)
                grafo[i][j] = 1

    return vertices, grafo

#Retorna os vértices adjacentes de um vértice passado por parâmetro
def getAdjacentes(vertice):
    grafo = lerGrafo()
    listaAdj = []
    for x in range(0, len(grafo[vertice])):
        aux = list(grafo[vertice][x].keys())
        listaAdj.append(aux[0])
    return listaAdj

#Retorna True se o grafo for regular e false se não for
def ehRegular():
    grafo = lerGrafo()
    qntdAdj = []
    for x in grafo:
        qntdAdj.append(len(grafo[x]))
    for x in range(0, len(qntdAdj)-1):
        if qntdAdj[x] != qntdAdj[x+1]:
            regular = False
            return regular
        else:
            regular = True
    return regular

#Retorna True se o grafo for completo e false se não for
def ehCompleto():
    grafo = lerGrafo()
    vertices = []
    for x in grafo:
        vertices.append(x)
    for x in grafo:
        if len(grafo[x]) != len(vertices) -1:
            completo = False
            return completo
        else:
            completo = True
    return completo

#Retorna uma lista de vetores visitados por uma busca em largura após passado um vetor inicial (origem) por parâmetro
def buscaLargura(origem):
    fila = []
    vetoresVisitados = []
    vetoresVisitados.append(origem)
    fila.append(origem)
    while (len(fila) > 0):
        vert1 = fila[0]
        listaAdj = getAdjacentes(vert1)
        for i in listaAdj:
            if (i not in vetoresVisitados):
                vetoresVisitados.append(i)
                fila.append(i)
        fila.pop(0)
    return vetoresVisitados


#Retorna true se o grafo for conexo e false se o grafo for desconexo
def ehConexo(origem):
    grafo = lerGrafo()
    vetoresVisitados = buscaLargura(origem)
    if len(vetoresVisitados) != len(grafo):
        return False
    else:
        return True


# Algoritimo de Djikstra que retorna os menor caminho entre um vértice passado por parâmetro e todos os vértices do grafo
#Seguindo a regra da tabela feita em aula lista S contem os vertices com os menores caminhos entre si

def DjikstraV1(vertice):
    grafo = lerGrafo()
    origem = vertice
    s = []
    vertices = []
    dist = []
    path1 = []
    path2 = []
    caminho = []

    # Adiciona os vértices do grafo em uma lista
    for x in grafo:
        vertices.append(x)

    # Adiciona valores a lista S
    for i in range(0, len(grafo) - 1):
        s.insert(i, "Não")
    s.insert(vertices.index(vertice), "Sim")

    # Adiciona valores a lista dist
    for h in range(0, len(grafo) - 1):
        dist.insert(h, float("distancia inferior"))
    dist.insert(vertices.index(vertice), 0)

    # Adiciona valores a lista path
    for j in range(0, len(grafo)):
        if j == vertices.index(vertice):
            path1.append("=")
            path2.append("=")
        else:
            path1.append(0)
            path2.append(0)

    # Pega os adjacentes e calcula os caminhos
    while s.count("Não") != 0:
        for x in range(0, len(grafo[vertice])):
            p = list(grafo[vertice][x].keys())
            peso = list(grafo[vertice][x].values())
            e = vertices.index(p[0])
            t = vertices.index(vertice)

            if dist[e] > dist[t] + peso[0]:
                dist[e] = dist[t] + peso[0]
                path1[e] = t

        listarMenor = []

        # Listagem  dos caminhos em busca do menor caminho
        for k in range(0, len(grafo)):
            if s[k] != "Sim":
                listarMenor.append(dist[k])

        # É o menor caminho? Se sim, add em S
        for j in range(0, len(grafo)):
            if s[j] != "Sim" and dist[j] == min(listarMenor):
                vertice = vertices[j]
                s[j] = "Sim"

        # Transforma em vértices no path2 os valores de path1
        for p in range(0, len(path1)):
            if path2[p] == "=":
                path2[p] = "="
            else:
                path2[p] = vertices[path1[p]]
    # Faz uma sequência passos para chegar ao menor caminho
    for l in range(0, len(grafo)):
        verticeMenor = vertices[l]
        caminho.append(verticeMenor)
        while "-" not in caminho:
            caminho.append(path2[vertices.index(verticeMenor)])
            verticeMenor = path2[vertices.index(verticeMenor)]
        caminho.pop(-1)
        caminho.reverse()
        #imprime o menor caminho de um vértice a todos os outros vértices do grafo
        print(f"A distância minima do vértice de  {origem} para o vértice {vertices[l]}: é {dist[l]}      "
              f"O caminho é: {caminho}")
        caminho = []


#Algoritimo de Djikstra que retorna os menor caminho entre dois vértices passados por parâmetro
def DjikstraV2(vertice, vertice2):
    grafo = lerGrafo()
    origem = vertice
    s = []
    vertices = []
    dist = []
    path1 = []
    path2 = []
    caminho = []

    # Adiciona os vértices do grafo em uma lista
    for x in grafo:
        vertices.append(x)

    # É o menor caminho? Se sim, add em S
    for k in range(0, len(grafo) - 1):
        s.insert(k, "Não")
    s.insert(vertices.index(vertice), "Sim")

    # Adiciona valores a lista dist
    for z in range(0, len(grafo) - 1):
        dist.insert(z, float("inf"))
    dist.insert(vertices.index(vertice), 0)

    # Adiciona valores a lista path
    for y in range(0, len(grafo)):
        if y == vertices.index(vertice):
            path1.append("=")
            path2.append("=")
        else:
            path1.append(0)
            path2.append(0)

    # Pega os adjacentes e calcula os caminhos entre eles
    while s[vertices.index(vertice2)] != "Sim":
        for x in range(0, len(grafo[vertice])):
            a = list(grafo[vertice][x].keys())
            peso = list(grafo[vertice][x].values())
            z = vertices.index(a[0])
            t = vertices.index(vertice)

            if dist[z] > dist[t] + peso[0]:
                dist[z] = dist[t] + peso[0]
                path1[z] = t

        listaMenor = []

        #Lista os caminhos em busca do menor caminho
        for k in range(0, len(grafo)):
            if s[k] != "sim":
                listaMenor.append(dist[k])

        #Adiciona "sim" a lista S quando for o menor caminho
        for j in range(0, len(grafo)):
            if s[j] != "sim" and dist[j] == min(listaMenor):
                vert = vertices[j]
                s[j] = "sim"

         #Pega os valores de path1 e transforma em vértices no path2
        for p in range(0, len(path1)):
            if path2[p] == "-":
                path2[p] = "-"
            else:
                path2[p] = vertices[path1[p]]

    #Explica como chegou do menor caminho
    verticeMenor = vertice2
    caminho.append(verticeMenor)
    while "-" not in caminho:
        caminho.append(path2[vertices.index(verticeMenor)])
        verticeMenor = path2[vertices.index(verticeMenor)]
    caminho.pop(-1)
    caminho.reverse()

    # Imprime o menor caminho de um vértice a outro vértice
    print(f"A distância minima do vértice {origem} para o vértice {vertice2}: é {dist[vertices.index(vertice2)]}    "
          f" O caminho é: {caminho}")