# 🎮 FIUBLE

**FIUBLE** es un juego de palabras al estilo **Wordle**, desarrollado en **Python** como trabajo práctico para la materia **Fundamentos de la Programación** de la **FIUBA**.

📺 Miralo en acción:  
[🔗 Video 1](https://youtu.be/c3yDt6w8TB4?si=E-idKKnSYr5bfyZJ) | [🔗 Video 2](https://youtu.be/2qBkduC_MuM)

---

## 📌 Descripción general

El objetivo del juego es adivinar una palabra de **5 letras** en un máximo de **5 intentos**.

### Modos de juego:

- 👤 **Un jugador**  
  - Registro e inicio de sesión con interfaz gráfica (Tkinter)  
  - Sistema de puntajes persistente  

- 👥 **Dos jugadores**  
  - Juego por consola  
  - Turnos alternados  
  - Competencia directa por puntaje  

---

## 🛠️ Tecnologías utilizadas

- 🐍 Python (3.x)
- 🖼️ Tkinter (interfaz gráfica)
- 📁 CSV (almacenamiento de usuarios y rankings)

---

## 📁 Estructura del proyecto

| Archivo         | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `fiuble.py`     | Lógica principal del juego en consola (modo un jugador y dos jugadores).   |
| `interfaz.py`   | Interfaz gráfica (Tkinter) para el modo un jugador.                        |
| `utiles.py`     | Funciones auxiliares (manejo de archivos, validaciones, colores, etc.).    |
| `usuarios.csv`  | Base de datos de usuarios registrados.                                     |
| `ranking.csv`   | Tabla de ranking con puntajes acumulados.                                  |

---

## 🚀 Cómo jugar

1. Cloná el repositorio.
2. Ejecutá `fiuble.py` para jugar por consola, o `interfaz.py` para usar la interfaz gráfica.
3. ¡Adiviná la palabra y sumá puntos!

---
