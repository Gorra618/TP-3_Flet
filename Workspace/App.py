import flet as ft
import mysql.connector

# --Importar los archivos correspondiente al sistema con las clases
from Usuario import Herramienta_Usuario


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="NikoStasyszyn",
            database="Taller_Mecanico",
            ssl_disabled=True,
        )
        if connection.is_connected():
            print("Conexión exitosa")
            return connection
    except Exception as ex:
        print("Conexión errónea")
        print(ex)
        return None


connection = connect_to_db()


def menu_principal(page: ft.Page):
    page.window.maximized = True
    page.title = "Administración de Taller Mecánico"

    # ----Iconos Personales---
    #  Crear un Row personalizado para el PopupMenuItem y barra de herramientas

    cliente_icono = ft.Icon(ft.Icons.PERSON, size=28)
    cliente_item = ft.Row(
        controls=[
            cliente_icono,
            ft.Text("Cliente"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    proveedor_icono = ft.Icon(ft.Icons.BUSINESS, size=28)
    proveedor_item = ft.Row(
        controls=[
            proveedor_icono,
            ft.Text("Proveedor"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    repuesto_icono = ft.Icon(ft.Icons.BUILD, size=28)
    repuesto_item = ft.Row(
        controls=[
            repuesto_icono,
            ft.Text("Repuesto"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    empleado_icono = ft.Icon(ft.Icons.PEOPLE, size=28)
    empleado_item = ft.Row(
        controls=[
            empleado_icono,
            ft.Text("Empleado"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    usuario_icono = ft.Icon(ft.Icons.PERSON_OUTLINE, size=28)
    usuario_item = ft.Row(
        controls=[
            usuario_icono,
            ft.Text("Usuario"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    ficha_tecnica_icono = ft.Icon(ft.Icons.DIRECTIONS_CAR, size=28)
    ficha_tecnica_item = ft.Row(
        controls=[ficha_tecnica_icono, ft.Text("Ficha Técnica")],
        alignment=ft.MainAxisAlignment.START,
        spacing=8,
    )

    presupuesto_icono = ft.Icon(ft.Icons.ATTACH_MONEY, size=28)
    presupuesto_icono_item = ft.Row(
        controls=[presupuesto_icono, ft.Text("Presupuesto")]
    )

    # ---Barra de Menú---
    archivo_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Copiar", icon=ft.Icons.COPY, tooltip="Copiar"),
            ft.PopupMenuItem(text="Salir", icon=ft.Icons.EXIT_TO_APP, tooltip="Salir"),
        ],
        content=ft.Text("Archivo"),
        tooltip="Archivo",
    )

    herramientas_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content=cliente_item, on_click=lambda e: cliente(e, page)),
            ft.PopupMenuItem(
                content=proveedor_item, on_click=lambda e: proveedor(e, page)
            ),
            ft.PopupMenuItem(
                content=repuesto_item, on_click=lambda e: producto(e, page)
            ),
            ft.PopupMenuItem(
                content=empleado_item, on_click=lambda e: empleado(e, page)
            ),
            ft.PopupMenuItem(content=usuario_item, on_click=lambda e: usuario(e, page)),
        ],
        content=ft.Text("Herramientas"),
        tooltip="Administrador de archivos maestros",
    )

    administracion = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content=ficha_tecnica_item),
            ft.PopupMenuItem(content=presupuesto_icono_item),
        ],
        content=ft.Text("Administración"),
        tooltip="Administración de presupuesto y ficha técnica",
    )

    # --Barra de Herramientas--
    boton_cliente_item = ft.Row(
        controls=[
            cliente_icono,
        ],
    )
    boton_cliente = ft.IconButton(icon=ft.Icons.PERSON, tooltip="Cliente")
    boton_usuario = ft.IconButton(
        icon=ft.Icons.PERSON_OUTLINE,
        tooltip="Usuario",
        on_click=lambda e: usuario(e, page),
    )

    boton_repuesto_item = ft.Row(
        controls=[
            repuesto_icono,
        ],
    )
    boton_producto = ft.IconButton(icon=ft.Icons.BUILD, tooltip="Repuesto")

    boton_ficha_tecnica_item = ft.Row(
        controls=[
            ficha_tecnica_icono,
        ]
    )
    boton_ficha_tecnica = ft.IconButton(
        ft.Icons.DIRECTIONS_CAR, tooltip="Ficha Técnica"
    )

    boton_presupuesto_item = ft.Row(
        controls=[
            presupuesto_icono,
        ]
    )
    boton_presupuesto = ft.IconButton(ft.Icons.ATTACH_MONEY, tooltip="Presupuesto")

    page.add(
        ft.Row(
            controls=[archivo_menu, administracion, herramientas_menu],
            spacing=10,
        ),
        ft.Row(
            controls=[
                boton_cliente,
                boton_producto,
                boton_ficha_tecnica,
                boton_presupuesto,
                boton_usuario,
            ]
        ),
    )


def cliente(e, page: ft.Page):
    pass


def proveedor(e, page: ft.Page):
    pass


def producto(e, page: ft.Page):
    pass


def empleado(e, page: ft.Page):
    pass


def usuario(e, page: ft.Page):
    Herramienta_Usuario(page, menu_principal)


def main(page: ft.Page):
    page.window.maximized = True
    menu_principal(page)


ft.app(target=main)
