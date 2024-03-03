# PREMIERE CLASSE

Ce projet vise à démontrer l'utilisation des classes en Python pour modéliser un joueur avec des attributs tels que le nom, les points de vie et les points.

## Instructions

1. **Création du projet sur GitLab :**
   - Créez un nouveau projet sur GitLab intitulé "PREMIERE CLASSE".

2. **Clonage du projet en local :**
   - Clonez le projet GitLab localement en utilisant la commande `git clone https://github.com/lakrim92/premiere_classe`.

3. **Environnement virtuel :**
   - Créez un environnement virtuel Python dans le dossier du projet pour isoler les dépendances. Vous pouvez utiliser `python -m venv venv` pour cela.

4. **Classe Joueur :**
   - Implémentez une classe `Joueur` avec un constructeur prenant trois attributs : nom (str), vie (int) et points (int).

5. **Getters et Setters :**
   - Ajoutez des méthodes getters et setters pour chaque attribut de la classe `Joueur` afin de contrôler l'accès et la modification des attributs.

6. **Méthodes supplémentaires :**
   - Ajoutez des méthodes pour ajouter des points au joueur, pour le tuer et pour le ressusciter.

7. **Description du personnage :**
   - Créez une fonction pour décrire en une phrase les attributs du joueur, notamment son nom, ses points de vie et ses points.

## Exemple d'utilisation

Voici un exemple d'utilisation de la classe `Joueur` :

```python
joueur1 = Joueur("Alice", 100, 0)

joueur1.ajouter_points(20)
print("Points du joueur après ajout :", joueur1.get_points())

joueur1.kill()
print("Vie du joueur après avoir été tué :", joueur1.get_vie())

joueur1.ressusciter(50)
print("Vie du joueur après la résurrection :", joueur1.get_vie())

print(description_personnage(joueur1))
