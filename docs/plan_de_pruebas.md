# Plan de pruebas ágil: Mercado Sabanero

## 1. Alcance
Solo la lógica de negocio de la liquidación de una compra. No incluye interfaz gráfica ni base de datos. El inventario es un servicio externo que se reemplaza en las pruebas por un doble de prueba (mock). Los valores se manejan en pesos, sin decimales, redondeando al peso más cercano.

Historias cubiertas: HU-01 (carrito), HU-02 (IVA), HU-03 (descuento por volumen), HU-04 (cupones), HU-05 (envío y total) y HU-06 (puntos).

## 2. Estrategia
- Desarrollo guiado por pruebas (TDD): cada criterio de aceptación sigue el ciclo rojo (`test:`), verde (`feat:`) y refactor (`refactor:`).
- Pruebas unitarias automatizadas con patrón AAA (preparar, ejecutar, verificar).
- Revisión entre pares mediante Pull Requests: cada integrante revisa las pruebas del otro.
- Integración local: `pytest` debe pasar antes de cada merge a `main`.

## 3. Tipos de prueba
- **Unitarias:** una por comportamiento esperado de cada criterio de aceptación.
- **Parametrizadas:** valores límite (0, 1, 50, 51 unidades; $199.999, $200.000, $499.999, $500.000; $49.999, $50.000; $149.999, $150.000; 999 y 1.000 pesos).
- **De errores:** cantidad inválida, stock insuficiente, cupón inválido y tarifa de IVA inválida.
- **Con doble de prueba:** inventario simulado con `unittest.mock`.

## 4. Herramientas y justificación
| Herramienta | Uso | Justificación |
|---|---|---|
| Python 3.13 | Lenguaje | Sintaxis simple, ideal para lógica de negocio |
| pytest | Pruebas unitarias | Parametrización y fixtures sencillas |
| unittest.mock | Dobles de prueba | Incluido en la librería estándar |
| pytest-cov | Cobertura | Se integra con pytest |
| Git y GitHub | Control de versiones | Evidencia del ciclo TDD y de la revisión entre pares |

## 5. Criterio de éxito
- Mínimo 20 pruebas unitarias, todas pasando.
- Cobertura de líneas mayor o igual al 80 % en la lógica de negocio.
- El ejemplo del enunciado da total de $250.515 y 250 puntos.
- Cada criterio de aceptación cubierto por al menos una prueba.
- Commits que muestran el ciclo test, feat y refactor en todas las historias.

## 6. Riesgos
| Riesgo | Mitigación |
|---|---|
| Ambigüedad en "productos con IVA suman $150.000" | Interpretación acordada (ver sección 7) y confirmación con la docente |
| Errores de redondeo | Aritmética entera y pruebas con valores que terminan en .5 |
| Dependencia del inventario externo | Mock del inventario en las pruebas |
| Conflictos de merge | Cada integrante trabaja en archivos y ramas distintas |
| Integrante sin commits propios | Reparto de historias y revisión periódica de `git log` |

## 7. Decisiones acordadas
1. **Redondeo:** aritmética entera, por ejemplo `(valor * pct + 50) // 100`.
2. **Límite de 50 unidades:** aplica por cada operación de agregar; el stock se valida contra la cantidad acumulada.
3. **Envío gratis:** "productos con IVA" se interpreta como los productos con tarifa de IVA mayor a 0.
4. **SABANERO10 con subtotal menor a $50.000:** se rechaza con error de cupón inválido.
5. **Fecha de cupones:** la fecha actual se inyecta como parámetro para poder probar cupones vencidos.
