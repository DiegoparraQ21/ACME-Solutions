import modules.core as cr
import modules.utils as ut
import modules.crud_users as cu
import modules.crud_contacts as cc
import modules.messages as ms

if __name__ == "__main__":

    origin = {}
    cr.MY_DATABASE = "data/agenda.json"
    cr.CheckFile(origin)

    print("Bienvenido al gestor de contactos")

    usuario_logueado = cu.iniciar_sesion(origin["usuarios"])

    isActive = True

    while isActive:

        try:
            ut.borrar_pantalla()

            print(f"Usuario activo: {usuario_logueado['nombres']} {usuario_logueado['apellidos']} - Rol: {usuario_logueado['rol']}")

            if usuario_logueado['rol'] == "admin":

                opcion = int(input(ms.menu_principal_usuarios_admin))

                match opcion:
                    case 1:
                        cc.registrar_contacto(origin)
                    case 2:
                        cc.listar_contactos(origin["contactos"])
                    case 3:
                        cc.buscar_contactos(origin["contactos"])
                    case 4:
                        cc.actualizar_contacto(origin)
                    case 5:
                        cc.eliminar_contacto(origin)
                    case 6:
                        cu.registrar_usuario(origin)
                    case 7:
                        cu.listar_usuarios(origin["usuarios"])
                    case 8:
                        cu.actualizar_usuario(origin)
                    case 9:
                        cu.eliminar_usuario(origin)
                    case 10:
                        usuario_logueado = cu.cerrar_sesion(origin["usuarios"])
                    case 0:
                        print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
                        isActive = False
                    case _:
                        print(ms.seleccion_invalida)
                        ut.pausar_pantalla()

            else:
                opcion = int(input(ms.menu_principal_usuarios_noadmin))

                match opcion:
                    case 1:
                        cc.registrar_contacto(origin)
                    case 2:
                        cc.listar_contactos(origin["contactos"])
                    case 3:
                        cc.buscar_contactos(origin["contactos"])
                    case 4:
                        cc.actualizar_contacto(origin)
                    case 5:
                        cc.eliminar_contacto(origin)
                    case 6:
                        usuario_logueado = cu.cerrar_sesion(origin["usuarios"])
                    case 0:
                        print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
                        isActive = False
                    case _:
                        print(ms.seleccion_invalida)
                        ut.pausar_pantalla()
        except:
            print(ms.dato_incorrecto)
            ut.pausar_pantalla()