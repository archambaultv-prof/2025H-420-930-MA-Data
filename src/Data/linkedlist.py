# Classe représentant un nœud de la liste chaînée
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next: LinkedListNode | None  = None

# Classe représentant la liste chaînée
class LinkedList:
    def __init__(self):
        # Pointeur vers la tête de la liste
        self.head: LinkedListNode | None = None
        # Pointeur vers la queue de la liste
        self.tail: LinkedListNode | None = None
        # Taille de la liste
        self.size = 0

    # Insère un élément en tête de liste
    def insert_head(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # Insère un élément en queue de liste
    def insert_tail(self, value):
        new_node = LinkedListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Insère un élément à l'index i
    def insert_mid(self, i: int, value):
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")
        new_node = LinkedListNode(value)
        if i == 0:
            self.insert_head(value)
        elif i == self.size:
            self.insert_tail(value)
        else:
            current = self.head
            for _ in range(i - 1):
                current = current.next # type: ignore
            new_node.next = current.next # type: ignore
            current.next = new_node # type: ignore
            self.size += 1

    # Supprime et retourne la valeur en tête de liste
    def delete_head(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_value
    
    # Supprime et retourne la valeur en queue de liste
    def delete_tail(self):
        if self.tail is None:
            raise IndexError("Cannot delete from an empty list")
        if self.head == self.tail:
            removed_value = self.head.value # type: ignore
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail: # type: ignore
                current = current.next # type: ignore
            removed_value = self.tail.value
            current.next = None # type: ignore
            self.tail = current
        self.size -= 1
        return removed_value

    # Retourne True si la liste est vide, sinon False
    def is_empty(self):
        return self.size == 0

    # Retourne la taille de la liste
    def __len__(self):
        return self.size