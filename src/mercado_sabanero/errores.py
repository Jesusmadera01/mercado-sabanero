class CantidadInvalidaError(ValueError):
    """Cantidad fuera del rango permitido (1 a 50)."""


class StockInsuficienteError(Exception):
    """El inventario no tiene unidades suficientes."""


class CuponInvalidoError(Exception):
    """Cupón inexistente, vencido o que no cumple condiciones."""


class TarifaIvaInvalidaError(ValueError):
    """Tarifa de IVA distinta de 0, 5 o 19."""
