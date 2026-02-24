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