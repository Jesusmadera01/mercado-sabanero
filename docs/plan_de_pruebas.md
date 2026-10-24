Alcance: solo lógica de negocio, sin interfaz ni base de datos; inventario simulado con mock.
Estrategia: pruebas unitarias con TDD (rojo, verde, refactor) y revisión entre pares.
Tipos de prueba: unitarias, parametrizadas (valores límite), de errores y con doble de prueba.
Herramientas y justificación: Python, pytest, unittest.mock, pytest-cov, Git/GitHub.
Criterio de éxito: todas las pruebas pasan, cobertura ≥ 80 %, el ejemplo del enunciado da $250.515 y 250 puntos.
Riesgos: ambigüedad en “IVA suman $150.000”, redondeo, dependencia del inventario, conflictos de merge.
Decisiones acordadas: redondeo, límite de 50 unidades, cupón con subtotal bajo, fecha inyectada.