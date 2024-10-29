import numpy as np

def positionX():
    lettre_X = np.array([[0,1,0],[1,1,1],[0,1,0]])
    return(lettre_X)

def positionY():
    lettre_Y = np.array([[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,1,1,1]])
    return(lettre_Y)

def positionZ():
    lettre_Z = np.array([[1,1,0],[1,1,1],[0,1,1]])
    return(lettre_Z)

def positionP():
    lettre_P = np.array([[1,1,0],[1,1,0],[1,0,0]])
    return(lettre_P)

def positionT():
    lettre_T = np.array([[1,1,1],[0,1,0],[0,1,0]])
    return(lettre_T)

def reduction(Mat):
    L=[]
    K=len(Mat)
    for i in range(K):
        if sum(Mat[i]) == 0 :
            L.append(i)
    Mat=np.delete(Mat,L,0)
    L=[]
    Mat=np.transpose(Mat)
    for i in range(K):
        if sum(Mat[i]) == 0 :
            L.append(i)
    Mat=np.delete(Mat,L,0)
    return(np.transpose(Mat))
    





    






























