# FIUBLE
# Autor: Faustina Retamar 46500039
import time 
import random
from utiles import obtener_palabras_validas, obtener_color, obtener_puntajes, cargar_puntajes,mostrar_ranking, actualizar_archivo_usuarios, actualizar_ranking

def validacion(palabra_objetivo:str, arriesgo:str): 
    """Valida que el arriesgo tenga la misma longitud que la palabra objetivo
    y que solo contenga letras (sin números ni símbolos).
    Retorna un booleano, que indica si el ingreso a sido valido o no.
    """
    validacion = True
    if len(palabra_objetivo) != len(arriesgo):
        validacion = False
        print('El arriesgo debe ser de 5 letras')
    i=0
    alpha = True
    while alpha and i<len(arriesgo):
        if not arriesgo[i].isalpha():
            validacion = alpha = False
            print('No puede contener numeros ni caracteres especiales, solo letras')
        i += 1
    return validacion

def procesar_palabra(arriesgo:str):
    """Convierte acentos a vocales simples y transforma la palabra a mayúsculas.
    Devuelve la palabra procesada.
    """
    VOCALES = ['A','E','I','O','U']
    ACENTOS = ['Á','É','Í','Ó','Ú']
    arriesgo = arriesgo.upper()
    arriesgo_procesado =''
    for l in arriesgo:
        if l in ACENTOS:
            arriesgo_procesado += VOCALES[ACENTOS.index(l)]
        else:
            arriesgo_procesado += l
    return arriesgo_procesado

def mostrar_resultado(palabra_objetivo, arriesgo):
    """Muestra en consola cada letra del arriesgo con colores:
    Verde si está en la posición correcta, amarillo si está mal ubicada,
    y gris si no pertenece a la palabra.
    """
    resultado = ""
    for i in range(5):
        letra = arriesgo[i]
        if letra == palabra_objetivo[i]:
            resultado += obtener_color("Verde") + letra + " "
        elif letra in palabra_objetivo:
            resultado += obtener_color("Amarillo") + letra + " "
        else:
            resultado += obtener_color("GrisOscuro") + letra + " "
    resultado += obtener_color("Defecto")  # Reset color
    print(resultado)

def mostrar_tablero(intentos, palabra_objetivo, arriesgos=[]):
    """Muestra la palabra parcialmente descubierta y los intentos realizados
    hasta el momento. Completa con '?' los intentos restantes.
    """

    if arriesgos:
        mostrar_letras_acertadas(palabra_objetivo, arriesgos)
        for i in range(intentos):
            if i < len(arriesgos):
                mostrar_resultado(palabra_objetivo, arriesgos[i])
            else:
                print('? ? ? ? ?')
    else:
        print("Palabra a adivinar: ? ? ? ? ?")
        for _ in range(intentos):
            print('? ? ? ? ?')

def mostrar_letras_acertadas(palabra_objetivo, arriesgos):
    """Muestra las letras que fueron adivinadas correctamente
en su posición, y '?' en las que aún no.
"""

    descubiertas = ["?"] * 5 

    for arriesgo in arriesgos:
        for i in range(5):
            if arriesgo[i] == palabra_objetivo[i]:
                descubiertas[i] = palabra_objetivo[i]  # Revelar letra correcta

    print("Palabra a adivinar:", " ".join(descubiertas))

def calcular_puntaje(intento):
    """Devuelve el puntaje correspondiente según la cantidad de intentos
    usados para adivinar la palabra. Si no se adivina, devuelve -100.
    """
    puntajes = [50,40,30,20,10]
    if intento == 5:
        puntaje = -100
    else: 
        puntaje = puntajes[intento]
    return puntaje
    
def mostrar_duracion(inicio, jugador=''):
    """Muestra el tiempo total que tardó el jugador en adivinar la palabra,
    expresado en minutos y segundos.
    """
    fin = time.time()
    duracion = int(fin - inicio)
    minutos = duracion // 60
    segundos = duracion % 60
    if jugador:
        print(f"\n🎉 ¡{jugador} adivinó! Tardaron {minutos}m {segundos}s en total.")
    else:
        print(f"\n🎉 ¡Ganaste! Tardaste {minutos} minutos y {segundos} segundos en adivinar la palabra.")

def seguir_jugando():
    """Pregunta al usuario si desea jugar otra partida.
    Devuelve True si responde 'S' y False si responde 'N'.
    """
    print()
    res = input('Desea jugar otra partida? (S/N) ')
    a = ['S', 'N', 's', 'n']
    while res not in a:
        res = input('Desea jugar otra partida? (S/N) ')
    if res == 'S' or res == 's':
        juega = True
    elif res == 'N' or res == 'n':
        juega = False 
    return juega

def modo_un_jugador(jugador):
    """Ejecuta el juego en modo un jugador. 
    Administra las partidas, suma puntajes, actualiza los archivos 
    y muestra el ranking final.
    """
    list_puntajes = cargar_puntajes()
    puntos_acumulados = obtener_puntajes(list_puntajes, jugador)

    juega = True
    while juega:
        puntos_ronda = jugar_un_jugador(random.choice(obtener_palabras_validas()).upper(), jugador, puntos_acumulados)
        puntos_acumulados += puntos_ronda
        juega = seguir_jugando()

    nueva_lista = actualizar_archivo_usuarios(jugador, puntos_acumulados, list_puntajes)
    actualizar_ranking(nueva_lista)
    mostrar_ranking(nueva_lista)

def jugar_un_jugador(palabra_objetivo, jugador, puntaje):
    """Ejecuta una ronda del juego en modo un jugador.
    Procesa los arriesgos, muestra resultados y retorna el puntaje de la partida.
    """
    intentos_totales = 5
    arriesgos = []
    adivino = False
    inicio = time.time()
    puntos_acumulados = 0
    mostrar_tablero(intentos_totales, palabra_objetivo)
    intento = 0

    while not adivino and intento < 5:
        valido = False
        while not valido:
            arriesgo = input("Arriesgo: ")
            valido = validacion(palabra_objetivo, arriesgo)
        arriesgo = procesar_palabra(arriesgo)
        arriesgos.append(arriesgo)
        if arriesgo == palabra_objetivo:
            adivino = True
        else: 
            mostrar_tablero(intentos_totales, palabra_objetivo, arriesgos)
            intento += 1

    p = calcular_puntaje(intento)
    print('La palabra era: ' + palabra_objetivo)
    puntos_acumulados += p
    if p > 0:
        mostrar_duracion(inicio)
        print(f"{jugador} ganaste {p} puntos, ahora tenés {puntaje + puntos_acumulados}")
    else:
        print("💀 No adivinaste la palabra.")
        print(f"{jugador} perdiste {abs(p)} puntos, ahora tenés {puntaje + puntos_acumulados}")

    return puntos_acumulados
  
def modo_dos_jugadores(jugador1, jugador2):
    """Controla el flujo general del modo dos jugadores.
    Llama a las rondas, gestiona turnos y muestra resultados finales.
    """

    puntajes = {jugador1: 0, jugador2: 0}
    turno_actual = random.choice([jugador1,jugador2])
    juega = True

    while juega:
        palabra = random.choice(obtener_palabras_validas()).upper()
        puntajes = jugar_dos_jugadores(palabra, jugador1, jugador2, turno_actual, puntajes)

        if turno_actual == jugador2:
            turno_actual = jugador1
        else :
            turno_actual = jugador2

        juega = seguir_jugando()

    # Fin del juego
    print("\n🏁 Juego terminado.")
    print(f"{jugador1} terminó con {puntajes[jugador1]} puntos.")
    print(f"{jugador2} terminó con {puntajes[jugador2]} puntos.")

    if puntajes[jugador1] > puntajes[jugador2]:
        print(f"👑 ¡El ganador es {jugador1}!")
    elif puntajes[jugador2] > puntajes[jugador1]:
        print(f"👑 ¡El ganador es {jugador2}!")
    else:
        print("🤝 ¡Empate!")

def jugar_dos_jugadores(palabra_objetivo, jugador1, jugador2, turno_actual, puntajes):
    """Ejecuta una ronda del juego en modo dos jugadores.
    Alterna los turnos, calcula los puntajes y actualiza el estado de juego.
    Devuelve los puntajes acumulados de cada jugadoor despues de cada ronda
    """
    intentos_totales = 5
    arriesgos = []
    adivino = False
    inicio = time.time()
    jugador_turno = turno_actual
    jugador_que_adivino = None 

    mostrar_tablero(intentos_totales, palabra_objetivo)
    intento = 0

    while not adivino and intento < 5:
        valido = False
        print(f"\nTurno de {jugador_turno}:")
        while not valido:
            arriesgo = input("Arriesgo: ")
            valido = validacion(palabra_objetivo, arriesgo)
        arriesgo = procesar_palabra(arriesgo)
        arriesgos.append(arriesgo)

        if arriesgo == palabra_objetivo:
            adivino = True
            jugador_que_adivino = jugador_turno  # guarda quién acertó
        else:
            mostrar_tablero(intentos_totales, palabra_objetivo, arriesgos)
            # solo cambiamos de turno si no adivinó
            jugador_turno = jugador2 if jugador_turno == jugador1 else jugador1
            intento += 1

    p = calcular_puntaje(intento)
    print('La palabra era: ' + palabra_objetivo)

    if jugador_que_adivino == jugador1:
        otro_jugador = jugador2
    else:
        otro_jugador = jugador1

    if adivino:
        mostrar_duracion(inicio, jugador_que_adivino)

        perdedor = otro_jugador

        puntajes[jugador_que_adivino] += p
        puntajes[perdedor] -= p

        print(f"{jugador_que_adivino} ganó {p} puntos, ahora tiene {puntajes[jugador_que_adivino]}")
        print(f"{perdedor} perdió {p} puntos, ahora tiene {puntajes[perdedor]}")

    else:
        print("💀 No adivinaron la palabra.")
        if turno_actual == jugador1:
            otro_jugador = jugador2
        else:
            otro_jugador = jugador1
        puntajes[turno_actual] -= 100
        puntajes[otro_jugador] -= 50
        print(f"{turno_actual} perdió 100 puntos, ahora tiene {puntajes[turno_actual]}")
        print(f"{otro_jugador} perdió 50 puntos, ahora tiene {puntajes[otro_jugador]}")
    return puntajes