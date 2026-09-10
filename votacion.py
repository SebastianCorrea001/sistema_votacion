"""
Sistema de Votación Simple
"""

import json
from datetime import datetime

votos = {}
votantes = {}

ARCHIVO_HISTORIAL = "historial_votaciones.json"


def reiniciar_votacion():
    """
    Guarda el estado actual en un historial (JSON) y reinicia la votación.
    """
    registro = {
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "votos": votos.copy(),
        "total_votantes": len(votantes),
    }

    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as f:
            historial = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    historial.append(registro)

    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)

    votos.clear()
    votantes.clear()
    print("🔄 Votación reiniciada. Historial guardado en", ARCHIVO_HISTORIAL)


def main():
    print("Sistema de votación - módulo base")


if __name__ == "__main__":
    main()