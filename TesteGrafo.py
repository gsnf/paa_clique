from Trab1_ForcaBruta import Grafo

grafotest = {'1':['3','5'],
             '2':['4','3','8'],
             '3':['1','2','4','5','6'],
             '4':['2','3','5','6'],
             '5':['1','3','4','6','7','9'],
             '6':['3','4','5','7','8',],
             '7':['5','6','8','9'],
             '8':['2','6','7','9'],
             '9':['5','8','7'],
             '10':[]
             }
exemplo = Grafo.Grafo()

exemplo.G = grafotest
cliqueMaxExemplo = exemplo.cliqueMaximo()
print(exemplo.listaClique)
print(cliqueMaxExemplo)

