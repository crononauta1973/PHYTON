class Empleado:
    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

# Crear instancias de la clase Empleado
empleados = [
    Empleado("Dacila", 45, "Directora"),
    Empleado("Lorena", 44, "Jefa de equipo"),
    Empleado("Claudia", 30, "Comercial"),
    Empleado("Karen", 30, "Administrativa"),
    Empleado("Victor", 55, "Comercial"),
    Empleado("Ignacio", 51, "Interventor"),
    Empleado("Alejandro", 54, "Administrativo"),
    Empleado("Antonio", 35, "Comercial")
]

# Imprimir la lista de empleados
for empleado in empleados:
    print("Nombre:", empleado.nombre)
    print("Edad:", empleado.edad)
    print("Cargo:", empleado.cargo)
    print()
