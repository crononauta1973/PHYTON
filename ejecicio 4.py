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


class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
        super().__init__(nombre, cedula, telefono)
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

    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)


class EmpleadoSubcontratado(Empleado):
    def __init__(self, nombre, cedula, telefono, empresa_responsable):
        super().__init__(nombre, cedula, telefono)
        self._empresa_responsable = empresa_responsable

    def set_empresa_responsable(self, empresa_responsable):
        self._empresa_responsable = empresa_responsable

    def get_empresa_responsable(self):
        return self._empresa_responsable


# Creación de instancias de las clases
subContratado1 = EmpleadoSubcontratado("Roberto Flores Morales", 123456789, 88888888, "Coca-Cola")
subContratado2 = EmpleadoSubcontratado("Ana Mora Cruz", 223446789, 77777777, "Pepsi")

empleadoD = EmpleadoDefinido("Jeff Muñoz Castro", 345687324, 66666666, 3, 500000, 3)
empleadoD2 = EmpleadoDefinido("María Gonzáles Pérez", 983456783, 99999999, 6, 450000, 2)

# Imprimir información
print("*** Empleados subcontratados ***")
print("\n****Empleado 1****")
print("Nombre: " + subContratado1.get_nombre() +
      "\nCédula: " + str(subContratado1.get_cedula()) +
      "\nTeléfono: " + str(subContratado1.get_telefono()) +
      "\nEmpresa responsable: " + subContratado1.get_empresa_responsable())

print("\n****Empleado 2****")
print("Nombre: " + subContratado2.get_nombre() +
      "\nCédula: " + str(subContratado2.get_cedula()) +
      "\nTeléfono: " + str(subContratado2.get_telefono()) +
      "\nEmpresa responsable: " + subContratado2.get_empresa_responsable())

print("\n*** Empleados de tiempo definido ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoD.get_nombre() +
      "\nCédula: " + str(empleadoD.get_cedula()) +
      "\nTeléfono: " + str(empleadoD.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoD.get_nPlaza()) +
      "\nDuracion contrato: " + str(empleadoD.get_duracion_contrato()) + " meses" +
      "\nSalario total: " + str(empleadoD.calcularSalarioTotal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoD2.get_nombre() +
      "\nCédula: " + str(empleadoD2.get_cedula()) +
      "\nTeléfono: " + str(empleadoD2.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoD2.get_nPlaza()) +
      "\nDuración contrato " + str(empleadoD2.get_duracion_contrato()) + " meses" +
      "\nSalario total: " + str(empleadoD2.calcularSalarioTotal()))
