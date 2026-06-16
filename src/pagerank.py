class PageRankMatematicoPurista:
    def __init__(self, matriz_adjacencia, d=0.85, max_iter=100, tol=1e-6):
        """
        Algoritmo PageRank Clássico (Iterativo / Método das Potências)
        baseado estritamente na modelagem original de Larry Page e Sergey Brin.
        """
        self.matriz = matriz_adjacencia
        self.N = len(matriz_adjacencia)
        self.d = d  # Fator de amortecimento (damping factor)
        self.max_iter = max_iter
        self.tol = tol

    def calcular_scores(self):
        # Inicialização purista: vetor de probabilidade uniforme (1 / N)
        scores_atuais = [1.0 / self.N] * self.N
        
        # Criação da Matriz de Transição Estocástica
        # No PageRank, cada linha deve somar 1. Se a linha sum(matriz[i]) for > 0, 
        # dividimos cada elemento pelo total daquela linha.
        matriz_transicao = [[0.0 for _ in range(self.N)] for _ in range(self.N)]
        
        for i in range(self.N):
            soma_linha = sum(self.matriz[i])
            if soma_linha > 0:
                for j in range(self.N):
                    matriz_transicao[i][j] = self.matriz[i][j] / soma_linha
            # Nós sem nenhuma saída (Dangling Nodes) serão tratados dinamicamente no loop

        # Loop de Iteração de Potências (Power Iteration)
        for iteracao in range(self.max_iter):
            novos_scores = [0.0] * self.N
            
            # Constante do vetor de teleporte do PageRank (gerado pelo damping factor)
            teleporte = (1.0 - self.d) / self.N

            for j in range(self.N):
                soma_links = 0.0
                for i in range(self.N):
                    soma_linha_original = sum(self.matriz[i])
                    
                    if soma_linha_original > 0:
                        # O nó 'i' passa sua autoridade para o nó 'j' baseado na matriz estocástica
                        soma_links += matriz_transicao[i][j] * scores_atuais[i]
                    else:
                        # Se o nó 'i' for um nó sumidouro (Dangling Node), 
                        # ele distribui sua probabilidade igualmente para todos
                        soma_links += (1.0 / self.N) * scores_atuais[i]

                # Equação fundamental do PageRank
                novos_scores[j] = teleporte + self.d * soma_links

            # Teste de convergência por norma L1 (distância absoluta dos vetores)
            variacao = sum(abs(novos_scores[k] - scores_atuais[k]) for k in range(self.N))
            if variacao < self.tol:
                print(f"-> PageRank Puro convergiu com sucesso na iteração {iteracao + 1}")
                return novos_scores

            scores_atuais = novos_scores

        print("-> PageRank atingiu o limite máximo de iterações.")
        return scores_atuais
if __name__ == "__main__":
    print("====================================================")
    print("   INICIANDO TESTE UNITÁRIO DO PAGERANK PURISTA     ")
    print("====================================================\n")

    # 1. Criação da matriz N x N simulada (3 frases)
    # matriz[origem][destino]
    matriz_teste = [
        [0.0, 0.8, 0.0],  # Nó 0 se conecta ao Nó 1
        [0.0, 0.0, 0.0],  # Nó 1 é um nó sem saídas (Dangling)
        [0.0, 0.9, 0.0]   # Nó 2 se conecta ao Nó 1
    ]

    # 2. Instanciando o seu algoritmo matemático
    # Vamos usar as configurações padrão (d=0.85, max_iter=100)
    calculador = PageRankMatematicoPurista(matriz_adjacencia=matriz_teste)
    
    # 3. Executando o cálculo
    scores_finais = calculador.calcular_scores()

    print("\n================== RESULTADOS ==================")
    for i, score in enumerate(scores_finais):
        print(f"Frase/Nó {i}: Score = {score:.4f}")
    print("================================================\n")

    # 4. Validação automática dos critérios de sucesso
    print("-> Verificação de Consistência:")
    
    # Critério 1: A soma de todos os scores deve ser exatamente 1.0 (ou muito próxima por float)
    soma_total = sum(scores_finais)
    print(f"1. Soma total dos scores (deve ser 1.0): {soma_total:.6f}")
    assert abs(soma_total - 1.0) < 1e-5, "ERRO: A soma dos scores não é igual a 1!"

    # Critério 2: O Nó 1 precisa ter a maior nota
    print(f"2. Nó 1 é o maior? {'SIM' if scores_finais[1] > scores_finais[0] and scores_finais[1] > scores_finais[2] else 'NÃO'}")
    assert scores_finais[1] > scores_finais[0] and scores_finais[1] > scores_finais[2], "ERRO: O nó central não acumulou a maior autoridade!"

    print("\n✅ TUDO OK! O core matemático passou no teste de estresse estocástico.")
        