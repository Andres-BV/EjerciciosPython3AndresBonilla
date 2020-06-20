'''#Buena tarde, maestro. En el ejercicio de los numeros telefonicos no he podido encontrar la manera
    de como incluir y validar los espacios y el guion. Sigo buscando la solución.'''

#Validando Direccion de Correo

import re

correo = 'j.pedro@padts.mx'

if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):

    print(f"El correo {correo} ES valido")
else:
    print(f"El correo {correo} NO es valido")

#VALIDANDO NUMEROS TELEFONICOS

# 3312345678, (33)12345678, (331)1235678, (33) 1234 5678, (331) 123-5678

num ='(331)1235678'

if re.match('[0-9]{10}|\([0-9]{2,3}\)[0-9]{7,8}$',num):         #[0-9] {3,4}    [0-9]{4}

    print(f'El numero {num} ES valido')
else:
    print(f'El numero {num} NO es valido')


# VALIDANDO EL RFC

RFC = 'VAGJ851104MJ8'

if re.match('[a-zA-Z]{4}[0-9]{6}[a-zA-Z0-9]{3}$',RFC):
    print(f'El RFC {RFC.upper()} ES correcto')

else:
    print(f'El RFC {RFC.upper()} NO es valido')


# VALIDANDO CURP

CURP = 'VAGJ851104hsrldn04'   #HSRLDN04

if re.match('[a-zA-Z]{4}[0-9]{6}[h-mH-M]{1}[a-zA-Z]{5}[a-zA-Z0-9]{2}$',CURP):
    print(f'El CURP {CURP.upper()} Es correcto')

else:
    print(f'El CURP {CURP.upper()} NO es valido')

input("Press ENTER to exit")






