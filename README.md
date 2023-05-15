# Rapida Introduccion a CI/CD

[![codecov](https://codecov.io/gh/valegui/intro-cicd/branch/main/graph/badge.svg?token=5I2LL0ZHW7)](https://codecov.io/gh/valegui/intro-cicd)

Este repositorio es un ejemplo para mostrar como configurar un flujo CI/CD (sencillo) para un codigo Python y contiene ejemplo de documentacion con Sphinx.

## CI/CD

CI con GitHub Actions (en .github/workflows)

## Instalacion y uso 

```
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

### build local de documentacion

```
cd docs
make html
```

### pre-commit
```
pre-commit install
```

## GitHub Pages

https://valegui.github.io/intro-cicd/