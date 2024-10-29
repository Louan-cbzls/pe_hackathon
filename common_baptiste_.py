n = 6
m = 10

Lettres_Base = [lettre_f,lettre_i,lettre_l,lettre_n,lettre_p,lettre_t,lettre_u,lettre_v,lettre_w,lettre_x,lettre_y,lettre_z]

def grille(n,m):
    tab = np.zeros((n,m))
    return(tab)


def rotation(tab):
    return(numpy.rot90(tab))

def symetrie(tab):
    return(numpy.fliplr(tab))