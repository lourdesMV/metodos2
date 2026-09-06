#!/usr/bin/env python3
"""Carga el dataset del ejercicio final de tomografia."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix


def _cargar_csr(datos: np.lib.npyio.NpzFile, prefijo: str) -> csr_matrix:
    return csr_matrix(
        (
            datos[f"{prefijo}_data"],
            datos[f"{prefijo}_indices"],
            datos[f"{prefijo}_indptr"],
        ),
        shape=tuple(datos[f"{prefijo}_shape"]),
    )


def cargar_datos_tomografia(ruta: str | Path) -> dict:
    with np.load(ruta, allow_pickle=False) as datos:
        return {
            "A": _cargar_csr(datos, "A"),
            "b": datos["b"].copy(),
            "n": int(datos["n"]),
            "angulos": datos["angulos"].copy(),
            "posiciones_detector": datos["posiciones_detector"].copy(),
            "ruido_relativo": float(datos["ruido_relativo"]),
            "desviacion_ruido": float(datos["desviacion_ruido"]),
            "norma_ruido_esperada": float(datos["norma_ruido_esperada"]),
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", type=Path)
    args = parser.parse_args()
    d = cargar_datos_tomografia(args.archivo)
    print(f"n = {d['n']}")
    print(f"A: {d['A'].shape}, nnz={d['A'].nnz:,}")
    print(f"b: {d['b'].shape}")
    print(f"angulos: {d['angulos'].shape}")
    print(f"posiciones de detector: {d['posiciones_detector'].shape}")
    print(f"ruido relativo: {d['ruido_relativo']:.3f}")
    print(f"norma esperada del ruido: {d['norma_ruido_esperada']:.3f}")
