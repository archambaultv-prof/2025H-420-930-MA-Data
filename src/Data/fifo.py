class FIFO:
    def __init__(self):
        # Liste pour stocker les éléments de la file
        self._data = []
        # Pointeur vers la tête de la file
        self._head = 0

    def enqueue(self, item):
        # Ajoute un élément à la fin de la file
        self._data.append(item)

    def dequeue(self):
        # Retire et retourne l'élément en tête de la file
        if self.is_empty():
            raise IndexError("retrait d'un élément dans une file vide")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head += 1
        # Nettoyage périodique pour éviter la croissance infinie de la liste
        if self._head > 50 and self._head > len(self._data) // 2:
            self._data = self._data[self._head:]
            self._head = 0
        return item

    def is_empty(self):
        # Retourne True si la file est vide, sinon False
        return self._head >= len(self._data)

    def peek(self):
        # Retourne l'élément en tête sans le retirer
        if self.is_empty():
            raise IndexError("lecture d'un élément dans une file vide")
        return self._data[self._head]
