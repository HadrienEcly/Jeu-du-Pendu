import random
from tkinter import *
Mots_bases = ["LIRE","TRAVAILLER","DORMIR","ECRIRE","CHARLOTTE","CLEMENTINE","XYLOPHONE","FENETRE","HYPOTENUSE","BACCALAUREAT","HALLYDAY","ELEPHANT","HIPPOPOTAME","RHINOCEROS","MOLIERE","DESCARTES","ZEBRE","GIRAFE","PIANO","EXAMEN","VIE","POSTE","TABLEAU","ALIEN","PRISE","ETRANGER","INFORMATIQUE","SCIENCE","MAMMOUTH","MANGER","PULLOVER","LUNETTES","CREPES","HARICOT","ARTICHAUT","ANOMALIE","COCCINELLE","TRAMPOLINE","PAMPLEMOUSSE","CUISINE","DANSER","GUITARE","ROMAN","MUSIQUE","MONTAGNE","SKIER","KOALA","PARESSEUX","CLIMATIQUE","BROUETTE"]
#Cette liste contient tous les mots que le joueur pourra chercher.


##FONCTIONS##

def Chiffrer(x): #Chiffrer permet de transformer le Mot choisi par la machine en code ascii, plus precisement pour le ranger dans une liste.
    l = len(x) #Prend la longueur de la variable
    list=[]  #creation d'une liste
    for i in range(0,l): #Transforme les lettres en code ascii et les insere dans une liste
        p = x[i] #prend la lettre numero i du mot
        z = ord(p) #transforme en ascii
        list.append(z)  #l'ajoute a la liste 
    return(list)

def Pendu(x) : #en fonction du nombre d'erreurs, un certain dessin du pendu s'affiche
    if x >= 1:
        Canvas1.create_line(50,400,200,400,fill='black',width=4) #Premiere erreur (fenetre dans laquelle on cree la ligne, coordonees, couleur, largeur)
        if x >= 2:
            Canvas1.create_line(125,400,125,50,fill='black',width=4) #Seconde erreur
            if x >= 3:
                Canvas1.create_line(125,50,350,50,fill='black',width=4) #Troisieme erreur
                if x >= 4:
                    Canvas1.create_line(125,100,175,50,fill='black',width=4) #Quatrieme erreur
                    if x >= 5:
                        Canvas1.create_line(350,50,350,100,fill='black',width=4) #Cinquieme erreur
                        if x >= 6:
                            Canvas1.create_oval(325,100,375,150,fill='',width=4) #Sixieme erreur
                            if x >= 7:
                                Canvas1.create_line(350,150,350,260,fill='black',width=4) #Septieme erreur
                                if x >= 8:
                                    Canvas1.create_line(350,185,400,145,fill='black',width=4) #Huitieme erreur
                                    Canvas1.create_line(350,185,300,145,fill='black',width=4)
                                    if x >= 9:
                                        Canvas1.create_line(350,260,400,320,fill='black',width=4) #Neuvieme erreur
                                        Canvas1.create_line(350,260,300,320,fill='black',width=4) 
    return()
    
def lire_lettre(lettre): #lire_lettre verifie si la lettre mise en variable respecte certaines conditions  (deja proposee, fausse, vraie)
    global echec, reussi #global permet de rendre echec et reussi en variable valable pour tout le programme
    if lettre in propositions: #si la lettre a deja ete proposee
        Texte1.config(text="Cette lettre a deja ete proposee.",bg="#ffcc99") #on affiche le texte dans le cadre prevu a cet effet
    elif lettre in Lettres_Justes : #Si la lettre est juste, on veut connaitre toutes les fois ou la lettre est en double et leurs positions:
        propositions.append(lettre) #comme elle a ete proposee, elle s'ajoute a la liste des lettres deja proposee pour ne plus la retenter
        for i,e in enumerate(Lettres_Justes): #On enumere les lettres presentes dans Lettres_Justes (qui deviennent e) et i correspond a leur position
            if e == lettre : #e est une variable. il prend la place de chaque lettre dans le mot. e = la lettre choisie (si x est dans le mot, et/ou en plusieurs exemplaires)
                    Canvas2.create_text(x3[i],25,width=1,text=chr(e)) #ce cadre permet d'afficher la lettre e a la position i
                    Texte1.config(text="Cette lettre est présente dans le mot",bg="#8fe38d") #on affiche le texte correspondant
                    reussi = reussi + 1 #le compte de lettres reussites
        if reussi == t : #si le nombre de reussi correspond a la longueur du mot
            Texte1.config(text="Fin de la partie, vous avez gagné") #on affiche que l'on a gagne
            for i in range(26): #et pour le bouton des 26 lettres
                bouton[i].config(state = DISABLED) #on le desactive
            Canvas2.config(bg="#8fe38d")  #le fond du mot trouve devient vert
    else: #sinon, si la lettre n'est pas dans le mot
        Texte1.config(text="Cette lettre n'est pas dans le mot",bg="#e38d8d") #on affiche le texte correspondant
        propositions.append(lettre) #comme elle a ete proposee, elle s'ajoute a la liste des lettres deja proposee pour ne plus la retenter
        echec = echec + 1 #a chaque lettre fausse on ajoute un echec
        Pendu(echec) #cela affiche le dessin du pendu correspondant au nombre d'echec
        if echec == 9: #si l'echec est egal a 9, on perd
            Texte1.config(text=("Fin de la partie, vous avez perdu, le mot était")) #On affiche que l'on a perdu et le mot qui etait a trouver
            for i in range(26): # on desactive le bouton des 26 lettres
                bouton[i].config(state = DISABLED)
            for i in range(t): #on affiche en rouge le mot qui etait a deviner
                Canvas2.create_text(x3[i],25,width=1,text=Mot_Final[i])
                Canvas2.config(bg="#e38d8d")
    return(lettre)


##PROGRAMME PRINCIPAL##

#Creation de la fenetre principale avec titre et couleur.
fenetre = Tk()
fenetre.title('Le Pendu')
fenetre["bg"] = "#ffe2c5"

defaite = 0
victoire = 0
Partie_Joue = 0
reussi = 0 #definition de reussi
resultat = 0
echec = 0
reussi = 0

#Initialisation de la partie
propositions = [] #creation de la liste des propositions entrees au prealable par l'utilisateur
Nbr = random.randint(0,49) #choisit un nombre aléatoire entre 0 et 49 (car il y a 50 mots dans la liste Mots_bases)
Mot_Final = Mots_bases[Nbr] #la place Nbr du mot dans la liste devient Mot_Final
Lettres_Justes = Chiffrer(Mot_Final) #transforme en ascii
t = len(Lettres_Justes) #longueur du mot permettant de savoir lorsque la partie est terminee


#Canvas1 correspond au pendu, fait a  l'aide de lignes et d'un ovale.
Canvas1=Canvas(fenetre, width=500, height=450,bg='ivory')
Canvas1.pack(side=TOP, padx=5, pady=5)

#Texte1 correspond au texte nous indiquant la marche à suivre pour jouer au jeu.
Texte1 = Label(fenetre,width=50, height=1, borderwidth='4', state="disabled",bg="#ffcc99",relief=RIDGE)
Texte1.pack(padx=10, pady=10)
Texte1.config(text="Rentrez une lettre")

#Cadre1 est le cadre dans lequel se trouve les lettres de l'alphabet.
cadre1 = Frame(fenetre,bg="#ffcc99", width=100, height=100, borderwidth=2) #cadre avec ses dimensions, couleurs pour rentrer les lettres
cadre1.pack(padx=10, pady=10)
bouton = [0]*26
for i in range(26):
    bouton[i] = Button(cadre1,text=chr(i+65),command=lambda x=i+65:lire_lettre(x))
    bouton[i].pack(side=LEFT)
    
#Cette partie sert a creer des coordonees pour les lettres selon la longueur du mot.
w = 100 + t*50 #
Canvas2=Canvas(fenetre, width=w, height=60,relief=RIDGE,bg="#ffcc99",borderwidth = "4") #cadre avec ses dimensions, couleurs pour rentrer les lettres
Canvas2.pack(padx=10, pady=10)
x1 = 10
x2 = 40
x3 = []
for i in range (0,t): #pour la longueur des tirets
    x1 = x1 + 50 
    x2 = x2 + 50 
    C = (x1+x2)/2 #on trouve le milieu des tirets
    x3.append(C)
    Canvas2.create_line(x1,40,x2,40,fill='gray',width=4)

#Bouton1 correspond au bouton pour fermer la fenêtre.
cadre2 = Frame(fenetre,width = 40, height=20,bg="#ffe2c5")
cadre2.pack(padx=5, pady = 5)
Bouton1 = Button(cadre2, text="Quitter",bg="#ffcc99",command=fenetre.destroy)
Bouton1.pack(side=LEFT,padx=5, pady = 5)

fenetre.mainloop()
