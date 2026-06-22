from heap import MaxHeap

def gerar_resumo(frases, scores, k=3):
    heap = MaxHeap()

    for indice, score in enumerate(scores):
        heap.inserir((indice, score))

    melhores = []

    for _ in range(k):
        item = heap.extrair_maximo()
        if item is not None:
            melhores.append(item)

    melhores.sort(key=lambda x: x[0])

    resumo = " ".join(frases[indice] for indice, score in melhores)

    return resumo


if __name__ == "__main__":

    frases = [
        "João sofreu lesão no joelho.",
        "O atleta realizou exames.",
        "Foi recomendado repouso.",
        "O jogador voltou aos treinos."
    ]

    scores = [0.40, 0.20, 0.35, 0.10]

    resumo = gerar_resumo(frases, scores)

    print("Resumo:")
    print(resumo)