class CineError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class CuentaExistenteError(CineError):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CuentaNoExistenteError(CineError):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class ContrasenaInvalida(CineError):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class EspaciosSinRellenar(CineError):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CantidadNoDisponible(CineError):
    def __init__(self, mensaje):
        super().__init__(mensaje)
