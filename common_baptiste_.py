import numpy as np

n = 6
m = 10

lettre_u = np.array([[0,0,0],[1,0,1],[1,1,1]])
lettre_v = np.array([[0,0,1],[0,0,1], [1,1,1])
lettre_w = np.array([[0,0,1],[0,1,1],[1,1,0]])
lettre_i=np.zeros((5,5))
lettre_i[0,0]=1
lettre_i[1,0]=1
lettre_i[2,0]=1
lettre_i[3,0]=1
lettre_i[4,0]=1
lettre_l=np.zeros((4,4))
lettre_l[0,0]=1
lettre_l[1,0]=1
lettre_l[2,0]=1
lettre_l[3,0]=1
lettre_l[3,1]=1

lettre_n=np.zeros((4,4))
lettre_n[0,1]=1
lettre_n[1,1]=1
lettre_n[2,1]=1
lettre_n[2,0]=1
lettre_n[3,0]=1

lettre_f=np.zeros((3,3))
lettre_f[0,1]=1
lettre_f[0,2]=1
lettre_f[1,0]=1
lettre_f[1,1]=1
lettre_f[2,1]=1

lettre_t = np.array([[1,1,1],[0,1,0],[0,1,0]])
lettre_x = np.array([[0,1,0],[1,1,1],[0,1,0]])
lettre_y = np.array([[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,1,1,1]])
lettre_z = np.array([[1,1,0],[1,1,1],[0,1,1]])
lettre_p = np.array([[1,1,0],[1,1,0],[1,0,0]])








dict = {'f' : lettre_f, 'i' :lettre_i, 'l' : lettre_l, 'n': lettre_n, 'p': lettre_p, 't': lettre_t, 'u' : lettre_u,'v':lettre_v, 'w': lettre_w, 'x' : lettre_x, 'z' : lettre_z}

Lettres_Base = [lettre_f,lettre_i,lettre_l,lettre_n,lettre_p,lettre_t,lettre_u,lettre_v,lettre_w,lettre_x,lettre_y,lettre_z]

def grille(n,m):
    tab = np.zeros((n,m))
    return(tab)


def rotation(tab):
    return(numpy.rot90(tab,1,(0,1)))

def symetrie(tab):
    return(numpy.fliplr(tab))

def ensemble_rotation_symetrie(lettre):
    tab=[lettre]
    for i in range(1,4):
        tab.append(rotation(tab[-1]))
    for j in range(0,4):
        tab.append(symetrie(tab[i]))
    return(tab)

def Lettres_tot(tab):
    Lettres_tot =[]
    for key in dict.keys :
        Lettres_tot.append(ensemble_rotation_symetrie(dict['key']))
    return(Lettres_tot)