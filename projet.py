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

#creation de la liste qui contient les positions du deplacement
x=[0]
#nombre de pas fait par la personne alcoolisee
N = int(input("number of steps : "))
nbonhomme = int(input("nombre de personne que vous voulez faire marcher : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
# creation d'une matrice de zeros qui deviendront bientot des heros (oui je sais c'est nul mais je suis fatiguee ok ?)
stock =np.zeros((nbonhomme,N+1))
stockr =np.zeros((nbonhomme,N+1))
stocka =np.zeros((nbonhomme,N+1))


#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas

# creation de la fonction qui repousse quand on rencontre un mur
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


for i in range(nbonhomme) :
	x = [0]
	xmaxlife=1
	listreflect=[0]
	listabsorb=[0]
	for pas in range(N):
		dx=np.random.normal()
		xn = listabsorb[-1]+ dx
		xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
		listabsorb.append(xn)

		dx=np.random.normal()
		xn = listreflect[-1]+ dx
		xn=reflect(xn,murdroite,murgauche)
		listreflect.append(xn)

#ajout de la liste des pas finies du bonhomme z dans la matrice
	stocka[i,:] = listabsorb
	stockr[i,:] = listreflect

a=stocka.mean(axis=0)
r=stockr.mean(axis=0)

plt.plot(a,'g--')
plt.plot(r,'b--')



plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273


