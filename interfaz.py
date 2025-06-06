# Autor: Faustina Retamar 46500039
from tkinter import *
from tkinter import messagebox
from fiuble import  modo_dos_jugadores, modo_un_jugador
from utiles import validar_usuario, validar_clave, usuario_existente, guardar_usuario, cargar_puntajes

def registrar_interfaz(ventana_padre):
    ventana_registro = Toplevel(ventana_padre)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")

    Label(ventana_registro, text="Nombre completo").pack()
    entrada_nombre = Entry(ventana_registro)
    entrada_nombre.pack()

    Label(ventana_registro, text="Nombre de usuario").pack()
    entrada_usuario = Entry(ventana_registro)
    entrada_usuario.pack()

    Label(ventana_registro, text="Contraseña").pack()
    entrada_clave = Entry(ventana_registro, show="*")
    entrada_clave.pack()

    def confirmar_registro():
        """
        Valida los datos del formulario de registro. Si todo es correcto, guarda el nuevo usuario
        y muestra un mensaje de éxito. Si hay errores, los informa sin cortar el flujo con return.
        """
        nombre = entrada_nombre.get()
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        lista = cargar_puntajes()

        error = False

        valido, msg = validar_usuario(usuario)
        if not valido:
            messagebox.showerror("Error", msg, parent=ventana_registro)
            error = True

        if not error and usuario_existente(usuario, lista):
            messagebox.showerror("Error", "El usuario ya existe.", parent=ventana_registro)
            error = True

        if not error:
            valido, msg = validar_clave(clave)
            if not valido:
                messagebox.showerror("Error", msg, parent=ventana_registro)
                error = True

        if not error:
            guardar_usuario(usuario, clave, nombre, lista)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.", parent=ventana_registro)
            ventana_registro.destroy()

    Button(ventana_registro, text="Confirmar", command=confirmar_registro).pack(pady=10)

def login_interfaz(ventana_padre):
    ventana_login = Toplevel(ventana_padre)
    ventana_login.title("Iniciar sesión")
    ventana_login.geometry("300x200")

    Label(ventana_login, text="Usuario").pack()
    entrada_usuario = Entry(ventana_login)
    entrada_usuario.pack()

    Label(ventana_login, text="Contraseña").pack()
    entrada_clave = Entry(ventana_login, show="*")
    entrada_clave.pack()

    def confirmar_login():
        """
        Verifica si el usuario y la contraseña ingresados coinciden con un usuario registrado.
        Si es correcto, cierra las ventanas y entra al modo un jugador. Si no, muestra un error.
        """
        confirmado = False
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        lista = cargar_puntajes()
        i = 0

        while i < len(lista) and not confirmado:
            if lista[i][0] == usuario and lista[i][1] == clave:
                messagebox.showinfo("Bienvenido", f"Hola {lista[i][2]}!", parent=ventana_login)
                confirmado = True
                ventana_login.destroy()
                ventana_padre.destroy()
                modo_un_jugador(usuario)
            i += 1

        if not confirmado:
            messagebox.showerror("Error", "Usuario o clave incorrectos.", parent=ventana_login)

    Button(ventana_login, text="Entrar", command=confirmar_login).pack(pady=10)

def iniciar_interfaz_modo_un_jugador():
    ventana = Tk()
    ventana.title("FIUBLE - Un Jugador")
    ventana.geometry("300x200")

    Label(ventana, text="Modo Un Jugador", font=("Arial", 14)).pack(pady=10)
    Button(ventana, text="Registrarse", width=20, command=lambda: registrar_interfaz(ventana)).pack(pady=5)
    Button(ventana, text="Iniciar sesión", width=20, command=lambda: login_interfaz(ventana)).pack(pady=5)

    ventana.mainloop()

def iniciar_modo_dos_jugadores():
    print("Modo 2 jugadores (consola)")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")
    modo_dos_jugadores(jugador1, jugador2)

def seleccionar_modo():
    ventana = Tk()
    ventana.title("FIUBLE - Modo de Juego")
    ventana.geometry("300x150")

    Label(ventana, text="¿Cómo querés jugar?", font=("Arial", 14)).pack(pady=10)
    Button(ventana, text="Un Jugador", width=25, command=lambda: [ventana.destroy(), iniciar_interfaz_modo_un_jugador()]).pack(pady=5)
    Button(ventana, text="Dos Jugadores", width=25, command=lambda: [ventana.destroy(), iniciar_modo_dos_jugadores()]).pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    seleccionar_modo()
