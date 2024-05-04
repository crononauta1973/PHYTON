class EmpleadoDefinido:
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
        #constructor de la clase empleado
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        #Nuevos atributos
        self._nPlaza = nPlaza
        self._salarioBase = salarioBase
        self._duracion_contrato = duracion_contrato

    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza

    def get_nPlaza(self):
        return self._nPlaza

    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase

    def get_salarioBase(self):
        return self._salarioBase

    def set_duracion_contrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato

    def get_duracion_contrato(self):
        return self._duracion_contrato

    #calcula el salario total
    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)

