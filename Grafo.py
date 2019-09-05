import itertools
class Grafo(object):
    def __init__(self):
        self.G = {}  #grafo como dicionario
        self.listaClique = []

    def Clique(self):
        for i in range (2, len(self.G)+1):
            listaElementos = list(itertools.combinations(self.G,i)) #lista de combinaçoes de vertices possiveis de tamanho i
            for j in listaElementos: #percorrer cada combinaçao da lista de elementos
                flag1 = 0
                for k in j: #percorre cada elemento da combinaçao j
                    listaElementos2 = list(j) #cria uma lista de elementos
                    listaElementos2.remove(k) #da combinaçao sem o elemento k

                    listaVerticesAdj = self.G[k] #lista de vertices adjacentes ao vertice k
                    flag2 = 0

                    for l in listaElementos2:
                        if l in listaVerticesAdj: #checa se o elemento l pertence a lista de adjacentes de k
                            flag2 +=1 #incrementa a flag2 
                    if flag2 == len(listaElementos2):
                        flag1 +=1 #incrementa a flag se o todos os elementos da lista2 estiverem na lsita de adjacencia
                if flag1 == len(j):
                    self.listaClique.append(j) #sendo clique adiciona na lista de cliques

    def cliqueMaximo(self):
        self.Clique()
        tam = 0
        cliqueMax = [] #lista de cliques maximos
        for i in self.listaClique: #procura na lista o elemento com o maior tamanho
            if len(i) > tam:
                tam = len(i)
                cliqueMax = [i]
            elif len(i) == tam:
                cliqueMax.append(i)
        return cliqueMax

##Custo operacional de O(n!)