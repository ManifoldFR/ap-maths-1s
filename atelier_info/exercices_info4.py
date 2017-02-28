from numpy import linspace
import matplotlib.pyplot as plt

class Vecteur:
    def __init__(self,*args):
        self.dim = len(args)
        self.coord = tuple(args)

    def __add__(self,other):
        # couples (x,y) où x est une coordonnée de 
        # self et y la coordonnée correspondante de other
        coords = zip(self.coord,other.coord)
        # arguments à passer au constructeur,
        # somme des coordonnées des vecteurs
        args = (x+y for x,y in coords)
        return Vecteur(*args)

    def mult(self,k):
        # arguments à passer au constructeur
        args = (k*x for x in self.coord)
        return Vecteur(args)

    def __repr__(self):
        return "Vecteur"+str(self.coord)

class Polynome(Vecteur):
    def func(self,x):
        coeffs = self.coord
        n = self.dim
        return sum(coeffs[i]*x**i for i in range(n))
        
    def graphe(self,a,b):
        Xar = linspace(a,b,100)
        valeurs = self.func(Xar)
        fig = plt.figure(0)
        plt.grid(True)
        plt.plot(Xar, valeurs)
        plt.show()
        return fig