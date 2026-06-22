#  Análise de Laudos Esportivos com Grafos e PLN

Este projeto aplica técnicas avançadas de **Processamento de Linguagem Natural (PLN)** e **Teoria dos Grafos** para sumarizar automaticamente laudos técnicos e médicos de atletas. Através de algoritmos estocásticos e estruturas de dados implementadas do zero, o sistema extrai as informações mais críticas de blocos de texto não estruturados.

Projeto desenvolvido para a disciplina de Estrutura de Dados 2 na Universidade de Brasília (FCTE).

## 🧠 Arquitetura e Pipeline de Dados

O fluxo de processamento funciona como uma linha de montagem industrial, onde o texto bruto entra e um resumo executivo matemático sai, seguindo 5 etapas:

1. **Entradas de Dados (JSON):** Leitura de laudos contendo o histórico do atleta.
2. **Pré-Processamento (NLP):** Utiliza a biblioteca `spaCy` para dividir o texto em frases, remover stopwords, pontuações e aplicar lematização (redução das palavras à sua raiz morfológica).
3. **Modelagem Matemática (Grafos):** Constrói uma **Matriz de Adjacência** não-direcionada e ponderada. Cada nó é uma frase. As arestas são criadas baseadas na **Similaridade de Jaccard** entre os conjuntos de palavras de cada frase, utilizando um limiar de corte dinâmico para evitar grafos esparsos ou densos demais.
4. **Cálculo de Relevância (PageRank):** Implementação purista do algoritmo PageRank (Método das Potências). O grafo de similaridade é convertido numa matriz de transição estocástica para calcular a "autoridade" (score) de cada frase dentro do contexto geral, lidando com *dangling nodes* de forma eficiente.
5. **Extração de Resumo (Max-Heap):** Uma fila de prioridade implementada manualmente (sem bibliotecas externas) organiza as frases pelas suas notas do PageRank em tempo logarítmico. As Top-3 frases são extraídas e reordenadas cronologicamente para formar o resumo final.

## 📂 Estrutura do Repositório

```text
scout-certo/
│
├── dados/
│   └── dataset.json             # Base de dados (entradas geradas)
│
├── src/
│   ├── apresentacao.py          # Showcase detalhado do funcionamento interno
│   ├── grafo.py                 # Matriz de Adjacência e Jaccard
│   ├── heap.py                  # Árvore binária Max-Heap e ordenação
│   ├── load_reports.py          # Script de carregamento de dados
│   ├── main.py                  # Orquestrador do pipeline em lote (50 laudos)
│   ├── pagerank.py              # Algoritmo de centralidade
│   ├── resumo.py                # Função que gera os resumos finais
│   └── spacy_processor.py       # Lematização e limpeza com spaCy
│
├── .gitignore
└── README.md
```
## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3 instalado (recomendado testar em ambiente Linux/Ubuntu) e instale a dependência do spaCy juntamente com o modelo de linguagem em português:


```bash
pip install spacy
python -m spacy download pt_core_news_sm
```

Rodando a Aplicação
Para ver o sistema processando o lote completo de laudos:

```bash
cd src
python main.py
```

Para uma visualização "aberta", demonstrando a construção da matriz e a convergência matemática (ideal para bancas e apresentações):

```bash
cd src
python apresentacao.py
```

## 👥 Equipe (Grupo 5)
- Bruno de Oliveira
- Eduardo Ribeiro Gomes da Silva
- João Pedro de Sousa Silva
- Lara Giuliana Lima dos Santos
- Pedro Vieira Antunes