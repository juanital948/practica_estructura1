class Secuencia:
    def __init__(self, id, nombre_muestra, secuencia, nivel_riesgo):
        self.id: int = id
        self.nombre_muestra: str = nombre_muestra
        self.secuencia: str = secuencia
        self.nivel_riesgo: int = nivel_riesgo

    
    def mostrar(self):
        print(f"ID: {self.id}")
        print(f"Muestra: {self.nombre_muestra}")
        print(f"Secuencia: {self.secuencia}")
        print(f"Nivel de riesgo: {self.nivel_riesgo}")
        print("\n")


    def contar(self, patron, secuencia = None):

        if secuencia is None:
            secuencia = self.secuencia

        if len(secuencia) < len(patron):
            return 0

        if secuencia[:len(patron)] == patron:
            return 1 + self.contar(patron, secuencia[1:]) 
        else:
            return self.contar(patron, secuencia[1:])


def registrar(lista):
    opcion = input("¿Quiere registrar una nueva secuencia? (SI/NO): ")

    if opcion != "SI":
        return
        
    id = int(input("ID: "))
    nombre_muestra = str(input("Nombre muestra: "))
    secuencia = str(input("Secuencia: "))
    nivel_riesgo= int(input("Nivel riesgo: "))

    nueva = Secuencia(id,nombre_muestra,secuencia,nivel_riesgo)
    lista.append(nueva)

    return registrar(lista)


def nivel_riesgo_promedio(lista, suma = 0, i= 0):
    
    if len(lista) == 0:
        return 0

    if i == len(lista):
        return suma / len(lista)
    
    return nivel_riesgo_promedio(lista, suma + lista[i].nivel_riesgo, i + 1)


def secuencia_larga(lista, i = 0, mayor = None):

    if len(lista) == 0:
        return None
    
    if i == len(lista):
        return mayor

    if mayor is None or len(lista[i].secuencia) > len(mayor.secuencia):
        mayor = lista[i]

    return secuencia_larga(lista, i+1, mayor)


def subcadenas_posibles(secuencia, i = 0, f = 0):

    if i == len(secuencia):
        return []
    
    if f == len(secuencia):
        return subcadenas_posibles(secuencia, i + 1, i + 1)
    
    return [secuencia[i:f+1]] + subcadenas_posibles(secuencia, i, f + 1)
    


def mas_nucleotidos(secuencia, i = 0):
    if i == len(secuencia):
        return 0
    
    if secuencia[i] == "A":
        return 1 + mas_nucleotidos(secuencia, i + 1)
    elif secuencia[i] == "T":
        return -1 + mas_nucleotidos(secuencia, i + 1)
    else:
        return mas_nucleotidos(secuencia, i + 1)

def mutacion_genetica(secuencia, i = 0):
    if i == len(secuencia):
        return ""
    
    if secuencia[i] == "A":
        nueva = "T"
    elif secuencia[i] == "T":
        nueva = "A"
    else:
        nueva = secuencia[i]

    return nueva + mutacion_genetica(secuencia, i + 1)


lista_secuencias = []

registrar(lista_secuencias)

print("\n")
print("Registros guardados:")

for s in lista_secuencias:
    s.mostrar()
        

patron = "AG"
print("Conteo patrón en cada secuencia:")
for s in lista_secuencias:
    conteo = s.contar(patron)
    print(f"Muestra con el nombre {s.nombre_muestra}: tiene como resultado {conteo} ocurrencias")

("\n")

print("Promedio de nivel de riesgo:")
promedio = nivel_riesgo_promedio(lista_secuencias)
print(f"Promedio: {promedio}")

("\n")

print("Secuencia más larga:")
larga = secuencia_larga(lista_secuencias)
if larga:
    larga.mostrar()
else:
    print("No hay secuencias registradas")

("\n")

print("Subcadenas posibles de cada secuencia:")
for s in lista_secuencias:
    print(f"Muestra: {s.nombre_muestra}")
    resultado = subcadenas_posibles(s.secuencia)
    print(resultado)

print("\n")

print("¿Hay más A que T en cada secuencia?")
for s in lista_secuencias:
    resultado = mas_nucleotidos(s.secuencia)
    if resultado > 0:
        print(f"La muestra {s.nombre_muestra} tiene más A que T")
    else:
        print(f"La muestra {s.nombre_muestra} NO tiene más A que T")

("\n")

print("Simulación de mutación genética:")
for s in lista_secuencias:
    nueva = mutacion_genetica(s.secuencia)
    print(f"Muestra: {s.nombre_muestra}")
    print("Original:", s.secuencia)
    print("Mutada:", nueva)
