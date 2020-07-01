class Estudiante():

    __nombre = " "
    __correo = " "

    def __init__(self,nombre, correo, contraseña):
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña =contraseña

    #Definiendo Metodos
    def setNombre(self):
        return self.nombre
    def getNombre(self):
        return self.__nombre
    def setContraseña(self):
        return self.contraseña
    def getContraseña(self):
        return self.__contraseña
    def setCorreo(self):
        return self.correo
    def getCorreo(self):
        return self.__correo

    def Imprimir_Datos(self):
        print("\nNombre: " + self.getNombre() +
              "\nCorreo: " + self.getCorreo() +
              "\nContraseña: " + self.getContraseña())


