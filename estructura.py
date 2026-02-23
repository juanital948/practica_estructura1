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

lista_secuencias = []

registrar(lista_secuencias)

print("Registros guardados:")
for s in lista_secuencias:
    s.mostrar()


def contar(secuencia, patron):
    pass
