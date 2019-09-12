#  C:\Users\Marilina\Desktop\manejable.txt
#  C:\Users\Marilina\Desktop\prueba\manejable.txt

#El programa mueve un archivo de un directorio a otro.

def mv():
    nameFile = input('Indica el archivo que deseas mover: ')
    try:
        archivo= open(nameFile)
    except FileNotFoundError:
        print('El archivo no existe')
        return
    import paste

    destinyname= input('Ingresa el directorio destino + el nombre del archivo + la extensión: ')
    paste.pasteex(destinyname, archivo)
    from os import remove
    remove (nameFile)

mv()


