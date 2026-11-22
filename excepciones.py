class ErrorSistema(Exception):
    """Excepción base del sistema."""


class DatosInvalidosError(ErrorSistema):
    pass


class ServicioNoDisponibleError(ErrorSistema):
    pass


class ReservaNoPermitidaError(ErrorSistema):
    pass
