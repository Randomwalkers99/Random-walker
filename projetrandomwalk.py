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
#nombre de pas fait par la personne 
N = int(input("number of steps : "))
nbonhomme = int(input("nombre de personne que vous voulez faire marcher : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
l = 0
nbonhommeenvie = nbonhomme
p=(len(x)//2*N)


# creation d'une matrice de zeros qui deviendront bientot des heros (oui je sais c'est nul mais je suis fatiguee ok ?)
stock =np.zeros((nbonhomme,N+1))

stockr =np.zeros((nbonhomme,N+1))
stocka =np.zeros((nbonhomme,N+1))


#np.random.normal prend une valeur dans une fonction normale centree
#valeur probable pour chaque pas
for i in range(N):
    dx=np.random.normal()
    xn = x[-1]+dx
    xn= reflect(xn,murdroite,murgauche)
    x.append(xn)
    #les murs



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


#vision horizontale
plt.subplot(211)
for i in range(N):
    plt.plot(x[i],3,'ob')
plt.title("déplacement du bonhomme")


#vision en fonction des pas
plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()




#Nombre de personnes en vie en fonction du temps

listpersonneviepas=[0]*N
for i in range(nbonhomme) :
	#il faut remettre a 0 la liste a chaque fois pour que chaque bonhomme commence a 0 pareil pour xmaxlife si le bonhomme est déjà mort
    x = [0]
    xmaxlife=1
    listreflect=[0]
    listabsorb=[0]
	#p sert a ce qu'il y ait une chance sur 3 pour qu'un bonhomme prenne un chemin ou un autre une fois qu'il choisit une mode il reste dedans
    p=np.random.choice([1,2,3])
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx
        #si on ne fait pas xmaxlife different de 0 alors la personne risque de continuer a bouger alors qu'elle est censee etre absorbee
        if xmaxlife!=0:
            #ajoute a chaque fois que quelqu'un arrive au pas z en vie 1 au nombre de survivant a ce pas
            listpersonneviepas[z]+=1
            xn,xmaxlife=reflectabsord(N,xn,xmaxlife)
        #si jamais le bonhomme est deja mort alors il faut qu'il reste sur le mur donc qu'il continue d'emprunter le chemin d'absorption
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
        #ajout a la liste x comprenant les coordonees des pas du bonhomme z

    #ajout de la liste des pas finies du bonhomme z dans la matrice
    stock[i,:] = x
    stocka[i,:]=listabsorb
    stockr[i,:]=listreflect


for i in range(nbonhomme) :
    plt.plot(stock[i], 'o')
plt.xlabel('Number of steps')
plt.ylabel('Position')
plt.show()

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


plt.figure(1)
#plt.subplot permet de separer la fenetre ou on affiche les graph en plusieurs parties. en l'occurence elle separ en 2 parties
plt.subplot(212)
#calcul de la moyenne de la position des bonhommes a chaque pas pour chaque chemin
moydureedevie=stock.mean(axis=0)
a=stocka.mean(axis=0)
r=stockr.mean(axis=0)

#on affiche en rouge le chemin absorption ou reflexion, en bleu reflexion, en vert absorption
plt.plot(moydureedevie,"r--")
plt.plot(a,'g--')
plt.plot(r,'b--')

#donne l'abcisse et l'ordonnée du graphique
plt.axis([0,N,murgauche,murdroite])

#legende
plt.xlabel('nombre de pas')
plt.ylabel('average position of the walkers')

#on affiche le graph
plt.show


#la figure 2 est l'affichage du nombre de survivants en fonction du nombre de pas
plt.figure(2)
plt.plot(listpersonneviepas,'^k:')
plt.show()



for i in range(nbonhomme) :
    x = [0]
    xmaxlife=1
    p=np.random.choice([1,2,3])
    wn = [0]

    for z in range(N):

        dx=np.random.normal()
        xn = x[-1]+ dx

        if p==1 :

            if xmaxlife!=0:
                xn,xmaxlife, nbonhommeenvie = reflectabsord(N,xn,xmaxlife, nbonhommeenvie)
                wn.append(1)
                #les pas en abscisses en ordonnée le nombre de survivant
                wn.append(nbonhommeenvie)
            else:
                xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        x.append(xn)

    stock[i,:] = x
    print(wn)




plt.show()


#Impact du nombre de personnes absorbées ou reflechies sur les moyennes et sommes
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


#calcul de variance 
numbon=0
X=np.zeros((N+1,nbonhomme))
listpersonneviepas=[0]*N
for i in range(nbonhomme) :
    #il faut remettre a 0 la liste a chaque fois pour que chaque bonhomme commence a 0 pareil pour xmaxlife si le bonhomme est déjà mort
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
    for bidule in range(0,len(x)):
        X[bidule][numbon]=(x[bidule])
    numbon+=1

variancepas=[]
for pas in range(N+1):
    variancepas.append(np.std(X[pas]))

plt.figure(4)
plt.plot(variancepas)

plt.figure(1)
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
