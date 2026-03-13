# version 2 du projet parc voiture
class Voiture:

    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print("Matricule:", self.matricule)
        print("Marque:", self.marque)
        print("Couleur:", self.couleur)
class Parc:

    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.listeVoitures:
            print("La voiture existe deja dans le parc")
            return

        if len(self.listeVoitures) >= self.capacite:
            print("Le parc est plein")
            return

        self.listeVoitures.append(voiture)
        print("Voiture ajoutee avec succes")

    def sortirVoiture(self, voiture):
        if voiture in self.listeVoitures:
            self.listeVoitures.remove(voiture)
            print("Voiture retiree")
        else:
            print("Voiture introuvable")

    def calculerNbrPlacesLibres(self):
        places = self.capacite - len(self.listeVoitures)
        return places

parc1 = Parc(1, "Toronto", 3)
v1 = Voiture("AAA111", "Toyota", "Rouge")
v2 = Voiture("BBB222", "Honda", "Noir")
v3 = Voiture("CCC333", "Ford", "Blanc")
parc1.entrerVoiture(v1)
parc1.entrerVoiture(v2)
parc1.entrerVoiture(v3)
print("Places libres:", parc1.calculerNbrPlacesLibres())
parc1.sortirVoiture(v2)
print("Places libres:", parc1.calculerNbrPlacesLibres())
