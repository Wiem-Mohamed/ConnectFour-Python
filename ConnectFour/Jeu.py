from Grille import *
from Joueur import *
class Jeu:
  def __init__(self) :
    self.joueurs=[Joueur(1,"blanc"),Joueur(2,"noir")]
    self.grille=Grille()   
jeu=Jeu()