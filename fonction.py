from turtle import *  #pour effectuer les dessin
import turtle
from math import *  #pour les opération en sqrt
from math import sqrt


#Pour centrer des fractale
def decale_vers_la_gauche (largeur) :#décale vers la gauche de "largeur" pixels
    left (180)
    penup ()
    forward(largeur)
    pendown ()
    left (180)
def decale_vers_le_haut(hauteur):#décale vers le haut de "hauteur" pixels
    left (90)
    penup ()
    forward (hauteur)
    pendown ()
    right (90)

#fractal flocon
def flocon(longeur, niv):
  if niv == 0:
    pass
  else:
    for i in range(6):
      forward(longeur)
      flocon(longeur / 3, niv - 1)
      backward(longeur)
      left(60)


#spirale instpiée du nombre d'or
def spirale(longeur, niv):
  hideturtle()
  speed(20)
  if niv == 0:
    for i in range(4):
      forward(longeur)
      left(90)
  else:
    longeur_petit_carre = longeur / sqrt(2)
    for i in range(4):
      forward(longeur)
      right(90)
    left(45)
    spirale(longeur / sqrt(2), niv)
    right(45)
    forward(longeur)
    left(45)
    spirale(longeur / sqrt(2), niv)
    forward(longeur / sqrt(2))
    left(45)


#arbre de Pythagore
#def arbrepyt(longeur, niv):
#  hideturtle()

#  def caree(longeur):
#    for i in range(4):
#      forward(longeur)
#      left(90)

#  if niv == 0:
#    caree(longeur)
#  else:
#    for i in range(niv):
#      caree(longeur)
#      right(135)
#      caree(longeur / sqrt(2))
 #     left(135)
 #     forward(longeur)
 #     right(135)
 #     caree(longeur / sqrt(2))
 #     forward(longeur / sqrt(2))

#window = turtle.Screen()
#arbrepyt(150,2)
#window.exitonclick()

#Meme que sierpinski
def triangle(longeur, niv):
  speed(1000)
  if niv == 0:
    forward(longeur)
    left(120)
    forward(longeur)
    left(120)
    forward(longeur)
    left(120)
  else:
    triangle(longeur / 2, niv - 1)
    forward(longeur / 2)
    triangle(longeur / 2, niv - 1)
    backward(longeur / 2)
    left(60)
    forward(longeur / 2)
    right(60)
    triangle(longeur / 2, niv - 1)
    left(60)
    backward(longeur / 2)
    right(60)

#arbre fractal
color('#3f1905')
def arbre(n,longueur):
  if n == 0:
    color('green')
    forward(longueur)  # avance
    backward(longueur)  # recule
    color('#3f1905')
  else:
    speed(100000)
    width(n)
    forward(longueur / 3)  #avance
    left(30)  # tourne vers la gauche de angle degrés
    arbre(n - 1, longueur * (2 / 3))
    right(60)  # tourne vers la droite de angle degrés
    arbre(n - 1, longueur * (2 / 3))
    left(30)  # tourne vers la gauche de angle degrés
    backward(longueur / 3)  # recule

#hideturtle()  # cache la tortue
#up()  # lève le stylo
#right(90)  # tourne de 90 degrés vers la droite
#forward(300)  # avance de 300 pixels
#left(180)  # fait un demi-tour
#down()  # pose le stylo
#arbre(11, 700)  # exécute la macro
#showturtle()  # affiche la tortue

#fractal de KOCH
def koch_n(n, longueur):
    speed(0)#speed du traceur au maximum
    pencolor ("blue")#couleur du stylo 
    ht() #masque la flèche qui trace
    if n==0:
      forward (longueur)
    else:
      koch_n(n-1, longueur/3)
      left (60) 
      koch_n(n-1, longueur/3)
      right (120)
      koch_n(n-1, longueur/3)
      left (60)
      koch_n(n-1, longueur/3)
decale_vers_la_gauche (300)
decale_vers_le_haut(-200)





#Fractal de sierpinski
def sierpinski(niv, longueur):
  speed (0)#speed du traceur au maximum
  pencolor("black")#couleur du stylo 
  shape ("turtle")#gadiet
  ht ()#masque la flèche qui trace
  if niv==0:
    for i in range (0,3):
      forward (longueur)
      left (120)
  if niv>0:
    sierpinski (niv-1, longueur/2)
    forward (longueur/2)
    sierpinski (niv-1, longueur/2)
    backward(longueur/2)
    left (60)
    forward (longueur/2)
    right (60)
    sierpinski (niv-1,longueur/2)
    left (60)
    backward (longueur/2)
    right (60) 


#window = turtle.Screen()
#triangle(100,3)
#window.exitonclick()
#  decale_vers_la_gauche (300)
#  decale_vers_le_haut(-200)
#  showturtle()  # affiche la tortue

def arbre_bonus(n, longueur):
        left(90)
        if n == 0:
                color('green')
                forward(longueur)  # avance
                backward(longueur)  # recule
                color('#3f1905')
        else:
                speed(1000)
                width(n)
                forward(longueur / 3)  #avance
                left(30)  # tourne vers la gauche de angle degrés
                arbre_bonus(n - 1, longueur * 2 / 3)
                right(60)  # tourne vers la droite de angle degrés
                arbre_bonus(n - 1, longueur * 2 / 3)
                left(30)  # tourne vers la gauche de angle degrés
                backward(longueur / 3)  # recule
