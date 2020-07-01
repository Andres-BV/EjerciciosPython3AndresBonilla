from Ejercicios import Estudiante
import pickle
import shelve

class EstudiantePickle:

    def GuadarPickle(lista_Estudiante):
        file = open('Estudiante.db','wb')
        pickle.Pickler(file).dump(lista_Estudiante)
        file.close()

    def LeerPickle(self):
        file = open('Estudiante.db','rb')
        lista_Estudiante = pickle.Unpickler(file)
        list =lista_Estudiante.load()
        file.close()

    # def ActualizarPickle(nombre,nnombre = None, ncorreo = None, ncontraseña = None):
    #     lista =
    #     Buscar = False

        for i, estudiante in enumerate(lista):
            if estudiante.getNombre() == nombre:
                Buscar = True
                if nnombre:
                    estudiante.setNombre(nnombre)
                if ncorreo:
                    estudiante.setCorreo(ncorreo)
                if ncontraseña:
                    Estudiante.setContraseña(ncontraseña)
                break

                if Buscar:
                    GuardarPickle(lista)
                else:
                    print("Estudiante no encontrado")

class EstudianteShelve:

    def GuardarShelve(lista_Estudiante):
            with shelve.open('Estudiante_shelve.db') as db:
                db["lista"] = lista_Estudiante

    def Leershelve(lista_Estudiante):
            with shelve.open("students_shelve") as db:
                keys = list(db.keys())
                db_list = []
                for i in range(len(keys)):
                    db_list.append(db[keys[i]])
                return db_list











