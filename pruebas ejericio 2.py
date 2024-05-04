class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_cedula(self, cedula):
        self._cedula = cedula

    def get_cedula(self):
        return self._cedula

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
