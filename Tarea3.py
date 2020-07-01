from Ejercicios.Estudiante import Estudiante
from StudentIO import EstudiantePickle as Pickle
from StudentIO import EstudianteShelve as Shelve

if __name__ == '__main__':

    e=Estudiante("Andres","andresvz2912@gmail.com","123456789")
    e1=Estudiante("Omar","Omar_69@gmail.com","2441307192")
    e2=Estudiante("Juan","Juan_87@gmail.com","123456789")
    e3=Estudiante("Karla",'Karla_@gmail.com','123456789')
    e4=Estudiante("Maria",'Maria_@gmail.com','123456789')

    e5=Estudiante('Pedro','Pedro@gmail.com','965111515')



Shelve.Leershelve(e2)
Pickle.GuadarPickle(e4)
Shelve.GuardarShelve(e3)


