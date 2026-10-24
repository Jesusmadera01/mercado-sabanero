# Registro de defectos: Mercado Sabanero

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| D-01 | La matriz de casos se subió vacía en el PR #1 (GitHub marcó "Whitespace-only changes") | 1. Crear `docs/matriz_casos.md` y pegar el contenido sin guardar. 2. `git add` y `git commit`. 3. Abrir el PR y revisar **Files changed** | Media | Corregido (se recreó el archivo y se verificó con `wc -c`) |
| D-02 | El plan de pruebas en `main` solo contenía la lista de secciones, sin desarrollar | 1. Hacer `git pull` en `main`. 2. Ejecutar `cat docs/plan_de_pruebas.md` y ver solo 7 líneas | Media | Corregido (rama `docs/plan-completo`) |
| D-03 | Faltaba el caso límite "cantidad igual al stock" en la matriz | 1. Revisar la matriz en el PR #1. 2. Buscar un caso con stock 10 y cantidad 10 | Baja | Corregido (se agregó CP-33) |
| D-04 | El repositorio no tenía `.gitignore`, con riesgo de subir la carpeta `venv/` | 1. Ejecutar `ls -la` en la raíz. 2. Hacer `git add .` y ver `venv/` en `git status` | Alta | Corregido (se creó `.gitignore` antes del primer commit) |
| D-05 | `tests/__init__.py` quedó fuera del commit inicial | 1. Ejecutar `git add .` antes de crear el archivo. 2. Ver que no aparece en `git status` | Baja | Corregido (se agregó con `git add tests/__init__.py`) |
| D-06 | El commit del README quedó en `main` local en lugar de `docs/readme` | 1. Commitear estando en `main`. 2. Ver `Your branch is ahead of 'origin/main' by 1 commit` | Baja | Corregido (`git reset --hard origin/main`) |
