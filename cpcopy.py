#  C:\Users\Marilina\Desktop\manejable.txt
#  C:\Users\Marilina\Desktop\prueba\manejable.txt
#  El programa copia un archivo y o pega en otro directorio,
#  Copia el archivo y lo pega

def copypaste():
    filename= input('Elige el nombre del archivo a copiar: ')
    try:
        archivo = open (filename)
    except FileNotFoundError:
        print('No existe el archivo')
        return
    filename2= input('Elige donde quieres copiar el archivo (ruta + nombre): ') 
    paste.pasteex(filename2, archivo)
  
import paste

    
copypaste()
