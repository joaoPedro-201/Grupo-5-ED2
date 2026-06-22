from load_reports import load_reports
from spacy_processor import SpacyProcessor, calculate_jaccard
from grafo import GrafoMatriz
from pagerank import PageRankMatematicoPurista 
from resumo import gerar_resumo 

def executar_pipeline():
    print("==================================================")
    print("      INICIANDO SISTEMA      ")
    print("==================================================\n")

    caminho_dados = '../dados/dataset.json'
    relatorios = load_reports(caminho_dados)

    if not relatorios:
        return

    processador_nlp = SpacyProcessor()
    
    print("\nIniciando processamento em lote. Isso pode levar alguns minutos...\n")

    for indice, laudo in enumerate(relatorios):
        texto_bruto = laudo.get('texto', '')
        
        if not texto_bruto:
            continue
            
        print(f"[{indice + 1}/50] Analisando: {laudo['atleta']} ({laudo['modalidade']})", end="... ")

        frases_originais = [f.strip() + "." for f in texto_bruto.split('.') if len(f.strip()) > 5]
        
        lista_conjuntos = []
        for frase in frases_originais:
            frase_limpa_string = processador_nlp.clean_text(frase)
            conjunto_palavras = set(frase_limpa_string.split())
            lista_conjuntos.append(conjunto_palavras)

        meu_grafo = GrafoMatriz(num_vert=len(frases_originais))
        meu_grafo.salvar_texto(frases_originais)
        meu_grafo.construir_arestas(lista_conjuntos, calculate_jaccard, limiar=0.02)

        calculador_pr = PageRankMatematicoPurista(matriz_adjacencia=meu_grafo.matriz)
        scores_finais = calculador_pr.calcular_scores()

        resumo_final = gerar_resumo(frases_originais, scores_finais, k=3)

        print("OK!")
        
        print("-" * 60)
        print(f"RESUMO: {resumo_final}")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    executar_pipeline()