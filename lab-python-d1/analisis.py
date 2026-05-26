import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent


def cargar_ventas(ruta_archivo):
    """Lee el archivo JSON y devuelve la lista de ventas."""
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return json.load(f)


def calcular_total_venta(venta):
    """Devuelve precio * cantidad para una venta."""
    return venta["precio"] * venta["cantidad"]


def ventas_por_categoria(ventas):
    """
    Agrupa las ventas por categoría.
    Devuelve un dict: { "categoria": total_euros }
    """
    totales = {}
    for venta in ventas:
        categoria = venta["categoria"]
        total = calcular_total_venta(venta)
        totales[categoria] = totales.get(categoria, 0) + total
    return totales


def producto_mas_vendido(ventas):
    """Devuelve el nombre del producto con mayor ingreso total."""
    return max(ventas, key=calcular_total_venta)["producto"]


def ventas_en_fecha(ventas, fecha_str):
    """Filtra ventas de una fecha específica (formato YYYY-MM-DD)."""
    return [v for v in ventas if v["fecha"] == fecha_str]


def guardar_informe(informe, ruta):
    """Guarda el informe como JSON en la ruta indicada."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(informe, f, ensure_ascii=False, indent=2)


def main():
    ventas = cargar_ventas("ventas.json")

    ingresos_totales = sum(calcular_total_venta(v) for v in ventas)
    por_categoria = ventas_por_categoria(ventas)
    top_producto = producto_mas_vendido(ventas)
    top_total = calcular_total_venta(next(v for v in ventas if v["producto"] == top_producto))
    ventas_16 = ventas_en_fecha(ventas, "2026-01-16")

    print("============================")
    print("   INFORME DE VENTAS")
    print("============================")
    print()
    print(f"Total de ventas: {len(ventas)}")
    print(f"Ingresos totales: {ingresos_totales:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
    print()
    print("--- Por categoría ---")
    for categoria, total in por_categoria.items():
        total_fmt = f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{categoria}: {total_fmt}")
    print()
    top_fmt = f"{top_total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"Producto más rentable: {top_producto} ({top_fmt})")
    print()
    print("--- Ventas del 16/01/2026 ---")
    for v in ventas_16:
        total_fmt = f"{calcular_total_venta(v):,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"- {v['producto']}: {total_fmt}")

    informe = {
        "generado_en": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "total_ventas": len(ventas),
        "ingresos_totales": round(ingresos_totales, 2),
        "por_categoria": {k: round(v, 2) for k, v in por_categoria.items()},
        "producto_top": top_producto,
    }
    guardar_informe(informe, "informe.json")


if __name__ == "__main__":
    main()
