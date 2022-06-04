global lista
lista=list()
class Alumno:
    cedula = ""
    nombre = ""
    edad = 0

def registrarAlumno(): 
    print("Registro de alumnos")
    a = Alumno()
    a.cedula =input ("Ingrese cedula: ")
    a.nombre = input ("Ingrese nombre: ")
    a.edad = input("ingrese edad: ")
    lista.append(a)

def listaAlumno(): 
    print("Lista de alumnos")
    for a in lista:
        print( "Cedula:", a.cedula , "-","Nombre:", a.nombre, "-","Edad:", a.edad)
    
def buscarAlumno(): 
    print("Busqueda de alumnos") 
    filtro= input("Ingrese la cedula o nombre a buscar: ")  
    for a in lista:
        if a.cedula == filtro or a.nombre==filtro:
            print(a.cedula, "-", a.nombre, "-",a.edad)
menu = """
Menu
1-Registrar alumno
2-Lista de alumnos
3-Buscar alumno
4-Salir
"""
pop= True
while pop == True:
    print(menu)
    op = int((input("toma una opcion:")))
    if op is 1:
       registrarAlumno()
    elif op is 2:
        listaAlumno()
    elif op is 3:
        buscarAlumno()
    elif op is 4:
       print("Gracias por usar la app") 
       pop= False 
    else:
        print("tecla error")  
                  









