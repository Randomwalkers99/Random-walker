murgauche = -5
xmaxlife = 1
p=(len(x)//2*N)

#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas



def reflect(xn,murdroite,murgauche):
    if xn > murdroite :
        xn=murdroite - abs(murdroite - xn)
@ -30,28 +33,25 @@ def reflect(xn,murdroite,murgauche):
    return(xn)


def absorbing(xn, murdroite, murgauche):
    xmaxlife=1
    i=0
    while xmaxlife != 0 :
        if xn>murdroite :
            xn=murdroite
            xmaxlife == 0
            print("xmaxlife = 0")
        if xn<murgauche :
            xn=murgauche
            xmaxlife == 0
            print("xmaxlife = 0")
        return(xmaxlife)
def absorbing(xn, murdroite, murgauche,xmaxlife):
    if xn>murdroite :
        xn=murdroite
        xmaxlife = 0
        print("xmaxlife = 0")
    if xn<murgauche :
        xn=murgauche
        xmaxlife = 0
        print("xmaxlife = 0")
    return(xn,xmaxlife)

for i in range(N):
    xmaxlife=1
    while xmaxlife !=0 :
        dx=np.random.normal()
        xn = x[-1]+ dx
        print (xn)
        xn=absorbing(xn, murdroite, murgauche)
        x.append(xn)
#for i in range(N):

#    while xmaxlife !=0 :
#        dx=np.random.normal()
#        xn = x[-1]+ dx
#        print (xn)
#        xn=absorbing(xn, murdroite, murgauche)
#        x.append(xn)
print (x)


@ -63,15 +63,15 @@ for i in range(N):
                xn=reflect(xn, murdroite, murgauche)
            print (xn)
            if 0.5 > p :
                xn = absorbing(xn, murdroite, murgauche)

                xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
            x.append(xn)
            print(xmaxlife)
            print (x)
            if xmaxlife==0:
                break

#vision horizontale
plt.subplot(211)
for i in range(N):
for i in range(len(x)):
    plt.plot(x[i],3,'ob')
plt.title("déplacement du bonhomme")

@ -80,7 +80,7 @@ plt.title("déplacement du bonhomme")
plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlabel("nombre de pas effectué")
plt.ylabel("coordonnée du pas")
plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273