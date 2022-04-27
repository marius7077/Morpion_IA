class Morpion:

    def __init__(self):
        self.plateau = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
        self.J1 = "X"
        self.J2 = "O"

    def jeu(self):
        pass

    def affiche_Plateau(self):
        for i in range(3):
            print("|", end="")
            print('|'.join(self.plateau[i]), end="")
            print("|")

    def test_fin_jeu(self, joueur):
        for i in range(3):
            if self.plateau[i].count(joueur) == 3:
                return joueur
        for i in range(3):
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] == joueur:
                return joueur

    def jouer(self, joueur):
        x = input("Pour l'abscisse entrer un nombre en 1 et 3")
        y = input("Pour l'ordonné entrer un nombre en 1 et 3")
        self.plateau[int(x)][int(y)] = joueur


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    morpion = Morpion()
    morpion.affiche_Plateau()
    print(morpion.test_fin_jeu(morpion.J2))
