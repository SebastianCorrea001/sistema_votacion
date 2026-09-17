"""
Sistema de Votación Simple
"""

votos = {}
votantes = {}


def registrar_voto(id_persona, opcion):
    if id_persona in votantes:
        print(f"⚠️  {id_persona} ya votó por '{votantes[id_persona]}'. Voto rechazado.")
        return False
    votantes[id_persona] = opcion
    votos[opcion] = votos.get(opcion, 0) + 1
    print(f"✅ Voto registrado: {id_persona} -> {opcion}")
    return True


def ver_resultados():
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