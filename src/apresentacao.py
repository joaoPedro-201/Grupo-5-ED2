from load_reports import load_reports
from spacy_processor import SpacyProcessor, calculate_jaccard
from grafo import GrafoMatriz
from pagerank import PageRankMatematicoPurista 
from resumo import gerar_resumo 

def rodar_demonstracao_viva():
    print("=" * 70)
    print("      DEMONSTRAÇÃO VIVA: PIPELINE DE ESTRUTURA DE DADOS     ")
    print("=" * 70)

    # ------------------------------------------------------------------
    # PASSO 1: CARGA DOS DADOS (Membro 1)
    # ------------------------------------------------------------------
    print("\n[PASSO 1] Carregando o Dataset JSON...")
    caminho_dados = '../dados/dataset.json'
    relatorios = load_reports(caminho_dados)

    if not relatorios:
        print("Erro ao carregar os dados. Abortando apresentação.")
        return

    # Selecionamos o Atleta 1 (Basquete) para o Showcase
    laudo = relatorios[0]
    texto_bruto = laudo['texto']
    
    print(f"-> Atleta Selecionado: {laudo['atleta']}")
    print(f"-> Modalidade: {laudo['modalidade']} | Tipo de Relatório: {laudo['tipo']}")
    print(f"-> Tamanho do Texto Bruto: {len(texto_bruto)} caracteres.")

    # ------------------------------------------------------------------
    # PASSO 2: PROCESSAMENTO DE LINGUAGEM NATURAL & LEMATIZAÇÃO (Membro 1)
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("[PASSO 2] Pré-Processamento de Texto com spaCy")
    print("="*70)
    
    processador_nlp = SpacyProcessor()
    
    # Divisão natural em frases
    frases_originais = [f.strip() + "." for f in texto_bruto.split('.') if len(f.strip()) > 5]
    print(f"-> O texto bruto foi fragmentado em {len(frases_originais)} frases (Nós do Grafo).")
    
    print("\n-> Demonstração da Lematização e Remoção de Stopwords (Frases 0 e 1):")
    lista_conjuntos = []
    for i, frase in enumerate(frases_originais):
        frase_limpa_string = processador_nlp.clean_text(frase)
        conjunto_palavras = set(frase_limpa_string.split())
        lista_conjuntos.append(conjunto_palavras)
        
        # Mostra o antes e depois das duas primeiras frases como exemplo pedagógico
        if i < 2:
            print(f"\n   Frase {i} Original: \"{frase}\"")
            print(f"   Frase {i} Limpa (Set): {conjunto_palavras}")

    # ------------------------------------------------------------------
    # PASSO 3: MODELAGEM MATEMÁTICA - GRAFO E MATRIZ DE ADJACÊNCIA (Membro 3)
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("[PASSO 3] Construção da Matriz de Adjacência (Grafo Não-Direcionado)")
    print("="*70)
    print("-> Calculando Similaridade de Jaccard entre todas as combinações de frases...")
    
    # Inicialização da classe de Grafo
    meu_grafo = GrafoMatriz(num_vert=len(frases_originais))
    meu_grafo.salvar_texto(frases_originais)
    
    # Construção das arestas com o limiar configurado
    LIMIAR_PROVA = 0.02
    meu_grafo.construir_arestas(lista_conjuntos, calculate_jaccard, limiar=LIMIAR_PROVA)
    
    print(f"-> Matriz construída com Limiar de Aceitação >= {LIMIAR_PROVA}")
    print("-> Exibindo a estrutura interna da Matriz de Adjacência populada:\n")
    
    # Chamada do método de impressão formatada
    meu_grafo.imprimir_matriz()
    
    print("\n   Nota para a banca: A diagonal principal está zerada (0.00) porque as")
    print("   frases não se conectam consigo mesmas. A matriz é perfeitamente simétrica")
    print("   devido ao espelhamento em tempo de inserção O(1).")

    # ------------------------------------------------------------------
    # PASSO 4: ALGORITMO PAGERANK ESTOCÁSTICO (Membro 4)
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("[PASSO 4] Execução do PageRank Clássico (Método das Potências)")
    print("="*70)
    
    calculador_pr = PageRankMatematicoPurista(matriz_adjacencia=meu_grafo.matriz)
    scores_finais = calculador_pr.calcular_scores()
    
    print("\n-> Distribuição de Vetores de Probabilidade Estabilizados:")
    for i, score in enumerate(scores_finais):
        print(f"   Nó/Frase {i:02d} -> Score PageRank: {score:.6f} | Texto resumido: {frases_originais[i][:55]}...")
        
    soma_verificacao = sum(scores_finais)
    print(f"\n-> Verificação Matemática: Soma de todos os scores = {soma_verificacao:.4f} (Deve ser exatamente 1.0)")

    # ------------------------------------------------------------------
    # PASSO 5: ORGANIZAÇÃO E EXTRAÇÃO COM MAX-HEAP (Membro 5)
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("[PASSO 5] Filtragem e Extração das Top-3 Frases Críticas via Max-Heap")
    print("="*70)
    print("-> Inserindo os pares (Índice, Score) na árvore binária do Max-Heap...")
    
    K_RESUMOS = 3
    resumo_final = gerar_resumo(frases_originais, scores_finais, k=K_RESUMOS)
    
    print(f"-> Remoções sucessivas do nó raiz executadas com sucesso. Elementos reordenados.")
    
    print("\n" + "*" * 70)
    print(" 📋 PRODUTO FINAL: RESUMO EXECUTIVO EXTRAÍDO DO GRAFO")
    print("*" * 70)
    print(f"\n\"{resumo_final}\"\n")
    print("*" * 70)
    print("\n=== FIM DA APRESENTAÇÃO ===\n")

if __name__ == "__main__":
    rodar_demonstracao_viva()