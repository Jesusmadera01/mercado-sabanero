# Mercado Sabanero

Módulo de liquidación de compras para la tienda en línea Mercado Sabanero (Sincelejo, Sucre). Calcula carrito, IVA, descuentos, cupones, envío, total y puntos de fidelización.

Proyecto de la Electiva Profesional en Ingeniería de Software (Agilidad Continua), Corporación Universitaria del Caribe (CECAR).

## Integrantes

| Integrante | Usuario de GitHub |
|---|---|
| Jesús Madera | Jesusmadera01 |
| Alex DG | AlexDG99 |

Docente: Laudyt María Lambraño Pérez (colaboradora del repositorio).

## Alcance

Solo lógica de negocio. No tiene interfaz gráfica ni base de datos. El inventario es un servicio externo que se reemplaza en las pruebas por un doble de prueba (mock). Los valores se manejan en pesos, sin decimales, redondeando al peso más cercano.

## Herramientas

| Herramienta | Uso |
|---|---|
| Python 3.13 | Lenguaje |
| pytest | Pruebas unitarias y parametrizadas |
| unittest.mock | Doble de prueba del inventario |
| pytest-cov | Cobertura de líneas |
| Git y GitHub | Control de versiones y revisión entre pares |

## Requisitos previos

- Python 3.10 o superior
- Git (en Windows, usar Git Bash)

## Instalación

```bash
git clone https://github.com/Jesusmadera01/mercado-sabanero.git
cd mercado-sabanero
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
# source venv/bin/activate        # Linux o macOS
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

```bash
pytest                         # todas las pruebas
pytest -v                      # con el nombre de cada prueba
pytest tests/test_carrito.py   # un archivo específico
```

## Cómo generar la cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
start htmlcov/index.html       # abre el reporte en el navegador (Windows)
```

El criterio de éxito es una cobertura de líneas mayor o igual al 80 %.

## Estructura del proyecto

```
mercado-sabanero/
├── src/mercado_sabanero/    # lógica de negocio
│   ├── carrito.py
│   ├── iva.py
│   ├── descuentos.py
│   ├── cupones.py
│   ├── envio.py
│   ├── puntos.py
│   ├── liquidador.py        # integra todas las reglas
│   ├── modelos.py
│   └── errores.py
├── tests/                   # pruebas unitarias
├── docs/                    # plan, matriz de casos y defectos
├── pytest.ini
└── requirements.txt
```

## Decisiones de diseño

1. **Redondeo:** aritmética entera, por ejemplo `(valor * pct + 50) // 100`, para no depender del redondeo del lenguaje.
2. **Límite de 50 unidades:** aplica a cada operación de agregar; el stock se valida contra la cantidad acumulada.
3. **Envío gratis:** "productos con IVA" se interpreta como los productos con tarifa de IVA mayor a 0.
4. **SABANERO10 con subtotal menor a $50.000:** se rechaza con `CuponInvalidoError`.
5. **Fecha de cupones:** la fecha actual se inyecta como parámetro para poder probar cupones vencidos.
6. **Descuentos:** el descuento se aplica por línea y el IVA se calcula sobre el valor ya descontado.

## Documentación

- [Plan de pruebas ágil](docs/plan_de_pruebas.md)
- [Matriz de casos de prueba](docs/matriz_casos.md)
- [Registro de defectos](docs/defectos.md)

## Uso de inteligencia artificial

Se usó IA como apoyo para orientar el proceso y proponer borradores de código y documentos. Cada integrante revisó, entendió y puede explicar cualquier línea del código y de las pruebas.
