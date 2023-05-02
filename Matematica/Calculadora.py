import Figuras

while(True):
      print("""Menú
1.Circulo 
2.Trapecio 
3.Triangulo 
4.Elipse
5.SALIR""")

      op=int(input("Ingrese una opción: "))

      if (op==1):
            op1=int(input("""1. Medir area
2. Medir perimetro 
"""))
            if (op1==1):
                  bolita=Figuras.Circulo()
                  bolita.radio=float(input("Ingrese el radio del circulo: "))
                  bolita.CalcularArea()
                  print("El area del circulo es: ",bolita.area)

            elif(op1==2):
                  bolita=Figuras.Circulo()
                  bolita.radio=float(input("Ingrese el radio del circulo: "))
                  bolita.CalcularPerimetro()
                  print("El perimetro del circulo es: ",bolita.perimetro)

      elif(op==2):
            op1=int(input("""1. Medir area
2. Medir perimetro
"""))
            if (op1==1):
                  tra=Figuras.Trapecio()
                  tra.base1=int(input("Ingrese la medida de la primer base: "))
                  tra.base2=int(input("Ingrese la medida de la segunda base: "))
                  tra.altura=int(input("Ingrese la altura del trapecio: "))
                  tra.CalcularArea()
                  print("El area del trapecio es: ",tra.area)

            elif(op1==2):
                  tra=Figuras.Trapecio()
                  tra.lado1=int(input("Ingrese el tamaño del primer lado: "))
                  tra.lado2=int(input("Ingrese el tamaño del segundo lado: "))
                  tra.lado3=int(input("Ingrese el tamaño del tercer lado: "))
                  tra.lado4=int(input("Ingrese el tamaño del cuarto lado: "))
                  tra.CalcularPerimetro()
                  print("El perimetro del Trapecio es: ",tra.perimetro)

#hasta aca asigne los atributos falta todo lo de abajo

      elif(op==3):
            op1=int(input("""1.Medir area
2.Medir perimetro
"""))
            if (op1==1):
                  tri=Figuras.Triangulo()
                  tri.base=float(input("Ingrese la base del triangulo: "))
                  tri.altura=float(input("Ingrese la altura del triangulo: "))
                  tri.CalcularArea()
                  print("El area del triangulo es: ",tri.area)

            elif(op1==2):
                  tri=Figuras.Triangulo()
                  tri.lado1=float(input("Ingrese el lado 1 del triangulo: "))
                  tri.lado2=float(input("Ingrese el lado 2 del triangulo: "))
                  tri.lado3=float(input("Ingrese el lado 3 del triangulo: "))
                  tri.CalcularPerimetro()
                  print("El perimetro es: ",tri.perimetro)

      elif(op==4):
            op1=int(input("""1.Medir area
2.Medir perimetro
"""))
            if (op1==1):
                  elip=Figuras.Elipse()
                  elip.semiEjeHorizontal=float(input("Ingrese el tamaño del semieje Horizontal: "))
                  elip.semiEjeVertical=float(input("Ingrese el tamaño del semieje vertical: "))
                  elip.CalcularArea()
                  print("El area del elipse es: ",elip.area)
            elif (op1==2):
                  elip=Figuras.Elipse()
                  elip.semiEjeHorizontal=float(input("Ingrese el tamaño del semieje Horizontal: "))
                  elip.semiEjeVertical=float(input("Ingrese el tamaño del semieje vertical: "))
                  elip.CalcularPerimetro()
                  print("El perimetro del elipse es: ",elip.perimetro)


      elif(op==5):
            break

