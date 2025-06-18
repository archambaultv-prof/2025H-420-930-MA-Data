# Classe représentant un arbre général (chaque nœud peut avoir plusieurs enfants)
class Tree:
    def __init__(self, value):
        # Valeur du nœud courant
        self.value = value
        # Liste des sous-arbres/enfants
        self.children: list[Tree] = []

    # Ajoute un enfant à ce nœud
    def add_child(self, subtree):
        if isinstance(subtree, Tree):
            self.children.append(subtree)
        else:
            raise TypeError("add_child expects a Tree instance")

    # Représentation textuelle de l'arbre (pour affichage)
    def __repr__(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.value}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result

    # Applique une fonction à chaque valeur de l'arbre et retourne un nouvel arbre
    def map(self, func):
        """Retourne un nouvel arbre avec func appliquée à chaque valeur."""
        new_tree = Tree(func(self.value))
        for child in self.children:
            new_tree.add_child(child.map(func))
        return new_tree

    # Recherche le premier nœud dont la valeur satisfait un prédicat
    def find(self, predicate):
        """Retourne le premier nœud dont la valeur satisfait predicate."""
        if predicate(self.value):
            return self
        for child in self.children:
            result = child.find(predicate)
            if result is not None:
                return result
        return None

    # Convertit l'arbre en dictionnaire (utile pour la sérialisation)
    def to_dict(self):
        """Retourne un dictionnaire représentant l’arbre."""
        return {
            "valeur": self.value,
            "enfants": [child.to_dict() for child in self.children]
        }


    @classmethod
    def from_dict(cls, data):
        """Crée un arbre à partir d'un dictionnaire."""
        if not isinstance(data, dict) or "valeur" not in data or "enfants" not in data:
            raise ValueError("Données invalides pour la création de l'arbre")
        
        node = cls(data["valeur"])
        for child_data in data["enfants"]:
            node.add_child(cls.from_dict(child_data))
        return node

if __name__ == "__main__":
    # Exemple d'utilisation
    root = Tree("racine")
    child1 = Tree("enfant1")
    child2 = Tree("enfant2")
    child1.add_child(Tree("enfant1.1"))
    child1.add_child(Tree("enfant1.2"))
    root.add_child(child1)
    root.add_child(child2)

    print(root)
    print(root.map(lambda x: x.upper()))
    print(root.find(lambda x: x == "enfant1"))
    d = root.to_dict()
    print(d)
    print()
    print(Tree.from_dict(d))