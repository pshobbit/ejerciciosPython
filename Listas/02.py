"""

Ejercicio 02
Escribe un programa que lea del fichero de buzón de correo mbox-short.txt (http://www.pythonlearn.com/code/mbox-short.txt)
y cada vez que se encuentre una línea que empiece por "From" separarla en palabras. Interesa quién envió el mensaje
(segunda palabra de la línea "From") sin la parte del dominio. Es decir, de:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 mostraremos solo "stephen.marquard".
El programa debe mostrar la lista de los usuarios ordenada alfabéticamente, sin repetir ninguno y finalizar visualizando
el total de líneas encontradas.

"""

try:
    fhandle = open("mbox-short.txt")
except IOError:
    print("El fichero no existe.")
    exit()

users = list()

cont = 0

for line in fhandle:
    if line.startswith("From "):
        cont += 1
        candidate = line.split()[1].split('@')[0]
        if candidate not in users:
            users.append(candidate)
users.sort()

for user in users:
    print(user)

print('Número de líneas encontradas: ', cont)
print('Número de usuarios encontrados: ', len(users))