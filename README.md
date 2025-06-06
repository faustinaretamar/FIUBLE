# 🎮 FIUBLE

FIUBLE es un juego de palabras tipo Wordle, desarrollado en Python como trabajo práctico para la materia **Fundamentos de la Programación** de la FIUBA.

---

## 📌 Descripción general

El objetivo del juego es adivinar una palabra de 5 letras en un máximo de 5 intentos. Hay dos modos de juego disponibles:

- 👤 **Modo un jugador**: con login, registro y sistema de puntajes persistente.
- 👥 **Modo dos jugadores**: por consola, alternando turnos y con sistema competitivo de puntaje.

Además, se utiliza **interfaz gráfica con Tkinter** para el registro e inicio de sesión en el modo un jugador.

---

## 📁 Estructura de archivos

- `fiuble.py`: lógica principal del juego (consola).
- `interfaz.py`: interfaz gráfica para un jugador (Tkinter).
- `utiles.py`: funciones auxiliares (manejo de archivos, validaciones, colores).
- `usuarios.csv`: base de datos de usuarios registrados.
- `ranking.csv`: ranking de puntajes totales.
