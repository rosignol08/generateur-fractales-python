#importation des bibliothèques
from pystyle import *
from turtle import *

#définition des fonctions
from fonction import *

###texte cool du début###
d = {
  'a': ['  ■  ', ' ■ ■ ', '■   ■', '■■■■■', '■   ■'],
  'b': ['■■■ ', '■  ■', '■■■ ', '■  ■', '■■■ '],
  'c': [' ■■ ', '■  ■', '■   ', '■  ■', ' ■■ '],
  'd': ['■■■ ', '■  ■', '■  ■', '■  ■', '■■■ '],
  'e': ['■■■', '■  ', '■■ ', '■  ', '■■■'],
  'f': ['■■■', '■  ', '■■ ', '■  ', '■  '],
  'g': [' ■■ ', '■   ', '■ ■■', '■ ■ ', ' ■■ '],
  'h': ['■  ■', '■  ■', '■■■■', '■  ■', '■  ■'],
  'i': ['■', '■', '■', '■', '■'],
  'j': ['   ■', '   ■', '   ■', '■  ■', ' ■■'],
  'k': ['■  ■', '■ ■ ', '■■  ', '■ ■ ', '■  ■'],
  'l': ['■  ', '■  ', '■  ', '■  ', '■■■'],
  'm': ['■   ■', '■■ ■■', '■ ■ ■', '■   ■', '■   ■'],
  'n': ['■   ■', '■■  ■', '■ ■ ■', '■  ■■', '■   ■'],
  'o': [' ■■ ', '■  ■', '■  ■', '■  ■', ' ■■ '],
  'p': ['■■ ', '■ ■', '■■ ', '■  ', '■  '],
  'q': [' ■■ ', '■  ■', '■  ■', '■ ■■', ' ■■■'],
  'r': ['■■ ', '■ ■', '■■ ', '■ ■', '■ ■'],
  's': [' ■■ ', '■   ', ' ■■ ', '   ■', ' ■■ '],
  't': ['■■■■■', '  ■  ', '  ■  ', '  ■  ', '  ■  '],
  'u': ['■  ■', '■  ■', '■  ■', '■  ■', ' ■■ '],
  'v': ['■   ■', '■   ■', '■   ■', ' ■ ■ ', '  ■  '],
  'w': ['■   ■', '■   ■', '■   ■', '■ ■ ■', ' ■ ■ '],
  'x': ['■   ■', ' ■ ■ ', '  ■  ', ' ■  ', ' ■ ■ ', '■   ■'],
  'y': ['■   ■', ' ■ ■ ', '  ■  ', ' ■   ', '■    '],
  'z': ['■■■■', '  ■ ', ' ■  ', '■   ', '■■■■'],
  ' ': ['  ', '  ', '  ', '  ', '  '],
}


def ligne(c):
  mot = ""
  for i in range(5):
    for caractere in c:
      mot = mot + d[caractere][i] + " "
    print(mot)
    mot = ""


ligne('generateur de fractales')

#interface
Write.Print("générateur de fractales", Colors.blue_to_purple, interval=0.02)
Write.Print(
  " \n 0:fermer le programe 1: flocon classique  2: le flocon de Koch  3: triangle de sierpinski 4: une spirale 5: la fractales de l'arbre 6: une fractales inconnue \n",
  Colors.purple_to_red,
  interval=0.01)

choix = int(input("tapez vôtre choix"))

#pour fermer le programe
if choix == 0:
  print("fermeture du programe, aurevoir")
  quit()

#pour sélectionner les fonctions
elif choix == 1:
  longeur = int(input("Incérez la taille (je recommande 100 ou plus)"))
  niv = int(input("Incérez le niveau de détais (plus la valeur sera élevée plus le dessin sera petit, 3 semble être une bonne valeur)"))
  flocon(longeur, niv)

elif choix == 2:
  longeur = int(input("Incérez la taille (je recommande 700 ou plus)"))
  niv = int(input("Incérez le niveau de détais (plus la valeur sera élevée plus le dessin sera petit, 4 semble être une bonne valeur)"))
  koch_n(niv, longeur)

elif choix == 3:
  longeur = int(input("Incérez la taille (je recommande 700 ou plus)"))
  niv = int(input("Incérez le niveau de détais (plus la valeur sera élevée plus le dessin sera petit, 3 ou plus semble être une bonne valeur)"))
  triangle(longeur, niv)

elif choix == 4:
  longeur = int(input("Incérez la taille (je recommande 400 ou plus)"))
  niv = int(input("Incérez le niveau de détais (plus la valeur sera élevée plus le dessin sera petit, 5 semble être une bonne valeur)"))
  spirale(longeur, niv)

elif choix == 5:
  longeur = int(input("Incérez la taille (je recommande 700 ou plus)"))
  niv = int(input("Incérez le niveau de détais (plus la valeur sera élevée plus le dessin sera petit, 10 semble être une bonne valeur)"))
  arbre(niv, longeur)

elif choix == 6:
  print("les valeurs de cette fractale sont prédéfinies il faut quelques minutes pour voir le résultat final")
  arbre_bonus(11, 700)

else:
  print("cette touche n'est pas dans le choix veuillez redémarer le programe.")
  quit()

#pour que la fenêtre se ferme quand on clique dessus

window = Screen()
window.exitonclick()
