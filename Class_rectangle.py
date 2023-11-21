class Rectangle() :
    def __init__(self) :
        self.largeur=4.2
        self.longueur=6.2
    def perimetre(self) :
        return 2*(self.largeur+self.longueur)
    def Aire(self) :
        return self.longueur*self.largeur
    def IsCarre(self) :
        if self.longueur==self.largeur :
            return True
        else :
            return False
    def AfficherRectangle(self):
            print("the length is: ",self.longueur)
            print("the width is: ",self.largeur)
            print("The perimeter is:",self.perimetre())
            print("The area is:",self.Aire())
            if self.IsCarre()==True :
                print("It is a square.")
            else:
                print("It's not a square.")
    

