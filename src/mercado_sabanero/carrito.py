from dataclasses import dataclass

from mercado_sabanero.modelos import Producto


@dataclass
class ItemCarrito:
    producto: Producto
    cantidad: int


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self.items = []

    def agregar(self, producto, cantidad):
        self.items.append(ItemCarrito(producto, cantidad))
