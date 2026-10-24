# Matriz de casos de prueba: Mercado Sabanero

| ID | Historia | Descripción | Datos de entrada | Resultado esperado | Estado |
|---|---|---|---|---|---|
| CP-01 | HU-01 CA1 | Agrega 1 unidad (límite inferior) | stock 100, cantidad 1 | Carrito con 1 unidad | Pendiente |
| CP-02 | HU-01 CA1 | Agrega 25 unidades | stock 100, cantidad 25 | Carrito con 25 unidades | Pendiente |
| CP-03 | HU-01 CA1 | Agrega 50 unidades (límite superior) | stock 100, cantidad 50 | Carrito con 50 unidades | Pendiente |
| CP-04 | HU-01 CA2 | Rechaza 0 unidades | cantidad 0 | CantidadInvalidaError | Pendiente |
| CP-05 | HU-01 CA2 | Rechaza 51 unidades | cantidad 51 | CantidadInvalidaError | Pendiente |
| CP-06 | HU-01 CA2 | Rechaza cantidad negativa | cantidad -1 | CantidadInvalidaError | Pendiente |
| CP-07 | HU-01 CA3 | Stock menor a lo pedido | stock 5, cantidad 10 | StockInsuficienteError | Pendiente |
| CP-08 | HU-01 CA4 | Suma cantidades del mismo producto | agrega 3 y luego 2 | Carrito con 5 unidades | Pendiente |
| CP-09 | HU-02 CA1 | IVA 0 % | valor 18.000, tarifa 0 | IVA 0 | Pendiente |
| CP-10 | HU-02 CA1 | IVA 5 % | valor 30.000, tarifa 5 | IVA 1.500 | Pendiente |
| CP-11 | HU-02 CA1 | IVA 19 % | valor 180.000, tarifa 19 | IVA 34.200 | Pendiente |
| CP-12 | HU-02 CA2 | IVA sobre valor con descuento | valor 171.000, tarifa 19 | IVA 32.490 | Pendiente |
| CP-13 | HU-02 | Tarifa de IVA inválida | tarifa 10 | TarifaIvaInvalidaError | Pendiente |
| CP-14 | HU-03 CA1 | Sin descuento por volumen | subtotal 199.999 | 0 % | Pendiente |
| CP-15 | HU-03 CA2 | Descuento 5 % en el límite | subtotal 200.000 | 5 % | Pendiente |
| CP-16 | HU-03 CA2 | Descuento 5 % en el tope | subtotal 499.999 | 5 % | Pendiente |
| CP-17 | HU-03 CA3 | Descuento 10 % en el límite | subtotal 500.000 | 10 % | Pendiente |
| CP-18 | HU-04 CA1 | SABANERO10 con subtotal mínimo | subtotal 50.000 | 10 % de descuento | Pendiente |
| CP-19 | HU-04 CA1 | SABANERO10 bajo el mínimo | subtotal 49.999 | CuponInvalidoError | Pendiente |
| CP-20 | HU-04 CA2 | ENVIOGRATIS | cupón ENVIOGRATIS | Envío $0 | Pendiente |
| CP-21 | HU-04 CA3 | Cupón inexistente | cupón XYZ | CuponInvalidoError | Pendiente |
| CP-22 | HU-04 CA3 | Cupón vencido | cupón con fecha pasada | CuponInvalidoError | Pendiente |
| CP-23 | HU-04 CA4 | Solo el mayor descuento | volumen 10 % y SABANERO10 | Se aplica solo 10 % | Pendiente |
| CP-24 | HU-05 CA1 | Envío en Sincelejo | municipio Sincelejo, base 100.000 | $8.000 | Pendiente |
| CP-25 | HU-05 CA1 | Envío a otro municipio | municipio Sampués, base 100.000 | $15.000 | Pendiente |
| CP-26 | HU-05 CA2 | Envío gratis en el límite | base IVA 150.000 | $0 | Pendiente |
| CP-27 | HU-05 CA2 | Envío no gratis bajo el límite | base IVA 149.999 | Se cobra envío | Pendiente |
| CP-28 | HU-05 CA3 | Total del ejemplo del enunciado | licuadora, 2 cafés, 4 arroces | Total $250.515 | Pendiente |
| CP-29 | HU-06 CA1 | Sin puntos bajo $1.000 | total 999 | 0 puntos | Pendiente |
| CP-30 | HU-06 CA1 | 1 punto en el límite | total 1.000 | 1 punto | Pendiente |
| CP-31 | HU-06 CA1 | Puntos del ejemplo | total 250.515 | 250 puntos | Pendiente |
| CP-32 | HU-06 CA2 | Cliente ORO doble de puntos | total 250.515, ORO | 500 puntos | Pendiente |
| CP-33 | HU-01 CA1 | Cantidad igual al stock | stock 10, cantidad 10 | Carrito con 10 unidades, sin error | Pendiente |
