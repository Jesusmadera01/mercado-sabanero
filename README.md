# Mercado Sabanero

Módulo de liquidación de compras desarrollado con TDD (Python + pytest).

## Cómo ejecutar las pruebas

    git clone <url-del-repo>
    cd mercado-sabanero
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
    pytest
    pytest --cov=src --cov-report=html
