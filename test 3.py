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
X=[]
listpersonneviepas=[0]*N
for i in range(nbonhomme) :
    #il faut remettre a 0 la liste a chaque fois pour que chaque bonhomme commence a 0 pareil pour xmaxlife si le bonhomme est direct mort c'est un peu couillon quand meme
    x = [0]
    xmaxlife=1
    #p sert a ce qu'il y ait une chance sur 3 pour qu'un bonhomme prenne un chemin ou un autre une fois qu'il choisit une mode il reste dedans
    p=np.random.choice([1,2,3])
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx

        if xmaxlife!=0:
            listpersonneviepas[z]+=1
            print(listpersonneviepas)

        if p==1 :
            #si on ne fait pas xmaxlife different de 0 alors la personne risque de continuer a bouger alors qu'elle est censee etre absorbee
            if xmaxlife!=0:
                xn,xmaxlife=reflectabsord(N,xn,xmaxlife)
            else:
                xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        if p==2:
            xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        if p==3:
            xn=reflect(xn,murdroite,murgauche)
        #ajout a la liste x comprenant les coordonees des pas du bonhomme z
        x.append(xn)
    
    #ajout de la liste des pas finies du bonhomme z dans la matrice
    stock[i,:] = x
    for numpas in range(len(x)):
            X[numpas].append(x[numpas])
variancepas=[]
for g in range(len(x))
    variancepas[g]=np.std(X[g])
plt.plot(variancepas)
      
print(listpersonneviepas)
plt.subplot(211)

dureedevietot=0
for numerobonhomme in range(nbonhomme) :
    x=stock[numerobonhomme]
    #creation d'une liste vide ou on va rentrer les pas qu'il a fait en etant vivant
    bonvivant=[]
    for pas in range(len(x)):
        if x[pas]!=murdroite and x[pas]!=murgauche:
            bonvivant.append(x[pas])

        if numerobonhomme%2==0:
            plt.plot(x[pas],numerobonhomme,'ob')
        else:
            plt.plot(x[pas],numerobonhomme,'or')
        plt.title("déplacement du bonhomme")






moydureedevie=(dureedevietot/N)
print(moydureedevie)


plt.show

#question 1

plt.subplot(212)

b=stock.mean(axis=0)
plt.plot(b,'ob')

#vision en fonction des pas

plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273
