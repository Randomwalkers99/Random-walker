# Créé par aaugr, le 01/12/2020 en Python 3.7
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
#nombre de pas faits par la personne
N = int(input("number of steps : "))
nbonhomme = int(input("nombre de personne que vous voulez faire marcher : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
nbonhommeenvie = nbonhomme


# création de matrices de zeros pour les coordonnees des bonhommes
stock =np.zeros((nbonhomme,N+1))
stockr =np.zeros((nbonhomme,N+1))
stocka =np.zeros((nbonhomme,N+1))
#creation de matrice zeros pour la variance
X=np.zeros((N+1,nbonhomme))
Xa=np.zeros((N+1,nbonhomme))
Xr=np.zeros((N+1,nbonhomme))


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


def reflectabsorb(N,xn,xmaxlife):
    #on definit p pour qu'il y ait une chance sur deux
    p=np.random.random()
    if 0.5 < p :
        xn=reflect(xn, murdroite, murgauche)
    if 0.5 > p :
        xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
    return(xn,xmaxlife)



bonvivant=np.zeros(N+1)
#Nombre de personnes en vie en fonction du temps
numbon=0
listpersonneviepas=[0]*N
listpersonneviepasa=[0]*N

for i in range(nbonhomme) :
	#il faut remettre à 0 la liste à chaque fois pour que chaque bonhomme
    #commence à 0 pareil pour xmaxlife si le bonhomme est déjà mort
    x = [0]
    xmaxlife=1
    xmaxlifea=1
    listreflect=[0]
    listabsorb=[0]
	#p sert a ce qu'il y ait une chance sur 3 pour qu'un bonhomme prenne
    #un chemin ou un autre une fois qu'il choisit un mode il reste dedans
    p=np.random.choice([1,2,3])
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx
        #si on ne fait pas xmaxlife différent de 0 alors la personne risque
        #de continuer à bouger alors qu'elle est censée être absorbée
        if xmaxlife!=0:
            #ajoute à chaque fois que quelqu'un arrive au pas z en vie 1 au
            #nombre de survivants à ce pas
            listpersonneviepas[z]+=1
            xn,xmaxlife=reflectabsorb(N,xn,xmaxlife)
        #si jamais le bonhomme est déjà mort alors il faut qu'il reste sur le
        #mur donc qu'il continue d'emprunter le chemin d'absorption
        else:
            xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        x.append(xn)

        if xmaxlifea!=0:
            listpersonneviepasa[z]+=1
        dx=np.random.normal()
        xn = listabsorb[-1]+ dx
        xn,xmaxlifea=absorbing(xn, murdroite, murgauche,xmaxlifea)
        listabsorb.append(xn)

        dx=np.random.normal()
        xn = listreflect[-1]+ dx
        xn=reflect(xn,murdroite,murgauche)
        listreflect.append(xn)
        #ajout à la liste x comprenant les coordonnées des pas du bonhomme z


    #ajout de la liste des pas finis du bonhomme z dans la matrice
    stock[i,:] = x
    stocka[i,:]=listabsorb
    stockr[i,:]=listreflect
    for bidule in range(0,len(x)):
        X[bidule][numbon]=(x[bidule])
        Xa[bidule][numbon]=(listabsorb[bidule])
        Xr[bidule][numbon]=(listreflect[bidule])
    numbon+=1





#densité pour le chemin partial absorbing
plt.figure(5)
for i in range(nbonhomme) :
    plt.plot(stock[i], 'o')
plt.title("la densité des marcheurs en fonction du nombre de pas")
plt.xlabel('Number of steps')
plt.ylabel('Position')



#moyenne
az=0
nvie=0
for i in range(1,len(listpersonneviepasa)):
    az+=i*listpersonneviepasa[i]
    nvie+=listpersonneviepasa[i]

meanlifetime=az/nvie
print("la moyenne du nombre de pas parcourue avant de mourrir est",meanlifetime)

plt.figure(1)
plt.subplot(211)

for numerobonhomme in range(nbonhomme) :
    x=stock[numerobonhomme]
    x
    #création d'une liste vide où on va rentrer les pas qu'il a fait en étant vivant

    for pas in range(len(x)):

        if numerobonhomme%2==0:
            plt.plot(x[pas],numerobonhomme,'ob')
        else:
            plt.plot(x[pas],numerobonhomme,'or')
        plt.title("déplacement du bonhomme")

#What is the average position of the walkers as a function of time
#plt.subplot permet de séparer la fenêtre où on affiche les graphes en
#plusieurs parties. En l'occurence elle sépare en 2 parties.
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

#légende
plt.xlabel('nombre de pas')
plt.ylabel('Average position of the walkers')
plt.title("Average position of the walkers as a function of time")
#on affiche le graphe
plt.show

#For the absorbing reflection case
#la figure 4 est l'affichage du nombre de survivants en fonction du nombre de pas
plt.figure(4)
plt.plot(listpersonneviepas,'^k:')
plt.xlabel("Nombre de pas")
plt.ylabel("Nombre de personnes en vie")
plt.show()

#What is the standard deviation of the position the walkers as a function of time
#calcul de variance
variancepas=[]
variancepasa=[]
variancepasr=[]

for pas in range(N+1):
    variancepas.append(np.std(X[pas]))
    variancepasa.append(np.std(Xa[pas]))
    variancepasr.append(np.std(Xr[pas]))

plt.figure(2)
plt.plot(variancepas,"r--", label = "chemin reflect absorb")
plt.plot(variancepasa,"b--", label = "chemin absorb")
plt.plot(variancepasr,"g--", label = "chemin reflect")
plt.xlabel('nombre de pas/temps')
plt.ylabel('Standard deviation of the walkers/variance')
plt.title("Standard deviation of the walkers as a function of time/number of steps")


plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273

