import logging
from excepciones import ErrorSistema, DatosInvalidosError
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva


logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)


class SistemaFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("El objeto suministrado no es un cliente.")
        if any(c.identificador == cliente.identificador for c in self.clientes):
            raise DatosInvalidosError("Ya existe un cliente con ese identificador.")
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.identificador)
        return cliente

    def registrar_servicio(self, servicio):
        if not hasattr(servicio, "calcular_costo"):
            raise DatosInvalidosError("El objeto no corresponde a un servicio válido.")
        if any(s.codigo == servicio.codigo for s in self.servicios):
            raise DatosInvalidosError("Ya existe un servicio con ese código.")
        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.codigo)
        return servicio

    def crear_reserva(self, reserva):
        if not any(c.identificador == reserva.cliente.identificador for c in self.clientes):
            raise DatosInvalidosError("El cliente no está registrado.")
        if not any(s.codigo == reserva.servicio.codigo for s in self.servicios):
            raise DatosInvalidosError("El servicio no está registrado.")
        if any(r.codigo == reserva.codigo for r in self.reservas):
            raise DatosInvalidosError("Ya existe una reserva con ese código.")
        self.reservas.append(reserva)
        logging.info("Reserva creada: %s", reserva.codigo)
        return reserva

    def ejecutar_demo(self):
        """Ejecuta más de 10 operaciones, incluyendo casos correctos e incorrectos."""
        print("\n========== DEMOSTRACIÓN SOFTWARE FJ ==========")

        # 1. Registro válido de cliente.
        cliente = self.registrar_cliente(
            Cliente("C001", "Laura Gómez", "laura@gmail.com", "3001234567")
        )
        print("1. Cliente registrado:", cliente)

        # 2. Registro inválido de cliente.
        try:
            Cliente("C002", "A", "correo-invalido", "12")
        except DatosInvalidosError as error:
            logging.exception("Error en registro de cliente")
            print("2. Cliente inválido controlado:", error)

        # 3-5. Creación de tres servicios especializados.
        sala = self.registrar_servicio(ReservaSala("S01", "Sala principal", 50000))
        equipo = self.registrar_servicio(AlquilerEquipo("E01", "Proyector", 20000))
        asesoria = self.registrar_servicio(Asesoria("A01", "Asesoría Python", 80000))
        print("3-5. Servicios registrados:", sala.nombre, equipo.nombre, asesoria.nombre)

        # 6. Intento de crear un servicio con tarifa inválida.
        try:
            ReservaSala("S02", "Sala inválida", -100)
        except DatosInvalidosError as error:
            logging.exception("Error al crear servicio")
            print("6. Servicio inválido controlado:", error)

        # 7. Reserva válida y confirmación.
        reserva1 = Reserva("R001", cliente, sala, 2, {"capacidad": 10})
        self.crear_reserva(reserva1)
        print("7.", reserva1.confirmar())

        # 8. Procesamiento y cálculo con impuesto.
        total = reserva1.procesar(impuesto=0.19)
        print(f"8. Reserva procesada. Total: ${total:,.2f}")

        # 9. Intento de procesar una reserva pendiente.
        reserva2 = Reserva("R002", cliente, equipo, 3, {"cantidad": 1})
        self.crear_reserva(reserva2)
        try:
            reserva2.procesar()
        except ErrorSistema as error:
            logging.exception("Intento de procesar reserva no confirmada")
            print("9. Operación no permitida controlada:", error)

        # 10. Servicio no disponible.
        servicio_no_disponible = ReservaSala("S03", "Sala ocupada", 45000, False)
        self.registrar_servicio(servicio_no_disponible)
        reserva3 = Reserva("R003", cliente, servicio_no_disponible, 1, {"capacidad": 5})
        self.crear_reserva(reserva3)
        try:
            reserva3.confirmar()
        except ErrorSistema as error:
            logging.exception("Servicio no disponible")
            print("10. Servicio no disponible controlado:", error)

        # 11. Cancelación correcta.
        print("11.", reserva2.cancelar())

        # 12. Ejemplo de encadenamiento de excepciones.
        try:
            try:
                float("dato-no-numerico")
            except ValueError as error_interno:
                raise DatosInvalidosError("No fue posible convertir el dato.") from error_interno
        except DatosInvalidosError as error:
            logging.exception("Error encadenado")
            print("12. Excepción encadenada controlada:", error)

        # Ejemplos de else y finally.
        try:
            valor = int("25")
        except ValueError:
            logging.exception("Error durante la conversión.")
            print("Conversión incorrecta.")
        else:
            print("13. Bloque else: conversión correcta =", valor)
        finally:
            print("14. Bloque finally: validación finalizada.")

        print("\nReservas registradas:")
        for reserva in self.reservas:
            print("-", reserva)
        print("\nLos eventos y errores se guardaron en software_fj.log")


    def menu(self):
        while True:
            print("\n===== SOFTWARE FJ =====")
            print("1. Ejecutar demostración de operaciones")
            print("2. Listar clientes")
            print("3. Listar servicios")
            print("4. Listar reservas")
            print("0. Salir")
            opcion = input("Seleccione una opción: ").strip()
            try:
                if opcion == "1":
                    self.ejecutar_demo()
                elif opcion == "2":
                    for cliente in self.clientes:
                        print(cliente)
                elif opcion == "3":
                    for servicio in self.servicios:
                        print(servicio.describir())
                elif opcion == "4":
                    for reserva in self.reservas:
                        print(reserva)
                elif opcion == "0":
                    print("Gracias por utilizar Software FJ.")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except Exception as error:
                logging.exception("Error no previsto en el menú")
                print("Se presentó un error controlado:", error)
