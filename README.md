![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Script de procesamiento de datos

## Objetivo

Construir un script Python que lea datos de un archivo JSON, los procese y genere un informe.

## Contexto

Tienes un archivo con registros de ventas de una tienda online. Tu script debe leerlo, analizarlo y mostrar un resumen.

## Paso 1: Preparar el entorno

```bash
mkdir lab-python-d1
cd lab-python-d1
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Crea el archivo `ventas.json`:

```json
[
  { "id": 1, "producto": "Laptop", "precio": 899.99, "cantidad": 2, "categoria": "electronica", "fecha": "2026-01-15" },
  { "id": 2, "producto": "Teclado", "precio": 49.99, "cantidad": 5, "categoria": "electronica", "fecha": "2026-01-16" },
  { "id": 3, "producto": "Silla", "precio": 299.99, "cantidad": 1, "categoria": "muebles", "fecha": "2026-01-16" },
  { "id": 4, "producto": "Monitor", "precio": 349.99, "cantidad": 3, "categoria": "electronica", "fecha": "2026-01-17" },
  { "id": 5, "producto": "Libro Python", "precio": 29.99, "cantidad": 10, "categoria": "libros", "fecha": "2026-01-18" },
  { "id": 6, "producto": "Escritorio", "precio": 499.99, "cantidad": 1, "categoria": "muebles", "fecha": "2026-01-18" },
  { "id": 7, "producto": "Auriculares", "precio": 79.99, "cantidad": 4, "categoria": "electronica", "fecha": "2026-01-19" }
]
```

## Paso 2: Leer y procesar los datos

Crea `analisis.py` con las siguientes funciones:

```python
import json
from datetime import datetime

def cargar_ventas(ruta_archivo):
    """Lee el archivo JSON y devuelve la lista de ventas."""
    pass

def calcular_total_venta(venta):
    """Devuelve precio * cantidad para una venta."""
    pass

def ventas_por_categoria(ventas):
    """
    Agrupa las ventas por categoría.
    Devuelve un dict: { "categoria": total_euros }
    """
    pass

def producto_mas_vendido(ventas):
    """Devuelve el nombre del producto con mayor ingreso total."""
    pass

def ventas_en_fecha(ventas, fecha_str):
    """Filtra ventas de una fecha específica (formato YYYY-MM-DD)."""
    pass
```

## Paso 3: Generar el informe

Implementa `main()` que imprima:

```
============================
   INFORME DE VENTAS
============================

Total de ventas: 7
Ingresos totales: 3.089,87 €

--- Por categoría ---
electronica: 2.599,87 €
muebles:       799,98 €
libros:        299,90 €

Producto más rentable: Laptop (1.799,98 €)

--- Ventas del 16/01/2026 ---
- Teclado: 249,95 €
- Silla: 299,99 €
```

## Paso 4: Exportar resultados

Añade una función `guardar_informe(informe, ruta)` que guarde el informe en `informe.json`:

```json
{
  "generado_en": "2026-05-11T09:30:00",
  "total_ventas": 7,
  "ingresos_totales": 3089.87,
  "por_categoria": {
    "electronica": 2599.87,
    "muebles": 799.98,
    "libros": 299.90
  },
  "producto_top": "Laptop"
}
```