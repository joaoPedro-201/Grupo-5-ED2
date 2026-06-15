class GrafoMatriz:

    def __init__(self, num_vert = 3):
        self.num_vert = num_vert
        self.matriz = [[0.0 for _ in range(num_vert)] for _ in range(num_vert)]
        self.texto_original = []

    def salvar_texto(self, lista_texto):
        self.texto_original = lista_texto

    def adicionar_aresta(self, vert1, vert2, peso):
        self.matriz[vert1][vert2] = peso
        self.matriz[vert2][vert1] = peso

    def construir_arestas(self, conjuntos_palavras, funcao_jaccard, limiar=0.15):
        for i in range(self.num_vert):
            for j in range(i + 1, self.num_vert):
                peso = funcao_jaccard(conjuntos_palavras[i], conjuntos_palavras[j])
                if peso >= limiar:
                    self.adicionar_aresta(i, j, peso)

    def imprimir_matriz(self):
        print("Matriz de Adjacência:")
        for linha in self.matriz:
            linha_formatada = ["{:.2f}".format(peso) for peso in linha]
            print(linha_formatada)


# ===================================================================
# CÓDIGO DE TESTE PARA VER SE A CONSTRUÇÃO DO GRAFO ESTÁ FUNCIONANDO
# ===================================================================
if __name__ == "__main__":

    def simular_jaccard(set1, set2):
        if not set1.union(set2): return 0.0
        return len(set1.intersection(set2)) / len(set1.union(set2))

    frase0 = {"atleta", "sente", "dor", "joelho"}
    frase1 = {"atleta", "tem", "lesao", "joelho"}
    frase2 = {"jogador", "tem", "excelente", "passe"}

    lista_de_conjuntos = [frase0, frase1, frase2]

    meu_grafo = GrafoMatriz(num_vert=3)

    meu_grafo.construir_arestas(conjuntos_palavras=lista_de_conjuntos, 
                                funcao_jaccard=simular_jaccard, 
                                limiar=0.1) # Limiar baixo para garantir a aresta

    print("Teste da Construção do Grafo executado com sucesso!\n")
    meu_grafo.imprimir_matriz()