from datetime import datetime
from excepciones import DatosInvalidosError, ReservaNoPermitidaError


class Reserva:
    """Integra cliente, servicio, duración y estado de una reserva."""

    ESTADOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")

    def __init__(self, codigo, cliente, servicio, duracion, parametros=None):
        if not codigo:
            raise DatosInvalidosError("El código de reserva es obligatorio.")
        if duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")
        self.codigo = str(codigo)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = float(duracion)
        self.parametros = parametros or {}
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ReservaNoPermitidaError("Solo se pueden confirmar reservas pendientes.")
        self.servicio.validar_parametros(**self.parametros)
        self.estado = "Confirmada"
        return f"Reserva {self.codigo} confirmada."

    def cancelar(self):
        if self.estado not in ("Pendiente", "Confirmada"):
            raise ReservaNoPermitidaError("La reserva no se puede cancelar en su estado actual.")
        self.estado = "Cancelada"
        return f"Reserva {self.codigo} cancelada."

    def procesar(self, impuesto=0.0, descuento=0.0):
        if self.estado != "Confirmada":
            raise ReservaNoPermitidaError("La reserva debe estar confirmada para procesarse.")
        costo = self.servicio.calcular_costo(self.duracion, impuesto, descuento)
        self.estado = "Procesada"
        return costo

    def __str__(self):
        return (f"{self.codigo} | {self.cliente.nombre} | {self.servicio.nombre} | "
                f"{self.duracion} h | {self.estado}")
