"""
Sistema de Votación Simple
"""

votos = {}
votantes = {}


def ver_resultados():
    """
    Muestra los resultados con conteo y porcentaje por opción,
    ordenados de mayor a menor.
    """
    total = sum(votos.values())

    if total == 0:
        print("📊 Todavía no hay votos registrados.")
        return

    print("📊 Resultados de la votación:")
    ordenados = sorted(votos.items(), key=lambda x: x[1], reverse=True)
    for opcion, cantidad in ordenados:
        porcentaje = (cantidad / total) * 100
        print(f"  - {opcion}: {cantidad} votos ({porcentaje:.1f}%)")
    print(f"  Total de votos: {total}")


def main():
    print("Sistema de votación - módulo base")


if __name__ == "__main__":
    main()