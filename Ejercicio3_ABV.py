class Figura ():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        pass

    def Print_Area(self):
        pass

class Rectangulo (Figura):
    def __init__(self, base, altura):
        super().__init__(base,altura)

    def area(self):
        return self.base * self.altura

    def Print_Area(self):
        print(f"El area del rectagulo es: {self.area()}")

class Triangulo (Figura):
    def __init__(self,base,altura):
        super().__init__(base, altura)

    def area(self):
        return (self.base * self.altura) / 2

    def Print_Area(self):
        print(f'El area del triangulo es: {self.area()}')

class Estudiante():

    def __init__(self,nombres, correos, contraseña):
        self.nombres = nombres
        self.correos = correos
        self.contraseña =contraseña

    #Definiendo Metodos

    def setNombre(self):
        return self.nombres
    def setCorreo(self):
        return self.correos
    def setContraseña(self):
        return self.contraseña
    def Imprimir_Datos(self):
        print("\nNombre: " + self.setNombre() + "\nCorreo: " + self.setCorreo() + "\nContraseña: " + self.setContraseña())

if __name__ == '__main__':

    rec = Rectangulo(10,3)
    rec.Print_Area()

    trin = Triangulo(6,3)
    trin.Print_Area()

    nom = input("Ingrese su nombre: ")
    corr = input("Ingrese su correo: ")
    passw = input("Ingrese su contraseña: ")

    e = Estudiante(nom,corr,passw)
    e.Imprimir_Datos()




