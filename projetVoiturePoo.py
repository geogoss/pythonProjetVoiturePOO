
#  Dans cet exercice sur la programmation orientée objet, vous allez devoir créer une classe Voiture, 
# qui doit contenir plusieurs attributs et méthodes afin de la faire fonctionner correctement.

#1) Créez une classe voiture avec un attribut essence qui est égal à 100.

#2) Créez une méthode afficher_reservoir qui affiche le nombre de litres d’essence restant 
# (La voiture contient x litres d’essence).

#3) Créez une méthode roule avec un paramètre km (kilomètre) qui va faire avancer 
# la voiture et vider petit à petit le réservoir. On considère une consommation de 5L pour 100km, 
# l’opération mathématique pour déterminer le nombre de litres d’essence nécessaire en 
# fonction du nombre de kilomètres est donc :
# (km * 5) / 100

#4) Si le réservoir est vide quand on essaie de rouler, afficher 
# la phrase : Vous n'avez plus d'essence, faites le plein ! et empêchez la voiture d’avancer.

#5) Si la jauge d’essence descend en dessous de 10L, affichez la phrase : Vous n'avez bientôt plus d'essence !

#6) Créez une méthode faire_le_plein qui remet le niveau d’essence à 100L et qui affiche la phrase Vous pouvez repartir !

class Voiture:
    def __init__(self, marque, essence):
        self.marque = marque
        self.essence = essence
        
    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")
    
    def roule(self, km):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        else:   
            self.essence = self.essence - (km*5)/100
            if self.essence < 0:
                print("Oups vous êtes tombé en panne, faite le plein !!!")
            elif self.essence <= 10:
                print(f"Attention, il ne vous reste presque plus d'essence ! \nLa {self.marque} à consommé {(km*5/100)} litres d'essence. \nIl lui reste {self.essence} litres.")
            else:
                print(f"La {self.marque} à consommé {(km*5/100)} litres d'essence. \nIl lui reste {self.essence} litres.")

    def faire_le_plein(self):
        while True:
            euro = int(input("Combien d'euro voulez vous mettre pour votre essence ?"))
            quantite_essence = euro*2
            if self.essence + quantite_essence > 100:
                print(f"Votre réservoire n'est pas aussi grand ! \nVous pouvez mettre {(100 - self.essence)/2} euros max ")
                continue
            else:
                self.essence = self.essence + quantite_essence
                print(f"Vous venez de faire un plein de {quantite_essence} litres. \nVotre réservoir contient {self.essence} litres ")
                break
            


voiture1 = Voiture("Porsche", 100)
print(voiture1.marque)
print(voiture1.essence)
Voiture.afficher_reservoir(voiture1)
Voiture.roule(voiture1, 1000)
Voiture.roule(voiture1, 100)
Voiture.roule(voiture1, 100)
Voiture.roule(voiture1, 400)
Voiture.roule(voiture1, 300)
Voiture.faire_le_plein(voiture1)





