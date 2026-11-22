from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


class Servicio(ABC):
    """Clase abstracta base para los servicios ofrecidos."""

    def __init__(self, codigo, nombre, tarifa_hora, disponible=True):
        if not codigo or not nombre:
            raise DatosInvalidosError("El código y el nombre del servicio son obligatorios.")
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise DatosInvalidosError("La tarifa por hora debe ser un número positivo.")
        self.codigo = str(codigo)
        self.nombre = str(nombre)
        self.tarifa_hora = float(tarifa_hora)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.nombre} no está disponible.")

    # Sobrecarga simulada mediante parámetros opcionales:
    # calcular_costo(horas), calcular_costo(horas, impuesto),
    # calcular_costo(horas, impuesto, descuento).
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.tarifa_hora * horas
        return round(subtotal * (1 + impuesto) * (1 - descuento), 2)

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass


class ReservaSala(Servicio):
    def describir(self):
        return f"Sala: {self.nombre}. Tarifa: ${self.tarifa_hora:.2f}/hora."

    def validar_parametros(self, **kwargs):
        capacidad = kwargs.get("capacidad")
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser un entero positivo.")
        self.validar_disponibilidad()


class AlquilerEquipo(Servicio):
    def describir(self):
        return f"Equipo: {self.nombre}. Tarifa: ${self.tarifa_hora:.2f}/hora."

    def validar_parametros(self, **kwargs):
        cantidad = kwargs.get("cantidad", 1)
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidosError("La cantidad de equipos debe ser un entero positivo.")
        self.validar_disponibilidad()


class Asesoria(Servicio):
    def describir(self):
        return f"Asesoría: {self.nombre}. Tarifa: ${self.tarifa_hora:.2f}/hora."

    def validar_parametros(self, **kwargs):
        especialidad = kwargs.get("especialidad")
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            raise DatosInvalidosError("Debe indicar una especialidad válida.")
        self.validar_disponibilidad()
