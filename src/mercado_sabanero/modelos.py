from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    codigo: str
    nombre: str
    precio: int        # pesos, sin decimales
    tarifa_iva: int    # 0, 5 o 19
