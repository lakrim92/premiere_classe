class joueur:
    def __init__(self, nom, vie, points):
        self._nom = nom
        self._vie = vie
        self._points = points

    # Getter et setter pour l'attribut name
    def get_nom(self):
        return self._nom

    def set_nom(self, nouveau_nom):
        self._nom = nouveau_nom

    # Getter et sette pour l'attribut vie
    def get_vie(self):
        return self._vie

    def set_vie(self, nouvelle_vie):
        self._vie = nouvelle_vie

    # Getter et setter pour l'attribut points
    def get_points(self):
        return self._points

    def set_points(self, nouveaux_points):
        self._points = nouveaux_points
    
    def descrition_joueur1(joueur):
        return f"Le joueur {joueur1.get_nom()} demarre avec {joueur1.get_vie()} % de vie et possède {joueur1.get_points()} de points."

    # Ajouter des points au joueur
    def ajouter_points(self, points_ajoutes):
        self._points += points_ajoutes

    # Tuer le joueur
    def kill(self):
        self._vie = 0

    # Ressusciter le joueur
    def ressusciter(self, points_de_vie):
        self._vie = points_de_vie

    # Description personnage
    def description_personnage(joueur):
        return f"{joueur.get_nom()} a {joueur.get_points()} points et {joueur.get_vie()} points de vie."

joueur1 = joueur("Georges", 100, 0)

print("___________________________________________________________________\n")
print(joueur1.descrition_joueur1())
print("___________________________________________________________________\n")

joueur1.ajouter_points(20)
print("Points du joueur apres ajout : ", joueur1.get_points())
print("___________________________________________________________________\n")

joueur1.kill()
print("Vie du joueur apres avoir été tué : ", joueur1.get_vie())
print("___________________________________________________________________\n")

joueur1.ressusciter(50)
print("Vie du joueur apres la resurrection : ", joueur1.get_vie())
print("___________________________________________________________________\n")

print(joueur1.description_personnage())
print("___________________________________________________________________\n")
