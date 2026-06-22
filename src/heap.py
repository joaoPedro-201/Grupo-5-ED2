class MaxHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        self.heap.append(item)
        self._subir(len(self.heap) - 1)

    def extrair_maximo(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maior = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)

        return maior

    def _subir(self, indice):
        while indice > 0:
            pai = (indice - 1) // 2

            if self.heap[indice][1] > self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def _descer(self, indice):
        tamanho = len(self.heap)

        while True:
            maior = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if esquerda < tamanho and self.heap[esquerda][1] > self.heap[maior][1]:
                maior = esquerda

            if direita < tamanho and self.heap[direita][1] > self.heap[maior][1]:
                maior = direita

            if maior != indice:
                self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
                indice = maior
            else:
                break

if __name__ == "__main__":

    heap = MaxHeap()

    heap.inserir((0, 0.15))
    heap.inserir((1, 0.42))
    heap.inserir((2, 0.30))

    print(heap.extrair_maximo())