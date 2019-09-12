#tail: imprime el número indicado de lineas o de bytes, empezando desde el final del archivo

#  C:\Users\Marilina\Desktop\manejable.txt
def tail():
    Namefile= input('Por favor ingrese el nombre del archivo: ')

    while True:
        modo= input ('indique si quiere abrir el archivo en modo texto (r) o en modo bytes (rb) \n r/rb: ')
        modo=modo.lower()
        if modo == 'r' or modo == 'rb':
            break
    try:
        archivo = open (Namefile, modo)
    except FileNotFoundError:
        print('No existe el archivo')
        return

    try:
        numero=int(input ('Ingresa la cantidad de lineas o bytes para mostrar: '))
    except ValueError:
        print('No ingresaste un entero')

    contenido= archivo.readlines()
    longitud = len(contenido)
    numero = longitud - numero
    archivo.seek(0)

    if modo == 'r':
        for linea in range(longitud):
            if linea >= numero:
                print(archivo.readline())
            else:
                archivo.readline()
        
    else:
        for linea in range(longitud):
            if linea >= numero:
                print(archivo.readline())
            else:
                archivo.readline()
    archivo.close()

tail()