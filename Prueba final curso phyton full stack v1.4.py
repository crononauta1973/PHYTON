class Tarea:
    def __init__(self, descripcion, completada=False):
        # Inicialización de una tarea con una descripción y estado (por defecto, no completada)
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        # Método para marcar una tarea como completada
        self.completada = True

    def __str__(self):
        # Método para representar una tarea como una cadena de texto
        # Muestra la descripción de la tarea y su estado (completada o pendiente)
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaTareas:
    def __init__(self):
        # Inicialización de la lista de tareas vacía
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Método para agregar una nueva tarea a la lista
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        # Método para marcar una tarea como completada, dada su posición en la lista
        try:
            tarea = self.tareas[posicion]  # Obtener la tarea en la posición indicada
            tarea.marcar_completada()  # Marcar la tarea como completada
        except IndexError:
            # Manejar el caso en que la posición ingresada no exista en la lista
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        # Método para imprimir en pantalla todas las tareas pendientes
        for i, tarea in enumerate(self.tareas):
            print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, posicion):
        # Método para eliminar una tarea de la lista, dada su posición
        try:
            del self.tareas[posicion]  # Eliminar la tarea en la posición indicada
        except IndexError:
            # Manejar el caso en que la posición ingresada no exista en la lista
            print("La posición ingresada no es válida.")

# Función para manejar la entrada del usuario y garantizar un entero positivo
def obtener_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 1:
                raise ValueError
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero positivo.")

# Programa principal
if __name__ == "__main__":
    lista_tareas = ListaTareas()  # Crear una instancia de la lista de tareas

    print("¡Bienvenidos a la gestión de tareas para el viaje de la familia García al Polo Norte!")

    while True:
        # Menú de opciones para el usuario
        print("\n1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = obtener_entero_positivo("\nIngrese el número de la opción deseada: ")

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            tarea = Tarea(descripcion)  # Crear una nueva tarea con la descripción ingresada
            lista_tareas.agregar_tarea(tarea)  # Agregar la tarea a la lista
            print("Tarea agregada correctamente.")

        elif opcion == 2:
            lista_tareas.mostrar_tareas()  # Mostrar todas las tareas pendientes
            posicion = obtener_entero_positivo("Ingrese la posición de la tarea completada: ") - 1
            lista_tareas.marcar_completada(posicion)  # Marcar la tarea seleccionada como completada

        elif opcion == 3:
            print("\nLista de tareas:")
            lista_tareas.mostrar_tareas()  # Mostrar todas las tareas pendientes

        elif opcion == 4:
            lista_tareas.mostrar_tareas()  # Mostrar todas las tareas pendientes
            posicion = obtener_entero_positivo("Ingrese la posición de la tarea a eliminar: ") - 1
            lista_tareas.eliminar_tarea(posicion)  # Eliminar la tarea seleccionada

        elif opcion == 5:
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
