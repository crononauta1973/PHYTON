class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.marcar_completada()
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            print("La posición ingresada no es válida.")

# Función para manejar la entrada del usuario
def obtener_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 1:
                raise ValueError
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero positivo.")

# Ejemplo de uso del programa
if __name__ == "__main__":
    lista_tareas = ListaTareas()

    while True:
        print("\n1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = obtener_entero_positivo("\nIngrese el número de la opción deseada: ")

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            tarea = Tarea(descripcion)
            lista_tareas.agregar_tarea(tarea)
            print("Tarea agregada correctamente.")

        elif opcion == 2:
            lista_tareas.mostrar_tareas()
            posicion = obtener_entero_positivo("Ingrese la posición de la tarea completada: ") - 1
            lista_tareas.marcar_completada(posicion)

        elif opcion == 3:
            print("\nLista de tareas:")
            lista_tareas.mostrar_tareas()

        elif opcion == 4:
            lista_tareas.mostrar_tareas()
            posicion = obtener_entero_positivo("Ingrese la posición de la tarea a eliminar: ") - 1
            lista_tareas.eliminar_tarea(posicion)
            print("Tarea eliminada correctamente.")

        elif opcion == 5:
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
