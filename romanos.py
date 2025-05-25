

    
valor_romanos  = [
    (1000,'M'),
    (900,'CM'),
    (800,'D'),
    (700,'DCC'),
    (600,'DC'),
    (500,'D'),
    (400,'CD'),
    (300,'CCC'),
    (200,'CC'),
    (100,'C'),
    (50,'L'),
    (10,'X')
]
   
numero = int(input('escriba el numero que desea convertir a simbolos romanos '))

if 1 <= numero <=3999:
    resultado = ''
    for valor, simbolo in valor_romanos :
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    print('numero romano es: ',resultado)
else:
    print('numero fuera del rango ')

print('-------------------------------------------------------')


lista1 = [1,2,3,4,5]
lista2 = ['uno','dos','tres','cuatro','cinco']

com1 = [len(lista1)]
com2 = [len(lista2)]
if com1 == com2 :
    combinar = zip(lista1,lista2)
    print(list(combinar))
else:
    print('no se puede ejecutar por que sus dimensiones no son iguales... :<')

print('-----------------------------------------------------')





class libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def info_libro(self):
        estado ='disponible' if self.disponible else 'prestado '
        print(f"'{self.titulo}' por {self.autor} - {estado}")

    def prestamo(self):
        if self.disponible:
            self.disponible = False
            print(f"el libro '{self.titulo}' ha sido pretado")
        else:
            print(f"el libro '{self.titulo}' no esta disponoble")
            
    def devolver(self):
        self.disponible = True
        print(f"el libro '{self.titulo}' ha sido devuelto")

class usuario:
    def __init__(self,nombre,id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")

    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene prestado el libro '{libro.titulo}'.")

class biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self,libro):
        self.libros.append(libro)
        print(f"libro '{libro.titulo}' agregado en la biblioteca ")

    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f"usuario '{usuario.nombre}' registrado ")

    def registrar_prestamo(self,titulo_libro,id_usuario):
        libro = next((l for l in self.libros if l.titulo == titulo_libro),None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario),None)

        if libro is None:
            print(f'el libro {titulo_libro} no existe en la biblioteca.')
            return
        if usuario is None:
            print(f'el usuario con ID {id_usuario} no registrado.')
            return
        if not libro.disponible:
            print(f'el libro {titulo_libro} no esta disponible')
            return
        
        libro.prestamo()
        usuario.tomar_libro(libro)

    def devolver_libro(self,titulo_libro, id_usuario):
        libro = next((l for l in self.libros if l.titulo == titulo_libro), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario ), None)


        if libro is None:
            print(f'el libro {titulo_libro} no existe en la biblioteca')
            return
        if usuario is None:
            print(f'el usuario con ID{id_usuario} no registrado ')
            return
        if libro.disponible:
            print(f'el libro {titulo_libro} ya se encuentra en la biblioteca')
            return
        if libro not in usuario.libros_prestados:
            print(f'el libro {titulo_libro} no esta prestado a {usuario.nombre}.')
            return
        
        libro.devolver()
        usuario.devolver_libro(libro)

biblio = biblioteca()

nom1 = input('escriba el nombre del primer libro ')
nom2 = input('escriba el nombre del segundo libro ')

nom1_autor = input('escriba el nombe del autor del primer libro ')
nom2_autor = input('escriba el nombe del autor del segundo libro ')
libro1=libro(nom1, nom1_autor)
libro2=libro(nom2, nom2_autor)
usu1 = input('escriba el nombre del primer usuario ')
usu2 = input('escriba el nombre del segundo usuario ')





biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)


usuario1 = usuario(usu1, 1)
usuario2 = usuario(usu2, 2)

biblio.registrar_usuario(usuario1)
biblio.registrar_usuario(usuario2)

biblio.registrar_prestamo(nom1, 1)
biblio.registrar_prestamo(nom1, 2)

biblio.devolver_libro(nom1, 1)

biblio.registrar_prestamo(nom1, 2)