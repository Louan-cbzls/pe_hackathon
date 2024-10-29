
### code alexis F I L N

import numpy as np

lettre_f=np.zeros((3,3))
lettre_f[0,1]=1
lettre_f[0,2]=1
lettre_f[1,0]=1
lettre_f[1,1]=1
lettre_f[2,1]=1
print(lettre_f)

lettre_i=np.zeros((5,5))
lettre_i[0,0]=1
lettre_i[1,0]=1
lettre_i[2,0]=1
lettre_i[3,0]=1
lettre_i[4,0]=1
print(lettre_i)

lettre_l=np.zeros((4,4))
lettre_l[0,0]=1
lettre_l[1,0]=1
lettre_l[2,0]=1
lettre_l[3,0]=1
lettre_l[3,1]=1
print(lettre_l)

lettre_n=np.zeros((4,4))
lettre_n[0,1]=1
lettre_n[1,1]=1
lettre_n[2,1]=1
lettre_n[2,0]=1
lettre_n[3,0]=1
print(lettre_n)

def placement(grille,matrice):
    n,p=np.shape(grille)
    s,t=np.shape(matrice)
    m=(n-s)*(p-t)
    liste=[]
    for i in range(n-s+1):
        for j in range(p-t+1):
            nom=np.zeros((n,p))
            nom[i:i+s,j:j+t]=matrice
            liste.append(nom)
    return liste

