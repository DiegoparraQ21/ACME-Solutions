import json

def auditar_datos(origin):

    usuarios = origin.get("usuarios", [])
    contactos = origin.get("contactos", [])

    reporte = {
        "usuarios_con_errores": [],
        "contactos_con_errores": [],
        "resumen": {}
    }

    emails_vistos = {}
    ids_contactos = {}

    usuarios_email_duplicado = 0
    contactos_id_duplicado = 0

# --------------------- AUDITORÍA DE USUARIOS -----------------------
    for usuario in usuarios:

        errores = []

        if not usuario.get("id"):
            errores.append("Falta el id")

        if not usuario.get("email"):
            errores.append("Falta el email")

        if not usuario.get("nombres"):
            errores.append("Falta el nombre")

        if not usuario.get("apellidos"):
            errores.append("Falta el apellido")

        email = usuario.get("email")

        if email:

            if email in emails_vistos:
                errores.append("Email duplicado")
                usuarios_email_duplicado += 1
            else:
                emails_vistos[email] = True

        if errores:
            reporte["usuarios_con_errores"].append({
                "email": usuario.get("email", "Sin email"),
                "id": usuario.get("id", "Sin id"),
                "errores": errores
            })

# --------------------- AUDITORÍA DE CONTACTOS ---------------------
    for contacto in contactos:

        errores = []

        if not contacto.get("id"):
            errores.append("Falta el id")

        if not contacto.get("nombre"):
            errores.append("Falta el nombre")

        if not contacto.get("telefono"):
            errores.append("Falta el teléfono")

        contacto_id = contacto.get("id")

        if contacto_id:

            if contacto_id in ids_contactos:
                errores.append("ID duplicado")
                contactos_id_duplicado += 1
            else:
                ids_contactos[contacto_id] = True

        if errores:
            reporte["contactos_con_errores"].append({
                "id": contacto.get("id", "Sin id"),
                "errores": errores
            })

    # ----------------- RESUMEN -------------------
    reporte["resumen"] = {
        "total_usuarios": len(usuarios),
        "total_contactos": len(contactos),
        "usuarios_con_errores": len(reporte["usuarios_con_errores"]),
        "contactos_con_errores": len(reporte["contactos_con_errores"]),
        "usuarios_con_email_duplicado": usuarios_email_duplicado,
        "contactos_con_id_duplicado": contactos_id_duplicado
    }

    if (
        len(reporte["usuarios_con_errores"]) == 0 and
        len(reporte["contactos_con_errores"]) == 0
    ):
        reporte["mensaje"] = "No se encontraron errores en los datos"

# ----------------- GENERAR JSON ----------------------
    with open("reporte_auditoria_datos.json", "w", encoding="utf-8") as archivo:
        json.dump(reporte, archivo, indent=4, ensure_ascii=False)

    print("Reporte generado correctamente")