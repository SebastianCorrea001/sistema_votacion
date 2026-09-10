"""
Sistema de Votación Simple
"""

votos = {}          # {opcion: cantidad_de_votos}
votantes = {}        # {id_persona: opcion_votada} -> evita doble voto


def registrar_voto(id_persona, opcion):
    """
    Registra el voto de una persona para una opción dada.
    Evita que la misma persona vote dos veces.
    """
    if id_persona in votantes:
        print(f"⚠️  {id_persona} ya votó por '{votantes[id_persona]}'. Voto rechazado.")
        return False

    votantes[id_persona] = opcion
    votos[opcion] = votos.get(opcion, 0) + 1
    print(f"✅ Voto registrado: {id_persona} -> {opcion}")
    return True


def main():
    print("Sistema de votación - módulo base")


if __name__ == "__main__":
    main()