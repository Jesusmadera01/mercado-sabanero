"""Reglas de descuento por volumen de compra."""

# (subtotal mínimo, porcentaje de descuento), de mayor a menor
TRAMOS_VOLUMEN = [
    (500_000, 10),
    (200_000, 5),
]


def porcentaje_descuento_volumen(subtotal):
    """Devuelve el porcentaje de descuento (0, 5 o 10) según el subtotal."""
    for minimo, porcentaje in TRAMOS_VOLUMEN:
        if subtotal >= minimo:
            return porcentaje
    return 0
