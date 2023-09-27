import numpy as np

class Grille:
  def __init__(self):
    self.grille=np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
  def affiche(self):
    for i in range(6):
     for j in range(7):
      print(str(self.grille[i][j]),", ",end="")
     print()
    
  def coup_gagnant(self,joueur):
    x=joueur.getId()
    # vérifier les lignes horizontales
    for j in range(4):
      for i in range(6):
        if self.grille[i,j]==x and self.grille[i,j+1]==x and self.grille[i,j+2]==x and self.grille[i,j+3]==x:
          return True
    # vérifier les lignes verticales
    for j in range(7):
      for i in range(3):
        if self.grille[i,j]==x and self.grille[i+1,j]==x and self.grille[i+2,j]==x and self.grille[i+3,j]==x:
          return True
    # verifier le diagonal principal
    for j in range(4):
      for i in range(3):
        if self.grille[i,j]==x and self.grille[i+1,j+1]==x and self.grille[i+2,j+2]==x and self.grille[i+3,j+3]==x:
          return True
      # verifier le diagonal secondaire
    for j in range(4):
      for i in range(3,6):
        if self.grille[i,j]==x and self.grille[i-1,j+1]==x and self.grille[i-2,j+2]==x and self.grille[i-3,j+3]==x:
          return True
    return False
  def remplir_grille(self,indice,joueur):
    x=joueur.getId()
    i=5
    while(i>=0):
            if (self.grille[i,indice]==0):
                self.grille[i,indice]=x
                break
            else:
                i=i-1
  