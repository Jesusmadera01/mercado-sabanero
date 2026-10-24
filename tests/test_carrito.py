from unittest.mock import Mock

import pytest

from mercado_sabanero.carrito import Carrito
from mercado_sabanero.modelos import Producto


@pytest.mark.parametrize("cantidad", [1, 25, 50])
def test_agregar_cantidad_valida_deja_producto_en_carrito(cantidad):
    # Arrange
    inventario = Mock()
    inventario.obtener_stock.return_value = 100
    arroz = Producto("A1", "Arroz", 4500, 0)
    carrito = Carrito(inventario)
    # Act
    carrito.agregar(arroz, cantidad)
    # Assert
    assert carrito.items[0].producto == arroz
    assert carrito.items[0].cantidad == cantidad