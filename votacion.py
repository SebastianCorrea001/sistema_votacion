"""
Sistema de Votación Simple
"""

import json
from datetime import datetime

votos = {}
votantes = {}

ARCHIVO_HISTORIAL = "historial_votaciones.json"


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


def mostrar_ganador():
    if not votos:
        print("🏆 Todavía no hay votos para determinar un ganador.")
        return
    max_votos = max(votos.values())
    ganadores = [opcion for opcion, cantidad in votos.items() if cantidad == max_votos]
    if len(ganadores) == 1:
        print(f"🏆 Va ganando: {ganadores[0]} con {max_votos} votos.")
    else:
        empate = ", ".join(ganadores)
        print(f"🏆 Hay un empate entre: {empate} (con {max_votos} votos cada uno).")


def reiniciar_votacion():
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
    registrar_voto("cedula1", "Candidato A")
    registrar_voto("cedula2", "Candidato B")
    registrar_voto("cedula3", "Candidato A")
    registrar_voto("cedula1", "Candidato B")  # debe salir rechazado

    ver_resultados()
    mostrar_ganador()
    reiniciar_votacion()
    ver_resultados()  # debería salir vacío, confirma que se reinició


if __name__ == "__main__":
    main()