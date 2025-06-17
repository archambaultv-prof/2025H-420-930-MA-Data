class LIFO:
    def __init__(self):
        # Liste pour stocker les éléments de la pile
        # Nous n'avons pas besoin de pointeur pour une pile
        # car nous ajoutons et retirons toujours du sommet et
        # la liste Python gère automatiquement la taille.
        self._data = []

    def push(self, item):
        # Ajoute un élément au sommet de la pile
        self._data.append(item)

    def pop(self):
        # Retire et retourne l'élément au sommet de la pile
        if self.is_empty():
            raise IndexError("retrait d'un élément dans une pile vide")
        return self._data.pop()

    def is_empty(self):
        # Retourne True si la pile est vide, sinon False
        return not self._data

    def peek(self):
        # Retourne l'élément au sommet sans le retirer
        if self.is_empty():
            raise IndexError("lecture d'un élément dans une pile vide")
        return self._data[-1]
