class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.padres = []

    def agregar_padre(self, padre):
        self.padres.append(padre)

    def __str__(self):
        return f"{self.nombre} - Fecha: {self.fecha}"


class ArbolGenealogico:
    def __init__(self):
        self.eventos = {}

    def agregar_evento(self, evento):
        self.eventos[evento.nombre] = evento

    def agregar_relacion_padres(self, hijo, padre1, padre2):
        if padre1 and padre1.nombre in self.eventos:
            hijo.agregar_padre(padre1)
        if padre2 and padre2.nombre in self.eventos:
            hijo.agregar_padre(padre2)

    def __str__(self):
        arbol_str = ""
        for nombre, evento in self.eventos.items():
            arbol_str += f"{nombre}:\n"
            arbol_str += f"  - {str(evento)}\n"
            for padre in evento.padres:
                arbol_str += f"    - Padre: {padre.nombre}\n"
        return arbol_str


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolGenealogico()

    # Crear eventos
    nacimiento_juan = Evento("Nacimiento de Juan", "01/01/2000")
    nacimiento_maria = Evento("Nacimiento de Maria", "02/02/2002")
    matrimonio_juan_maria = Evento("Matrimonio de Juan y Maria", "03/03/2022")
    nacimiento_pedro = Evento("Nacimiento de Pedro", "04/04/2025")

    # Agregar eventos al árbol genealógico
    arbol.agregar_evento(nacimiento_juan)
    arbol.agregar_evento(nacimiento_maria)
    arbol.agregar_evento(matrimonio_juan_maria)
    arbol.agregar_evento(nacimiento_pedro)

    # Establecer relaciones de padres
    arbol.agregar_relacion_padres(nacimiento_juan, None, None)  # Sin padres por ahora
    arbol.agregar_relacion_padres(nacimiento_maria, None, None)  # Sin padres por ahora
    arbol.agregar_relacion_padres(nacimiento_pedro, nacimiento_juan, matrimonio_juan_maria)
    
    # Imprimir árbol genealógico
    print(arbol)
