class Complex:
    def __init__(self, Re=0, Im=0): #inicializator klassa
        self.Re = Re
        self.Im = Im


    def __add__(self, other): #matem oper: slozhenie
        return Complex(self.Re + other.Re, self.Im + other.Im)


    def __sub__(self, other): #vychitanie
        return Complex(self.Re - other.Re, self.Im - other.Im)


    def __mul__(self, other): #umnozhenie
        return Complex(self.Re*other.Re - self.Im*other.Im, self.Re*other.Im + self.Im*other.Re)


    def __truediv__(self, other): #delenie
        return Complex((self.Re*other.Re-self.Im*other.Im)/(other.Re*other.Re + other.Im*other.Im), (other.Re*self.Im - self.Re*other.Im)/(self.Im*self.Im + other.Im*other.Im))


    def __abs__(self): #znach po modulu
        return (self.Re**2 + self.Im**2)**(1/2)


    def __str__(self):
        return "(" + str(self.Re) +"," + str(self.Im) + ")"


#primery vychisleniy
x = Complex(1, -2)
y = Complex(3, 4)
print((x+y).__str__())
print(x-y)
print(x*y)
print(x/y)
print(abs(x), abs(y))