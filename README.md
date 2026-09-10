# 🗳️ Sistema de Votación Simple

Proyecto académico enfocado en la práctica de **ramas (branches)** y **versionado con Git**, simulando el trabajo colaborativo de un equipo de 3 integrantes, donde cada uno desarrolla una función independiente del sistema.

---

## 📌 Descripción general

Este proyecto implementa un sistema de votación básico en Python, dividido en tres funcionalidades principales. Cada función fue desarrollada en su propia rama, con commits siguiendo el estándar de **Conventional Commits**, y marcada con un **tag personal** al finalizar.

El objetivo es practicar el flujo de trabajo típico de control de versiones: creación de ramas, commits atómicos y bien descritos, etiquetado de versiones y publicación remota del trabajo.

---

## 👥 Integrantes y ramas de trabajo

| Integrante | Rama | Función desarrollada | Tag |
|---|---|---|---|
| Integrante 1 | `feature/registrar-voto` | `registrar_voto()` | `v0.1-registro` |
| Integrante 2 | `feature/ver-resultados` | `ver_resultados()` | `v0.1-resultados` |
| Integrante 3 | `feature/reiniciar-votacion` | `reiniciar_votacion()` | `v0.1-reinicio` |

---

## ⚙️ Funcionalidades

### 1️⃣ `registrar_voto(id_persona, opcion)`
Registra el voto de una persona para una opción específica.

- Usa un diccionario `votantes = {}` para llevar el control de quién ya votó (`{id_persona: opcion_votada}`).
- Antes de registrar un voto, valida si la persona ya está en el diccionario.
- Si la persona **ya votó**, el voto es rechazado y se muestra una advertencia.
- Si es su primer voto, se registra correctamente y se contabiliza en el diccionario `votos = {}`.

```python
registrar_voto("cedula123", "Candidato A")   # ✅ Voto registrado
registrar_voto("cedula123", "Candidato B")   # ⚠️ Rechazado (doble voto)
```

### 2️⃣ `ver_resultados()`
Muestra los resultados de la votación en pantalla.

- Calcula el **total de votos** emitidos.
- Muestra, para cada opción, la cantidad de votos **y el porcentaje** que representa sobre el total.
- Los resultados se muestran ordenados de mayor a menor cantidad de votos.

```
📊 Resultados de la votación:
  - Candidato A: 2 votos (66.7%)
  - Candidato B: 1 votos (33.3%)
  Total de votos: 3
```

### 3️⃣ `reiniciar_votacion()`
Reinicia la votación, sin perder el registro histórico.

- Antes de limpiar los datos, guarda un resumen del estado actual (fecha, conteo de votos y total de votantes) en un archivo `historial_votaciones.json`.
- Si el archivo ya existe, agrega el nuevo registro a la lista en lugar de sobrescribirlo.
- Limpia los diccionarios `votos` y `votantes` para dejar el sistema listo para una nueva votación.

---

## 🌳 Flujo de trabajo con Git

Cada integrante siguió este flujo desde la rama `main`:

```bash
git checkout main
git pull
git checkout -b feature/nombre-de-la-funcion

# ... desarrollo y commits con conventional commits ...

git tag -a v0.1-tag-personal -m "descripción del tag"
git push -u origin feature/nombre-de-la-funcion --tags
```

### Ejemplos de commits (Conventional Commits)

```
feat: agregar registrar_voto con validación de doble voto
test: agregar script de prueba para registrar_voto
feat: agregar ver_resultados con cálculo de porcentajes
refactor: ordenar resultados de mayor a menor votación
feat: agregar reiniciar_votacion con guardado de historial en JSON
chore: agregar .gitignore
```

---

## 🗂️ Estructura del repositorio

```
sistema-votacion/
├── votacion.py                  # Módulo principal con las funciones
├── historial_votaciones.json    # Historial generado al reiniciar (se crea en tiempo de ejecución)
├── .gitignore
└── README.md
```

---

## 🚀 Próximos pasos

> Esta actividad continúa en la próxima sesión.

Pendiente para la siguiente etapa:
- Fusionar (`merge`) las tres ramas en `main`.
- Integrar las tres funciones en un solo `votacion.py` funcional.
- Resolver posibles conflictos de fusión.
- Crear una nueva versión (tag) del sistema ya integrado.

---

## 🖥️ Cómo ejecutar el proyecto

```bash
git clone <url-del-repositorio>
cd sistema-votacion
python3 votacion.py
```

---

## 🏷️ Historial de tags

| Tag | Descripción |
|---|---|
| `v0.1-registro` | Función `registrar_voto` lista y probada |
| `v0.1-resultados` | Función `ver_resultados` lista con porcentajes |
| `v0.1-reinicio` | Función `reiniciar_votacion` lista con historial persistente |