# Autor: Faustina Retamar 46500039
ARCHIVO_USUARIOS = "usuarios.csv"
ARCHIVO_RANKING = "ranking.csv"
FIN_DEL_ARCHIVO_US = ('', '', '', '')
FIN_DEL_ARCHIVO_RK = ('','')

def obtener_palabras_validas():
    """Devuelve una lista de palabras válidas de 5 letras que se pueden usar como objetivo en el juego."""
    return ["abran", "abria", "acojo", "actuo", "aguda", "agudo", "algas", "almas",
            "alojo", "alojo", "altas", "altos", "andes", "anima", "apodo", "arcos", "ardan",
            "ardes", "arios", "azote", "bajas", "bajan", "bardo", "bates", "bayas", "bebas",
            "bebes", "besen", "besos", "botas", "bodas", "bondi", "bonos", "borre", "botan",
            "botes", "bruta", "cagas", "cajas", "callo", "calma", "campo", "canas", "capas",
            "caros", "casan", "casas", "cazan", "cazas", "caida", "caido", "ceder",
            "cenas", "cepas", "ceras", "cerdo", "cerco", "ceros", "cerro", "ciega", "ciego",
            "cines", "clava", "clavo", "calvo", "cogen", "coger", "colas", "coles", "coman",
            "conos", "capas", "capaz", "copos", "copas", "coral", "corra", "corre",
            "cosas", "coses", "croar", "cruje", "cuida", "culta", "culto", "cunas", "curso",
            "dagas", "datos", "debes", "dedos", "densa", "dijes", "doman", "domar", "donan",
            "donas", "dones", "dotes", "dudan", "dunas", "duros", "echas", "echan",
            "edita", "ellos", "emana", "emoji", "enoja", "enojo", "entes", "envio", "erizo",
            "errar", "error", "espia", "euros", "evita", "evito", "falla", "falta", "fetos",
            "filas", "firme", "focos", "fosos", "frias", "fugas", "fumar", "gafas",
            "galas", "galos", "ganas", "gases", "gatos", "genes", "giras", "giros", "goles",
            "gorra", "grave", "grite", "grito", "hielo", "heces", "habia", "hacen", "hacia",
            "hacha", "hecho", "hijas", "hilos", "hojas", "hugos", "ideas", "iglus",
            "islas", "india", "jefes", "jerga", "jodas", "jugos", "jamon", "kenia", "kodak",
            "kayak", "lacra", "libro", "lados", "lagos", "lamen", "larga", "latas", "lazos",
            "lejos", "lenta", "lento", "libre", "linda", "locas", "locos", "lomos",
            "loros", "losas", "luces", "leche", "lucha", "luche", "magos", "malas", "males",
            "malos", "mamas", "manca", "manco", "manos", "manda", "mapas", "marco", "mares",
            "matar", "mayas", "mazos", "mesas", "metas", "metes", "miles", "minas",
            "mirar", "mitos", "modas", "mojar", "modos", "mojan", "moles", "monas", "monos",
            "monte", "moras", "moros", "mozas", "mocos", "mulas", "multa", "muros", "musas",
            "nabos", "nadar", "naves", "nazis", "nubes", "nudos", "nieve", "nunca",
            "nacer", "necio", "necia", "obras", "odiar", "odios", "ollas", "ombus", "ondas",
            "onzas", "opera", "orcas", "orden", "otras", "ovulo", "paces", "pajas", "palas",
            "palma", "palos", "panes", "parda", "parar", "pares", "pases", "patos",
            "pecas", "peces", "penas", "pense", "perdi", "pesas", "pesca", "pesos", "pesas",
            "peces", "pican", "pedir", "pisar", "pleno", "plena", "pocas", "pocos", "podar",
            "poder", "podia", "ponen", "poner", "posee", "pozos", "pijar", "pujan", "pulen",
            "pulir", "pumas", "puros", "quema", "quise", "quito", "queso", "rabia",
            "rabos", "ramos", "ratas", "ratos", "redes", "rejas", "remos", "retos", "reyes",
            "rifas", "rimas", "riman", "rimar", "roban", "rodan", "rojas", "rojos",
            "rosas", "rotar", "rugir", "runas", "rusas", "rusos", "sabia", "serio", "sacar",
            "salgo", "salga", "salta", "salto", "selva", "sanar", "sapos", "sedes", "santa",
            "seria", "serio", "sobar", "sonar", "subir", "suela", "sumar", "super",
            "tacos", "talar", "tejas", "temas", "temen", "temer", "tener", "tenso", "tensa",
            "tiros", "titan", "togas", "tomar", "tonta", "tonto", "torpe", "traje", "trios",
            "urnas", "untar", "umami", "urgar", "vacas", "vagos", "vagas", "vasca",
            "velos", "venas", "vidas", "vigas", "vinos", "volar", "votos", "votar", "video",
            "yates", "yemas", "yenes", "yogur", "zetas", "zonas", "zurda", "zurdo", "zorro"]

def obtener_color(color):
    """Devuelve el código ANSI correspondiente al color indicado para impresión en consola."""
    colores = {
        "Verde": "\x1b[32m",
        "Amarillo": "\x1b[33m",
        "GrisOscuro": "\x1b[90m",
        "Defecto": "\x1b[39m"
    }
    return colores[color]

def abrir_archivo(ruta=ARCHIVO_USUARIOS, modo='r'):
    """Abre el archivo indicado. Si no existe, lo crea vacío. Devuelve el archivo abierto."""
    try:
        archivo = open(ruta, modo)
    except FileNotFoundError:
        archivo = open(ruta, 'x')  # crea archivo vacío
        archivo.close()
        archivo = open(ruta, modo)
    return archivo

def leer_linea(archivo, fin_archivo=FIN_DEL_ARCHIVO_US):
    """Lee una línea del archivo y la separa por comas. Si el archivo terminó, devuelve una constante de fin."""
    linea = archivo.readline()
    if linea == '':
        return fin_archivo
    return linea.rstrip().split(',')

def usuarios_puntajes(archivo):
    """Lee todos los usuarios desde el archivo y devuelve una lista de listas con sus datos."""
    archivo.readline() 
    linea = leer_linea(archivo)
    lista = []
    while linea != FIN_DEL_ARCHIVO_US:
        usuario, clave, nombre, puntos = linea
        lista.append([usuario, clave, nombre, int(puntos)])
        linea = leer_linea(archivo)
    return lista

def cargar_puntajes():
    """Carga el archivo de usuarios, lo procesa y devuelve la lista de usuarios con sus puntajes."""
    archivo = abrir_archivo()
    lista = usuarios_puntajes(archivo)
    archivo.close()
    return lista

def obtener_puntajes(lista, usuario):
    """Busca y devuelve el puntaje actual del usuario indicado. Si no se encuentra, devuelve 0."""
    for u in lista:
        if u[0] == usuario:
            return u[3]
    return 0

def validar_usuario(usuario):
    """
    Verifica que el nombre de usuario tenga entre 5 y 19 caracteres, comience con una letra,
    no empiece ni termine con guion bajo, y solo contenga letras, números o guion bajo.
    Devuelve una tupla (booleano, mensaje).
    """
    valido = True
    mensaje = ""

    if not (4 < len(usuario) < 20):
        valido = False
        mensaje = "EL nombre de usuario debe tener entre 5 y 19 caracteres."

    elif not usuario[0].isalpha():
        valido = False
        mensaje = "El nombre de usuario debe comenzar con una letra."

    elif usuario[0] == "_" or usuario[-1] == "_":
        valido = False
        mensaje = "El nombre de usuario no puede contener un guion bajo al principio o final."

    else:
        i = 0
        while i < len(usuario) and valido:
            if not (usuario[i].isalnum() or usuario[i] == "_"):
                valido = False
                mensaje = "El nombre de usuario solo puede contener letras, números o _."
            i += 1

    return valido, mensaje

def validar_clave(clave):
    """
    Valida que la clave tenga entre 8 y 12 caracteres y cumpla con los requisitos de seguridad:
    debe contener al menos una mayúscula, una minúscula, un número y un símbolo ($, -, *).
    Devuelve una tupla (booleano, mensaje).

    Bajo mi interpretación de la consigna:
    SOLO se permiten caracteres alfanuméricos y los símbolos permitidos ($, -, *).
    Cualquier otro carácter será considerado inválido.
    """
    SIMBOLOS = ["$", "-", "*"]
    valido = True
    mensaje = ""

    if not (8 <= len(clave) <= 12):
        valido = False
        mensaje = "La clave debe tener entre 8 y 12 caracteres."

    else:
        mayus = minus = digito = simbolo = False
        i = 0
        while i < len(clave) and valido:
            c = clave[i]
            if c.isupper():
                mayus = True
            elif c.islower():
                minus = True
            elif c.isdigit():
                digito = True
            elif c in SIMBOLOS:
                simbolo = True
            else:
                valido = False
                mensaje = "La clave solo admite letras, números y símbolos ($ - *)."
            i += 1

        if valido and not (mayus and minus and digito and simbolo):
            valido = False
            mensaje = "La clave debe tener mayúscula, minúscula, número y símbolo ($ - *)."

    return valido, mensaje

def usuario_existente(usuario, lista):
    """Verifica si un nombre de usuario ya existe dentro de la lista de usuarios."""
    existe = False
    i=0
    while not existe and i<len(lista):
        if lista[i][0] == usuario:
            existe = True
        i+=1
    return existe

def guardar_usuario(usuario, clave, nombre, lista):
    """Agrega un nuevo usuario a la lista y reescribe el archivo de usuarios con la lista actualizada."""
    lista.append([usuario, clave, nombre, 0])
    archivo = abrir_archivo(modo='w')
    archivo.write("usuario,clave,nombre,puntos\n")
    for u in lista:
        archivo.write(f"{u[0]},{u[1]},{u[2]},{u[3]}\n")
    archivo.close()
    return lista

def actualizar_ranking(lista):
    """Agrega puntajes de los jugadores al archivo de ranking."""
    archivo = abrir_archivo(ARCHIVO_RANKING, modo='w') 
    for usuario in lista:
        archivo.write(f"{usuario[0]},{usuario[3]}\n")
    archivo.close()

def mostrar_ranking(lista):
    """Muestra en consola el Top 5 de usuarios con más puntaje acumulado."""
    ranking = {}
    for us in lista:
        ranking[us[0]] = int(us[3])  

    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("\n🏆 Top 5 Puntajes:")
    i = 0
    while i < 5 and i < len(ranking_ordenado):
        usuario, puntos = ranking_ordenado[i]
        print(f"{i+1}. {usuario} - {puntos} pts")
        i += 1

def actualizar_archivo_usuarios(usuario, nuevos_puntos, lista):
    """Actualiza el puntaje del usuario en la lista y reescribe el archivo de usuarios con los nuevos valores."""
    i = 0
    actualizado = False
    while  not actualizado:
        if lista[i][0] == usuario:
            lista[i][3] = nuevos_puntos
            actualizado = True
        i += 1

    archivo = abrir_archivo(modo='w')
    archivo.write("usuario,clave,nombre,puntos\n")
    for u in lista:
        archivo.write(f"{u[0]},{u[1]},{u[2]},{u[3]}\n")
    archivo.close()
    return lista
