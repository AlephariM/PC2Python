#1-----------------------------------------------
cadena_num = ''
for numeros in range(1500,2700):
    if (numeros%7==0 and numeros%5==0):
        cadena_num = cadena_num + ' ' + str(numeros)
cadena_num


#2-----------------------------------------------
h = 5
for i in range(h):
    print( '* ' * (i+1))

for i in range(4):
    print('* '*(4 - i) )

  
#3-----------------------------------------------
cad_numeros = []
continuar = True
pares = 0
impares = 0

while continuar:

    numero = int(input("Ingrese un número (o ingrese cualquier letra para terminar): "))
    cad_numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    opcion_i = input("Desea ingresar otro numero?")

    if (opcion_i == 'si'):
        continuar = True
    else:
        break


print("Numeros ingresados: ", cad_numeros )
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)


#4-----------------------------------------------
# Inicializar una lista vacía para almacenar los datos de los alumnos
lista_alumnos = []

# Pedir al usuario la cantidad de alumnos
cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Ingresar los datos de cada alumno
for _ in range(cant_alumnos):
    nombre_a = input("Nombre del alumno: ")
    
    n1 =  float( input(f"Ingrese la nota 1 del alumno {nombre_a}: ") )
    n2 =  float( input(f"Ingrese la nota 2 del alumno {nombre_a}: ") )
    n3 =  float( input(f"Ingrese la nota 3 del alumno {nombre_a}: ") ) 

    notas = [ n1, n2, n3]
    
    # Crear un diccionario con los datos del alumno y agregarlo a la lista
    datos_alumno = {"Alumno": nombre_a, "Notas": notas}
    lista_alumnos.append(datos_alumno)

# Mostrar el listado completo de alumnos y sus calificaciones
print("\nListado completo de alumnos:")
for info in lista_alumnos:
    print(f"Alumno: {info['Alumno']}, Notas: {info['Notas']}")

  
#5-----------------------------------------------

  def contar_dig_num(num_ent, digito):
    cant_digit = num_ent.count(digito)
    return cant_digit

# solicitar ingresar los valores
num_ent = input('Ingrese el numero entero')
#type(numero)
digito = input('Ingrese el digito que quiere buscar: ')

# empezar ejecucion de la funcion
cant_digit = contar_dig_num(num_ent, digito)
cant_digit

#imprimir
print(f'Número ingresado: {num_ent} y Dígito: {digito}')
print(f'Catidad de veces {digito} en el número: {cant_digit}')


#6-----------------------------------------------
lista_fib = [0, 1]
type(lista_fib)

nmax = 50

while ( lista_fib[-1] + lista_fib[-2] <= nmax ):
    nfib = lista_fib[-1] + lista_fib[-2]
    
    lista_fib.append(nfib)
lista_fib



#7-----------------------------------------------
def num_primo(num):

    # Verificar si el número es divisible por algún otro número menor que él
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    # Si no se encontraron divisores, el número es primo
    return True

# Ejemplo de uso
num = int(input("ingrese número: "))  # Puedes cambiar este valor para probar con diferentes números

if num_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")


  
#8-----------------------------------------------
def factorial(nfact:int):
    if (nfact == 0 or nfact == 1):
        solu = 1
    else:
        solu = 1
        for i in range(nfact):
            solu = (i+1) * solu
    
    return solu

nfact = int(input('Ingrese numero: '))
print(f"El factorial de {nfact} es {factorial(nfact)}")


#9-----------------------------------------------
def eliminar_vocales(cadena_texto):
  type(cadena_texto)
  
  #vocales = "aeiouAEIOU"
  vocales =["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  texto_sin_vocales = ""

  for letra in cadena_texto:
    if letra not in vocales:
      texto_sin_vocales += letra

  return texto_sin_vocales

# Pedir al usuario una cadena de texto
cadena_texto = input("Ingrese una cadena de texto: ")

# Eliminar las vocales
texto_sin_vocales = eliminar_vocales(cadena_texto)

# Imprimir el resultado
print(f"Texto ingresado: {cadena_texto}")
print(f"Texto sin vocales: {texto_sin_vocales}")


#10-----------------------------------------------
meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def formatofinal(fechaf):
    partes = fechaf.split()
    
    # Verificar si la fecha está en el formato mes-día-año o mes día, año
    if len(partes) == 3:
        mes = partes[0]
        dia = partes[1].strip(',')
        anio = partes[2]
    else:
        mes, dia, anio = fechaf.split('/')
    
    # Obtener el índice del mes en la lista de meses
    nmes = meses.index(mes) + 1
    
    # Imprimir la fecha en el formato AAAA-MM-DD
    print(f"{anio:04d}-{nmes:02d}-{int(dia):02d}")

# Ejemplos de uso
fechaf = input("Ingrese la fecha en formato mes-día-año o mes día, año: ")
formatofinal(fechaf)
