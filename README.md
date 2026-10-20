# Proyecto aplicado: reconstrucción tomográfica

Este repositorio contiene un notebook de Jupyter por ejercicio del proyecto de Métodos Computacionales. Los notebooks están preparados para ejecutarse de principio a fin de manera independiente.

## Requisitos

Se recomienda utilizar Python 3.11 y crear un entorno virtual. Las dependencias utilizadas están enumeradas en `requirements.txt` y pueden instalarse con:

```powershell
python -m pip install -r requirements.txt
```

Después de instalar las dependencias, se debe seleccionar como kernel de cada notebook el intérprete del entorno virtual. En Windows, si el entorno se creó en la raíz del proyecto, su ruta es:

```text
.venv\Scripts\python.exe
```

## Bibliotecas

Los cálculos numéricos y las visualizaciones utilizan principalmente `numpy`, `scipy` y `matplotlib`.

También se utiliza `pandas` en los ejercicios 5, 6, 9 y 10 únicamente para organizar y presentar los resultados en forma de tablas. `pandas` no interviene en los cálculos numéricos ni en los métodos de reconstrucción. Las tablas estilizadas requieren además `jinja2`.

## Archivos auxiliares

El ejercicio 10 necesita los siguientes archivos, que deben conservarse en la misma carpeta que el notebook:

- `cargar_datos_tomografia.py`
- `datos_tomografia_final_128.npz`

La carpeta `figuras/` contiene las visualizaciones exportadas de los notebooks. Los nombres siguen el formato `ejercicio_XX_figura_YY.png`.

El archivo `uso_ia.txt` documenta el uso de herramientas de IA generativa durante el desarrollo y la revisión del proyecto.
