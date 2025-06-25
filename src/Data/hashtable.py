from typing import Any


class HashTable:
    def __init__(self, size: int = 10):
        # Liste pour stocker les éléments (chaque élément est une liste pour gérer les collisions)
        self.table: list[list[tuple[int, Any]]] = [[] for _ in range(size)]
        # Nombre d'éléments stockés
        self.count = 0
        # Facteur de charge maximum avant redimensionnement
        self.max_load_factor = 0.75
    
    @property
    def size(self) -> int:
        # Taille de la table de hachage (calculée dynamiquement)
        return len(self.table)
    
    def _hash(self, key) -> int:
        # Fonction de hachage simple utilisant le modulo
        return hash(key) % self.size
    
    def _resize(self):
        # Redimensionne la table quand le facteur de charge est trop élevé
        old_table = self.table
        
        # Doubler la taille de la table
        self.table = [[] for _ in range(len(old_table) * 2)]
        self.count = 0  # Sera recalculé lors de la réinsertion
        
        # Réinsérer tous les éléments avec les nouveaux indices de hachage
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)  # Utilise put sans vérifier le facteur de charge
    
    def insert(self, key, value):
        # Ajoute ou met à jour une paire clé-valeur
        index = self._hash(key)
        bucket = self.table[index]
        
        # Vérifier si la clé existe déjà
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Mettre à jour la valeur existante
                return
        
        # Ajouter nouvelle paire clé-valeur si la clé n'existe pas
        bucket.append((key, value))
        self.count += 1
        
        # Vérifier si on doit redimensionner (facteur de charge = count / size)
        if self.count > self.size * self.max_load_factor:
            self._resize()
    
    def lookup(self, key):
        # Récupère la valeur associée à une clé
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        # Lever une exception si la clé n'existe pas
        raise KeyError(f"Clé '{key}' non trouvée")
    
    def delete(self, key):
        # Supprime une paire clé-valeur
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1  # Décrémenter le compteur
                return
        
        # Lever une exception si la clé n'existe pas
        raise KeyError(f"Clé '{key}' non trouvée")
    
    def contains(self, key) -> bool:
        # Vérifie si une clé existe dans la table
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return True
        
        return False
    
    def _load_factor(self) -> float:
        # Retourne le facteur de charge actuel
        return self.count / self.size if self.size > 0 else 0
    
    def __str__(self) -> str:
        # Représentation textuelle de la table de hachage
        result = f"HashTable (size: {self.size}, count: {self.count}, load factor: {self._load_factor():.2f}):\n"
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f"  Index {i}: {bucket}\n"
        return result

if __name__ == "__main__":
    # Exemple d'utilisation de la table de hachage
    ht = HashTable()
    print(ht)
    for i in range(20):
        # Ajouter des éléments à la table de hachage
        ht.insert(f"key{i}", f"value{i}")
        print(ht)