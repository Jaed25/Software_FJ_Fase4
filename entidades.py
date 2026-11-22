from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Entidad(ABC):
    """Clase abstracta para las entidades generales del sistema."""

    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise DatosInvalidosError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        pass


class Cliente(Entidad):
    """Representa un cliente y encapsula sus datos personales."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos 2 caracteres.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise DatosInvalidosError("El correo electrónico no tiene un formato válido.")
        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        limpio = str(valor).replace(" ", "").replace("-", "")
        if not limpio.isdigit() or len(limpio) < 7:
            raise DatosInvalidosError("El teléfono debe contener al menos 7 dígitos.")
        self.__telefono = limpio

    def describir(self):
        return f"Cliente {self.nombre} | correo: {self.correo}"

    def __str__(self):
        return f"{self.identificador} - {self.nombre} ({self.correo})"
