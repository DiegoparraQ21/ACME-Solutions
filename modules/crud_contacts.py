import modules.core as cr
import modules.utils as ut
import modules.messages as ms
from tabulate import tabulate

def registrar_contacto(contactos):

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
    print("Registrar contacto")
        
    n_identificacion = pedir_numero("Ingrese el numero de identificacion o ID interno: ")
    nombres = pedir_texto("Ingrese los nombres: ")
    apellidos = pedir_texto("Ingrese los apellidos: ")
    telefono = pedir_numero("Ingrese el teléfono principal: ")
    email = pedir_texto("Ingrese el e-mail: ")
    direccion = pedir_texto("Ingrese la direccion: ")
    tipo = pedir_texto("Ingrese el tipo de contacto: ")
    notas = pedir_texto("Ingrese notas u observaciones: ")
    
    contacto = {
        "ID": n_identificacion,
        "nombre": nombres,
        "apellido": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "tipo": tipo,
        "nota": notas
    }

    contactos["contactos"].append(contacto)

    cr.AddData(contactos)

    print("Contacto agregado exitosamente.")
    ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def listar_contactos(contactos):
    ut.borrar_pantalla()
    print("Lista de contactos")

    if not contactos:
        print("No hay contactos registrados")
        ut.pausar_pantalla()
        return

    tabla = []

    for contacto in contactos:
        nombre_completo = f"{contacto.get('nombre', '')} {contacto.get('apellido', '')}"

        tabla.append([
            contacto.get("ID"),
            nombre_completo,
            contacto.get("telefono"),
            contacto.get("email"),
            contacto.get("tipo")
        ])

    print(tabulate(tabla, headers = ['ID', 'Nombre completo', 'Telefono', 'E-mail', 'Tipo']))
    
    ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def buscar_contactos(contactos):
    ut.borrar_pantalla()
    print("Buscar contactos")

    if not contactos:
        print("No hay contactos registrados")
        ut.pausar_pantalla()
        return
    
    print(ms.buscar_contacto)

    try:
        opcion = int(input("Ingrese el numero de la opcion: "))
    except ValueError:
        print(ms.dato_incorrecto)
        ut.pausar_pantalla()
        return

    if opcion == 0:
        return

    resultados = []

    if opcion == 1:
        buscar = input("Ingrese el ID: ")

    elif opcion == 2:
        buscar = input("Ingrese los nombres o apellidos: ").lower()

    elif opcion == 3:
        buscar = input("Ingrese el tipo de contacto: ").lower()

    else:
        print("Opción inválida")
        ut.pausar_pantalla()
        return
    #----------------------------------
    for contacto in contactos:

        if opcion == 1:
            if str(contacto.get("ID")) == buscar:
                resultados.append(contacto)

        elif opcion == 2:
            nombre = contacto.get("nombre", "").lower()
            apellido = contacto.get("apellido", "").lower()

            if buscar in nombre or buscar in apellido:
                resultados.append(contacto)

        elif opcion == 3:
            tipo = contacto.get("tipo", "").lower()

            if buscar in tipo:
                resultados.append(contacto)

    # -----------------------------------
    if not resultados:
        print("No se encontraron contactos")
        ut.pausar_pantalla()
        return

    tabla = []

    for contacto in resultados:
        nombre_completo = f"{contacto.get('nombre', '')} {contacto.get('apellido', '')}"

        tabla.append([
            contacto.get("ID"),
            nombre_completo,
            contacto.get("telefono"),
            contacto.get("email"),
            contacto.get("tipo")
        ])

    print(tabulate(tabla, headers=['ID', 'Nombre completo', 'Telefono', 'E-mail', 'Tipo']))

    ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def actualizar_contacto(contactos):
    ut.borrar_pantalla()
    print("Actualizar contacto")

    n_identificacion = int(input("Ingrese el ID del contacto a actualizar: "))

    encontrado = False

    for contacto in contactos["contactos"]:

        if contacto["ID"] == n_identificacion:

            encontrado = True
            
            new_nombre = input(f"Nombres ({contacto['nombre']}): ").lower()
            new_apellido = input(f"Apellidos ({contacto['apellido']}): ").lower()
            new_telefono = int(input(f"Telefono ({contacto['telefono']}): "))
            new_email = input(f"E-mail ({contacto['email']}) ").lower()
            new_direccion = input(f"Direccion ({contacto['direccion']}): ").lower()
            new_tipo = input(f"Tipo de contacto ({contacto['tipo']}): ").lower()
        
            contacto.update({
                "nombre": new_nombre,
                "apellido": new_apellido,
                "telefono": new_telefono,
                "email": new_email,
                "direccion": new_direccion,
                "tipo": new_tipo
            })

            cr.AddData(contactos)

            print("Contacto actualizado exitosamente.")
            ut.pausar_pantalla()

            break

    if not encontrado:
        print("ID no encontrado")
        ut.pausar_pantalla()

#---------------------------------------------------------------------------------------------------
def eliminar_contacto(contactos):
    ut.borrar_pantalla()
    print("Eliminar contacto")

    n_identificacion = int(input("Ingrese el ID del contacto a eliminar: "))

    encontrado = False

    for contacto in contactos["contactos"]:

        if contacto["ID"] == n_identificacion:

            encontrado = True

            confirmacion = input(f"Desea eliminar a {contacto['nombre']} {contacto['apellido']}? (S/N): ").lower()

            if confirmacion == "s":

                contactos["contactos"].remove(contacto)

                print("Contacto eliminado")

                cr.AddData(contactos)
                ut.pausar_pantalla()
            else:
                print("Eliminacion cancelada")
                ut.pausar_pantalla()

    if not encontrado:
        print("El contacto no existe")
        ut.pausar_pantalla()