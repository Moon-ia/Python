import Calculadora

class Figuras:
    pass

class Circulo(Figuras):
    def __init__(self):
        Calculadora.__init__(self) #tomo los valores de cal
        self.radio=0
        self.perimetro=0
    def CalcularArea(self):
        self.area=3.1415*self.radio*self.radio #area= pi por radio al cuadrado
    def CalcularPerimetro(self):
        self.perimetro=2*3.1415*self.radio #perimetro 2* pi* radio

class Trapecio(Figuras):
    def __init__(self):
        Calculadora.__init__(self)
        self.base1=0
        self.base2=0
        self.altura=0
        self.lado1=0
        self.lado2=0
        self.lado3=0
        self.lado4=0
    def CalcularArea(self):
        self.area=(self.base1+self.base2)*self.altura/2 #area= la suma de las bases * la altura /2
    def CalcularPerimetro(self):
        self.perimetro=self.lado1+self.lado2+self.lado3+self.lado4 #perimetro= suma de todos los lados

class Triangulo(Calculadora):
    def __init__(self):
        Calculadora.__init__(self)
        self.base=0
        self.altura=0
        self.lado1=0
        self.lado2=0
        self.lado3=0
    def CalcularArea(self):
        self.area=(self.base*self.altura)/2 #area= base* altura /2
    def CalcularPerimetro(self):
        self.perimetro=self.lado1+self.lado2+self.lado3

class Elipse(Calculadora):
    def __init__(self):
        Calculadora.__init__(self)
        self.semiEjeHorizontal=0
        self.semiEjeVertical=0
    def CalcularArea(self):
        self.area=3.1415*self.semiEjeHorizontal*self.semiEjeVertical#area= pi * semejHor *semejVer
    def CalcularPerimetro(self):
        self.perimetro=3.1415*(self.semiEjeHorizontal+self.semiEjeVertical)#perim= pi * (seEjHor+ seEjVer)