class GastosMensuales:
    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self, nombre, cantidad):
        self.gastos[nombre] = cantidad

    def total_gastos(self):
        return sum(self.gastos.values())

    def __str__(self):
        return "\n".join([f"{nombre}: {cantidad} euros" for nombre, cantidad in self.gastos.items()])


# Ejemplo de uso
if __name__ == "__main__":
    gastos = GastosMensuales()

    # Agregar gastos
    gastos.agregar_gasto("Hipoteca y préstamos", 800)
    gastos.agregar_gasto("Alquiler", 850)
    gastos.agregar_gasto("Visa", 100)
    gastos.agregar_gasto("Corte Inglés", 400)
    gastos.agregar_gasto("Parking", 108)
    gastos.agregar_gasto("Colegio", 25)
    gastos.agregar_gasto("Monasterio", 30)
    gastos.agregar_gasto("Luz", 100)
    gastos.agregar_gasto("Teléfono", 140)

    # Imprimir gastos totales
    print("Gastos totales:")
    print(gastos)
    print(f"\nTotal: {gastos.total_gastos()} euros")
