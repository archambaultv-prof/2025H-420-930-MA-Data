class Deque:
    def __init__(self):
        # Liste pour stocker les éléments de la deque
        self._data = []
        # Pointeur vers la tête
        # Nous n'avons pas besoin de pointeur pour la queue
        # car la liste Python gère automatiquement la taille.
        self._head = 0

    def append_left(self, item):
        # Ajoute un élément à gauche de la deque
        if self._head == 0:
            # Pré-alloue de l'espace à gauche
            new_space = max(8, len(self._data) * 2)
            self._data = [None] * new_space + self._data
            self._head = new_space
        self._head -= 1
        self._data[self._head] = item

    def append_right(self, item):
        # Ajoute un élément à droite de la deque
        self._data.append(item)

    def pop_left(self):
        # Retire et retourne l'élément à gauche de la deque
        if self.is_empty():
            raise IndexError("retrait d'un élément dans une deque vide")
        item = self._data[self._head]
        self._head += 1
        # Nettoyage périodique
        if self._head > 50 and self._head > (len(self._data) - self._head):
            self._data = self._data[self._head:]
            self._head = 0
        return item

    def pop_right(self):
        # Retire et retourne l'élément à droite de la deque
        if self.is_empty():
            raise IndexError("retrait d'un élément dans une deque vide")
        return self._data.pop()

    def peek_left(self):
        # Retourne l'élément à gauche sans le retirer
        if self.is_empty():
            raise IndexError("lecture d'un élément dans une deque vide")
        return self._data[self._head]

    def peek_right(self):
        # Retourne l'élément à droite sans le retirer
        if self.is_empty():
            raise IndexError("lecture d'un élément dans une deque vide")
        return self._data[-1]

    def is_empty(self):
        # Retourne True si la deque est vide, sinon False
        return not self._head or self._head >= len(self._data)