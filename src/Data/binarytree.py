# Classe représentant un nœud de l'arbre binaire
class Node:
    def __init__(self, val):
        # Valeur du nœud
        self.val = val
        # Sous-arbre gauche
        self.left: Node | None = None
        # Sous-arbre droit
        self.right: Node | None = None

# Classe représentant l'arbre binaire de recherche
class BinarySearchTree:
    def __init__(self):
        # Racine de l'arbre
        self.root: Node | None = None

    # Insère une valeur dans l'arbre
    def insert(self, val):
        def _insert(node: Node | None, val) -> Node:
            if node is None:
                return Node(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            # Si val == node.val, on ne fait rien (pas de doublons)
            return node
        self.root = _insert(self.root, val)

    # Supprime une valeur de l'arbre
    def delete(self, val):
        def _delete(node, val):
            if node is None:
                return None
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                # Cas 1: pas d'enfant
                if node.left is None and node.right is None:
                    return None
                # Cas 2: un seul enfant
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Cas 3: deux enfants
                # On trouve le successeur (plus petit dans le sous-arbre droit)
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                node.right = _delete(node.right, succ.val)
            return node
        self.root = _delete(self.root, val)

    # Vérifie si une valeur est présente dans l'arbre
    def contains(self, val):
        def _contains(node, val):
            if node is None:
                return False
            if val == node.val:
                return True
            elif val < node.val:
                return _contains(node.left, val)
            else:
                return _contains(node.right, val)
        return _contains(self.root, val)

    # Calcule la hauteur de l'arbre
    def height(self):
        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
