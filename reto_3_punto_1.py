from math import atan2
from math import degrees

class Point:
    """Se define un punto del espacio"""

    def __init__(self,x,y):
        # se establecen coordenadas x,y para el punto
        self.x = x
        self.y = y
class Line:
    """Linea con un punto de inicio y uno de final"""

    def __init__(self,start: Point,end: Point):
        # se inicializa un inicio y un final aclarando que estos pertenecen a la clase Point
        self.start = start
        self.end = end

    def compute_lenght(self):
        # hace una diferencia en el eje x y el eje y para asi calcular la longitud mediante pitagoras (a^2 + b^2 = h^2)
        horizontal_lenght = self.end.x-self.start.x
        vertical_lenght = self.end.y - self.start.y
        lenght = (vertical_lenght**2 + horizontal_lenght**2)**(1/2)
        return lenght
    
    def compute_slope(self):
        # usando atan2 calcula en radianes el angulo formado por los componentes x y y del triangulo que forma la recta, para luego transformarlo a grados
        return degrees(atan2(abs(self.end.y - self.start.y), abs(self.end.x-self.start.x)))
    
    def compute_horizontal_cross(self):
        # verifica que la linea corte el eje x multiplicando su inicio y fin en y, si es negativo, pasa por el eje (Teorema de bolzano)
        if self.start.y * self.end.y <= 0:
            print("La recta corta al eje x")

    def compute_vertical_cross(self):
        # verifica que la linea corte el eje y multiplicando su inicio x fin en x, si es negativo, pasa por el eje (Teorema de bolzano)
        if self.start.x * self.end.x <= 0:
            print("La recta corta al eje y")

    def discretize_line(self, n):
        # toma un numero de puntos para discretizar la linea, y define el avance que se hara en cada eje segun la diferencia en los ejes, para luego crear una lista con cada uno de los puntos, iterando hasta que una variable i llegue al valor del n ingresado para la cantidad de puntos
        array_points = []
        x_advance = (self.end.x - self.start.x)/n
        y_advance = (self.end.y - self.start.y)/n
        i = 0
        while i <= n:
            array_points.append((self.start.x, self.start.y))
            self.start.x = self.start.x + x_advance
            self.start.y = self.start.y + y_advance     
            i += 1
        return array_points

class Rectangle:
    """Reinvencion de la clase Rectangle, haciendo uso de composicion de lineas"""
    def __init__(self, height1: Line, height2: Line, width1: Line, width2: Line):
            # se define cada una de las lineas como objetos de la clase Line
            self.height1 = height1
            self.height2 = height2
            self.width1 = width1
            self.width2 = width2

    def compute_area(self):
        # toma coordenadas de los puntos de las lineas para determinar altura y anchura del rectangulo para asi calcular el area
        return ((self.height1.end.y-self.height1.start.y) * (self.width1.end.x - self.width1.start.x))
    
    def compute_perimeter(self):
        # toma coordenadas de los puntos de las lineas para determinar altura y anchura del rectangulo para asi calcular el perimetro
        return 2 * ((self.height1.end.y-self.height1.start.y) + (self.width1.end.x - self.width1.start.x))

if __name__ == "__main__":
    # definicion de una linea ejemplo
    linea_ejemplo = Line(
        start = Point(0,3),
        end = Point(5,2)
    )

    # definicion de un rectangulo ejemplo
    rectangulo_ejemplo = Rectangle(
        height1= Line(
            start = Point(0,0),
            end = Point(0,3)
        ),
        height2= Line(
            start = Point(5,0),
            end = Point(5,3)
        ),
        width1 = Line(
            start = Point(0,0),
            end = Point(5,0)
        ),
        width2= Line(
            start = Point(0,3),
            end = Point(5,3)
        )
    )
    
    # impresion de los calculos del rectangulo (area y perimetro)
    print(f"El area del rectangulo es: {rectangulo_ejemplo.compute_area()}")
    print(f"EL perimetro del rectangulo es: {rectangulo_ejemplo.compute_perimeter()}")
    print("\n")

    # impresion de los calculos de la linea (longitud, grados de inclinacion, corte con los ejes y discretizacion)
    print(f"La longitud de la recta es: {linea_ejemplo.compute_lenght()}")
    print(f"La pendiente de la recta calculada en grados es: {linea_ejemplo.compute_slope()}°")
    linea_ejemplo.compute_horizontal_cross()
    linea_ejemplo.compute_vertical_cross()
    print("\n")
    arreglo = linea_ejemplo.discretize_line(5)
    for i in range(0,len(arreglo)):
        print(f"p{i}= {arreglo[i]}")