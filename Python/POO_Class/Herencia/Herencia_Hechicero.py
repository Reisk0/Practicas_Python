# Clase base
class Hechicero: 
    def __init__(self, nombre, elemento):
        self.nombre = nombre
        self.elemento = elemento

    def wizard(self): 
        print(f"Mi nombre es {self.nombre}, me especializo en {self.elemento}")

# Clase hija que hereda de Hechicero
class MagoOscuro(Hechicero):  # ← Aquí sí hereda correctamente
    def wizard(self):  # ← Sobrescribimos el método con otro mensaje
        print(f"Yo soy {self.nombre}, el portador de la {self.elemento}...")

# Creamos objetos
mago_luz = Hechicero("Cacian", "Magia Luminus")
mago_oscuridad = MagoOscuro("Lucian", "Magia Tenebris")

# Llamamos a los métodos
mago_luz.wizard()          # Sale: Mi nombre es Cacian, me especializo en Magia Luminus
mago_oscuridad.wizard()    # Sale: Yo soy Lucian, el portador de la Magia Tenebris...





# Clase base
class Criaturas: 
    def __init__(self, nombre, elemento, nivel_de_poder):
        self.nombre = nombre
        self.elemento = elemento
        self.nivel_de_poder = nivel_de_poder  # ← Agregamos esto

# Clase hija que hereda de Criaturas
class Dragon(Criaturas):
    def presentarse(self): 
        self.nivel_de_poder += 150  # Aumentamos el poder
        print(f"🔥 Mi nombre es {self.nombre}, mi elemento es {self.elemento}, mi nivel de poder es {self.nivel_de_poder}")

# Creamos un objeto tipo Dragon
mi_dragon = Dragon("Altius", "Fuego", 300)

# Llamamos al método
mi_dragon.presentarse()



