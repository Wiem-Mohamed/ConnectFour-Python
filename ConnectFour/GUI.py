from tkinter import *
import tkinter as tk
from Jeu import *
from PIL import ImageTk,Image
from turtle import *
import os



tour=1 
jeu_fini=False
cmt=0
# ****************************Les fonctions***********************
def fin_jeu():
 global canvas,main
 canvas.delete("all")
 f=Frame(width='600',height='600',bg='#EAC7C7')
 f.place(x=0,y=0)
 ph='   Jeu fini! \n Félicitations le joueur '+ str(tour)+' est le vainqueur '
 Label(f,width=600,text=ph,anchor='nw' ,font=('verdana',20),bg='#EAC7C7').place(x=5,y=10)
 l=Label(f,image=img,anchor='nw').place(x=150,y=150)
 Button(main, text ="Fermer",fg='black',bg='white',padx=10,pady=10,font=('verdana',10), command = main.destroy).place(x=250,y=400)

def cliquer_sur(event):
    global canvas,tour,jeu_fini,cmt
    cmt+=1
    if cmt==42:
      main.destroy()
    if (0<=event.x<=85):
        indice=0
    else:
        indice=(event.x//80)
    if tour==1:
        if jeu.grille.coup_gagnant(jeu.joueurs[1]):
         fin_jeu()
        jeu.grille.remplir_grille(indice,jeu.joueurs[0])
        jeu.grille.affiche()
        for i in range(6):
          for j in range(7):
            if jeu.grille.grille[i,j]==1:
                canvas.create_oval(j*85,i*85,j*85+85,i*85+85,fill='white')
        
        tour=2
    else:
      if jeu.grille.coup_gagnant(jeu.joueurs[0]):
          fin_jeu()
      jeu.grille.remplir_grille(indice,jeu.joueurs[1])
      jeu.grille.affiche()
      for i in range(6):
       for j in range(7):
        if jeu.grille.grille[i,j]==2:
          canvas.create_oval(j*85,i*85,j*85+85,i*85+85,fill='black')
      
          
      tour=1
def handler1():
  global canvas
  f1.destroy()
  f2.destroy()
  canvas=Canvas(main,width=600,height=600,bg='#A0C3D2')
  canvas.place(x=0,y=0)
  for i in range(8):
    canvas.create_line(85*i,0,85*i,85+5*85)
  for i in range(7):
    canvas.create_line(0,85*i,85+7*85,85*i)
  canvas.bind('<Button-1>',cliquer_sur)   

# ***********************La création de l'interface*********************  
main=Tk()
main.geometry("600x600+900+100")
main.title("Jeu puissance 4")
main.resizable(False,False)
f1=Frame(width='290',height='599',bg='#A0C3D2')
f1.place(x=1,y=1)
canvas=Canvas(f1,width=290,height=599,bg="#A0C3D2")
canvas.create_text(10,5,width=280,text= "Le jeu puissance 4 est une grille de jeu avec :\n * 2 réceptacles \n * 42 emplacements \n * 21 pions noirs \n * 21 pions blancs \n * 2 joueurs \n Les joueurs choisissent chacun une couleur de pion. Le joueur qui commence met un premier pion dans l’une des couleurs de son choix. Le jeton tombe au bas de la colonne. Son adversaire insère à son tour un jeton, le but étant de contrer l’autre au fur et à mesure du jeu pour qu’il n’arrive pas à former une rangée de 4 jetons de sa couleur, dans un sens, comme dans l’autre et en diagonale.\n Le gagnant est le joueur qui arrive à aligner 4 pions horizontalement ou verticalement ou diagonalement. La partie est nulle et recommencée si aucun des deux n’y est arrivé et que la grille est remplie.",anchor='nw' , fill="black",font=('verdana',10))
canvas.pack()
f2=Frame(width='305',height='600',bg='#EAC7C7')
f2.place(x=293,y=1)
image_folder = 'images'
image_path = os.path.join(image_folder, 'king.png')
image1_path = os.path.join(image_folder, 'photo.png')
img = ImageTk.PhotoImage(Image.open(image_path))
img1 = ImageTk.PhotoImage(Image.open(image1_path))
label1 = Label(f2, image=img1, anchor='nw')
label1.place(x=1, y=1)
b2=Button(f2,text='commencer le jeu',fg='black',bg='white',padx=10,pady=10,font=('verdana',10),command=handler1)
b2.place(x=100,y=500)
main.mainloop()
