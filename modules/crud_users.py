import modules.core as cr
import modules.utils as ut
import modules.messages as ms
from tabulate import tabulate

def iniciar_sesion(usuarios):
    ut.borrar_pantalla()
    
    while True:
        ut.borrar_pantalla()
        print("Inicio de sesion - ACME Solutions")

        email = input("Ingrese el e-mail corporativo: ").lower()
        clave = input("Ingrese la clave: ")

        acceso = False

        for usuario in usuarios:

            if (usuario["email"].lower() == email and usuario["clave"] == clave):

                print("Acceso concedido")
                acceso = True
                return usuario
                
        if not acceso:
            print("Credenciales incorrectas.")
            ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def registrar_usuario(usuarios):

    def pedir_texto(mensaje):
        while True:
            dato = input(mensaje).strip()

            if dato == "":
                print("Este campo es obligatorio.")
            else:
                return dato.lower()

    def pedir_numero(mensaje):
        while True:
            dato = input(mensaje).strip()

            if dato == "":
                print("Este campo es obligatorio.")
                continue

            if dato.isdigit():
                return int(dato)

            print("Debe ingresar solo números.")

    ut.borrar_pantalla()
    print("Registrar usuario al sistema")

    n_identificacion = pedir_numero("Ingrese el numero de identificacion: ")
    nombres = pedir_texto("Ingrese los nombres: ")
    apellidos = pedir_texto("Ingrese los apellidos: ")
    telefono = pedir_numero("Ingrese el numero de teléfono: ")
    email = pedir_texto("Ingrese el e-mail corporativo: ")
    direccion = pedir_texto("Ingrese la direccion: ")
    while True:
        rol = pedir_texto("Ingrese el rol (admin / operario): ")

        if rol in ["admin", "operario"]:
            break

        print("Rol inválido. Debe ser admin u operario.")

    clave = pedir_texto("Ingrese la clave: ")

    usuario = {
        "ID": n_identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "rol": rol,
        "clave": clave
    }

    usuarios["usuarios"].append(usuario)

    cr.AddData(usuarios)

    print("\nUsuario agregado exitosamente.")

    ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def listar_usuarios(usuarios):
    ut.borrar_pantalla()
    print("Lista de usuarios")

    if not usuarios:
        print("No hay usuarios registrados")
        ut.pausar_pantalla
        return

    tabla = []

    for usuario in usuarios:
        nombre_completo = f"{usuario.get('nombres', '')} {usuario.get('apellidos', '')}"

        tabla.append([
            usuario.get("ID"),
            nombre_completo,
            usuario.get("telefono"),
            usuario.get("email"),
            usuario.get("rol")
        ])

    print(tabulate(tabla, headers = ['ID', 'Nombre completo', 'Telefono', 'E-mail', 'Rol']))
    
    ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def actualizar_usuario(usuarios):
    ut.borrar_pantalla()
    print("Actualizar usuario")

    n_identificacion = int(input("Ingrese el ID del usuario a actualizar: "))

    encontrado = False

    for usuario in usuarios["usuarios"]:

        if usuario["ID"] == n_identificacion:

            encontrado = True
            
            new_nombre = input(f"Nombres ({usuario['nombre']}): ").lower()
            new_apellido = input(f"Apellidos ({usuario['apellido']}): ").lower()
            new_telefono = int(input(f"Telefono ({usuario['telefono']}): "))
            new_email = input(f"E-mail ({usuario['email']}) ").lower()
            new_direccion = input(f"Direccion ({usuario['direccion']}): ").lower()
            new_rol = input(f"Rol ({usuario['rol']}): ").lower()
            new_clave = input(f"Clave ({usuario['clave']}): ").lower()
        
            usuario.update({
                "nombre": new_nombre,
                "apellido": new_apellido,
                "telefono": new_telefono,
                "email": new_email,
                "direccion": new_direccion,
                "rol": new_rol,
                "clave": new_clave
            })

            cr.AddData(usuarios)

            print("Usuario actualizado exitosamente.")
            ut.pausar_pantalla()

            break

    if not encontrado:
        print("ID no encontrado")
        ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def eliminar_usuario(usuarios):
    ut.borrar_pantalla()
    print("Eliminar usuario")

    n_identificacion = int(input("Ingrese el ID del usuario a eliminar: "))

    encontrado = False

    for usuario in usuarios["usuarios"]:

        if usuario["ID"] == n_identificacion:

            encontrado = True

            confirmacion = input(f"Desea eliminar a {usuario['nombres']} {usuario['apellidos']}? (S/N): ").lower()

            if confirmacion == "s":

                usuarios["usuarios"].remove(usuario)

                print("Usuario eliminado")

                cr.AddData(usuarios)
                ut.pausar_pantalla()
            else:
                print("Eliminacion cancelada")
                ut.pausar_pantalla()

    if not encontrado:
        print("El usuario no existe")
        ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def cerrar_sesion(usuarios):
    print("Sesion cerrada correctamente")

    input("Presione ENTER para continuar...")

    usuario_logueado = iniciar_sesion(usuarios)

    return usuario_logueado