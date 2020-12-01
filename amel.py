import random
import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
from random import randrange
from matplotlib import pyplot
seed(1)

#<<<<<<< HEAD

#création de la liste qui contient les positions du déplacement
x=[0]
#nombre de pas faits par la personne alcoolisée
N = int(input("number of steps : "))
nbonhomme = int(input("nombre de personne que vous voulez faire marcher : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
# création d'une matrice de zeros qui deviendront bientot des heros (oui je sais c'est nul mais je suis fatiguee ok ?)
stock =np.zeros((nbonhomme,N+1))

stockr =np.zeros((nbonhomme,N+1))
stocka =np.zeros((nbonhomme,N+1))
stockra =np.zeros((nbonhomme,N+1))


#np.random.normal prend une valeur dans une fonction normale centrée (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas

# création de la fonction qui repousse quand on rencontre un mur
def reflect(xn,murdroite,murgauche):
    if xn > murdroite :
        xn=murdroite - abs(murdroite - xn)
    if xn < murgauche :
        xn = murgauche + abs(murgauche - xn)
    return(xn)


def absorbing(xn, murdroite, murgauche,xmaxlife):
    if xn>murdroite :
        xn=murdroite
        xmaxlife = 0

    if xn<murgauche :
        xn=murgauche
        xmaxlife = 0

    return(xn,xmaxlife)


def reflectabsord(N,xn,xmaxlife):
    #on definit p pour qu'il y ait une chance sur deux
    p=np.random.random()
    if 0.5 < p :
        xn=reflect(xn, murdroite, murgauche)
    if 0.5 > p :
        xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
    return(xn,xmaxlife)

listpersonneviepas=[0]*N
for i in range(nbonhomme) :
    #il faut remettre a 0 la liste a chaque fois pour que chaque bonhomme
    #commence a 0 pareil pour xmaxlife si le bonhomme est direct mort
    x = [0]
    xmaxlife=1
    listreflect=[0]
    listabsorb=[0]
    listreflectabsord=[0]
    #p sert à ce qu'il y ait une chance sur 3 pour qu'un bonhomme prenne
    #un chemin ou un autre une fois qu'il choisit une mode il reste dedans
    p=np.random.choice([1,2,3])
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx
        #si on ne fait pas xmaxlife différent de 0 alors la personne risque
        #de continuer a bouger alors qu'elle est censée être absorbée
        if xmaxlife!=0:
            #ajoute a chaque fois que quelqu'un arrive au pas z en vie 1 au
            #nombre de survivants à ce pas
            listpersonneviepas[z]+=1
            xn,xmaxlife=reflectabsord(N,xn,xmaxlife)
        #si jamais le bonhomme est déjà mort alors il faut qu'il reste sur le
            #mur donc qu'il continue d'emprunter le chemin d'absorption
        else:
            xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        x.append(xn)

        dx=np.random.normal()
        xn = listabsorb[-1]+ dx
        xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        listabsorb.append(xn)

        dx=np.random.normal()
        xn = listreflect[-1]+ dx
        xn=reflect(xn,murdroite,murgauche)
        listreflect.append(xn)

        #ajout a la liste x comprenant les coordonnées des pas du bonhomme z

    #ajout de la liste des pas finis du bonhomme z dans la matrice
    stock[i,:] = x
    stocka[i,:]=listabsorb
    stockr[i,:]=listreflect
    stockra[i,:]=listreflectabsord

plt.subplot(211)

dureedevietot=0
for numerobonhomme in range(nbonhomme) :
    x=stock[numerobonhomme]
    #x=stocka[numerobonhomme]
    #x=stockr[numerobonhomme]
    #x=stockra[numerobonhomme]
    #création d'une liste vide ou on va rentrer les
    #pas qu'il a fait en étant vivant
    bonvivant=[]
    for pas in range(len(x)):
        if x[pas]!=murdroite and x[pas]!=murgauche:
            bonvivant.append(x[pas])

        if numerobonhomme%2==0:
            plt.plot(x[pas],numerobonhomme,'ob')
        else:
            plt.plot(x[pas],numerobonhomme,'or')
        plt.title("Déplacement du bonhomme")
        plt.xlabel("Position de chaque pas entre les deux murs")
        plt.ylabel("Numéro des bonhommes")




plt.figure(1)
#plt.subplot permet de séparer la fenêtre ou on affiche les graphes en plusieurs parties. En l'occurence elle sépare en 2 parties
plt.subplot(212)
#calcul de la moyenne de la position des bonhommes à chaque pas pour chaque chemin
moydureedevie=stock.mean(axis=0)
a=stocka.mean(axis=0)
r=stockr.mean(axis=0)


#on affiche en rouge le chemin absorption ou reflexion, en bleu reflexion, en vert absorption
plt.plot(moydureedevie,"r--", label = "Chemin absorption ou reflexion")
plt.plot(a,'g--', label = "Chemin absorption")
plt.plot(r,'b--', label = "Chemin reflexion")
plt.legend()


#donne l'abcisse et l'ordonnée du graphique
plt.axis([0,N,murgauche,murdroite])

#legende
plt.xlabel('Nombre de pas')
plt.ylabel('Average position of the walkers')

#on affiche le graph
plt.show()



#la figure 2 est l'affichage du nombre de survivants en fonction du nombre de pas
plt.figure(2)
plt.plot(listpersonneviepas,'^k:')
plt.title("Nombre de survivants en fonction du nombre de pas")
plt.xlabel("Nombre de pas")
plt.ylabel("Nombre de survivants")
plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273


