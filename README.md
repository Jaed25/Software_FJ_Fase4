# Software_FJ_Fase4
Sistema de gestión de clientes, servicios y reservas desarrollado en Python.

# 1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite administrar clientes, servicios y reservas mediante un sistema organizado de gestión empresarial.

El programa está diseñado para registrar clientes, gestionar diferentes tipos de servicios, controlar la disponibilidad, crear y confirmar reservas, calcular costos de operación y administrar situaciones excepcionales.

La aplicación implementa los principios de la programación orientada a objetos (POO), utilizando abstracción, encapsulación, herencia y polimorfismo. También incorpora mecanismos de validación de datos, excepciones personalizadas y registro de eventos mediante archivos de log.

# 2. Objetivo del sistema

Desarrollar una aplicación modular que facilite la administración de clientes, servicios y reservas, garantizando la validación de información, el control de operaciones y el manejo adecuado de errores mediante técnicas de programación orientada a objetos.

# 3. Funcionalidades principales

3.1. Gestión de clientes

Registrar clientes con identificador, nombre, correo electrónico y teléfono.

Validar la información ingresada.

Evitar registros con datos incorrectos.

Controlar identificadores duplicados.

Consultar los clientes registrados.

3.2. Gestión de servicios

El sistema permite registrar tres categorías de servicios especializados:

Reserva de salas

Registrar salas con nombre y tarifa por hora.

Validar la capacidad de las salas.

Comprobar la disponibilidad antes de confirmar una reserva.

Alquiler de equipos

Registrar equipos y sus tarifas.

Validar la cantidad de equipos solicitados.

Controlar la disponibilidad del servicio.

Asesorías

Registrar servicios de asesoría.

Establecer tarifas por hora.

Validar la especialidad requerida.

3.3. Gestión de reservas

Crear reservas asociadas a clientes y servicios registrados.

Asignar códigos únicos a las reservas.

Establecer la duración y los parámetros de cada servicio.

Confirmar reservas pendientes.

Cancelar reservas pendientes o confirmadas.

Procesar reservas confirmadas.

Controlar los estados de cada reserva.

3.4. Cálculo de costos

El sistema calcula el costo de los servicios teniendo en cuenta:

Tarifa por hora.

Duración del servicio.

Impuestos aplicables.

Descuentos opcionales.

La fórmula utilizada es:

Costo total = Tarifa por hora × Duración × (1 + Impuesto) × (1 - Descuento).

Los valores se presentan con dos decimales.

3.5. Manejo de excepciones

Software FJ incorpora excepciones personalizadas para controlar situaciones incorrectas, como:

Datos inválidos.

Servicios no disponibles.

Operaciones de reserva no permitidas.

Intentos de procesar reservas sin confirmar.

También implementa estructuras try, except, else y finally, además del encadenamiento de excepciones para conservar información sobre los errores originales.

3.6. Registro de eventos y errores

El sistema utiliza el módulo logging de Python para registrar eventos y errores durante la ejecución.

El archivo generado es:

software_fj.log

Este archivo permite consultar:

Registro de clientes.

Registro de servicios.

Creación de reservas.

Operaciones incorrectas.

Excepciones y detalles técnicos de los errores.

# 4. Arquitectura del proyecto

El programa está organizado en módulos independientes para facilitar su mantenimiento y comprensión.

Archivo

Funcionalidad

main.py

Punto de entrada y ejecución del programa.

entidades.py

Clases de entidades y gestión de clientes.

excepciones.py

Definición de excepciones personalizadas.

servicios.py

Clases abstractas y servicios especializados.

reservas.py

Creación, confirmación, cancelación y procesamiento de reservas.

sistema.py

Administración general e integración de clientes, servicios y reservas.

README.md

Documentación del proyecto.

.gitignore

Exclusión de archivos temporales y registros.

# 5. Principios de programación orientada a objetos

El desarrollo incorpora los siguientes conceptos:

Abstracción: utilización de clases abstractas para establecer estructuras generales de entidades y servicios.

Encapsulación: protección y control de atributos mediante propiedades y validaciones.

Herencia: reutilización de características y comportamientos mediante clases derivadas.

Polimorfismo: implementación de métodos como describir() y validar_parametros() con comportamientos específicos para cada tipo de servicio.

Sobrecarga: simulación mediante parámetros opcionales en el método calcular_costo(), permitiendo incorporar impuestos y descuentos.

# 6. Tecnologías utilizadas

Python 3.14.

Programación orientada a objetos.

Módulo abc para clases abstractas.

Módulo datetime para gestionar fechas y horas.

Módulo logging para registrar eventos.

Excepciones personalizadas.

Visual Studio Code como entorno de desarrollo.

Git y GitHub para el control de versiones.

# 7. Instalación y ejecución

Requisitos previos

Tener Python instalado.
Tener Visual Studio Code o una terminal compatible.
Descargar el proyecto

Clonar el repositorio:
git clone https://github.com/Jaed25/Software_FJ_Fase4.git

Ingresar a la carpeta:
cd Software_FJ_Fase4
Ejecutar el programa

Desde la terminal ejecutar:
py main.py

El programa mostrará un menú principal con las siguientes opciones:

Ejecutar demostración de operaciones.

Listar clientes.

Listar servicios.

Listar reservas.

Salir.

# 8. Demostración de funcionamiento

El sistema incluye una demostración integrada de 14 operaciones que permite verificar diferentes escenarios:

Registro válido de un cliente.
Control de registro inválido de cliente.
Registro de una sala.
Registro de un equipo.
Registro de una asesoría.
Control de una tarifa inválida.
Creación y confirmación de una reserva.
Procesamiento y cálculo del costo con impuesto.
Control de procesamiento de una reserva pendiente.
Validación de un servicio no disponible.
Cancelación de una reserva.
Encadenamiento de excepciones.
Ejecución del bloque else.
Ejecución del bloque finally.

# 9. Almacenamiento de información

Los clientes, servicios y reservas se administran mediante listas internas de Python durante la ejecución del programa.
El archivo software_fj.log conserva los registros de eventos y errores. La información operativa no se almacena permanentemente en una base de datos.

# 10. Autoría y propósito académico

Proyecto desarrollado como actividad académica de programación de la Universidad Nacional Abierta y a Distancia (UNAD).

Proyecto: Software FJ
Lenguaje: Python
Repositorio: https://github.com/Jaed25/Software_FJ_Fase4
