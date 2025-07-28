import flet as ft


def Herramienta_Usuario(page: ft.Page, volver_callback):

    nombre = ft.TextField(label="Nombre", width=300)
    apellido = ft.TextField(label="Apellido", width=300)
    email = ft.TextField(label="Email", width=300)
    usuario = ft.TextField(label="Usuario", width=300)
    contrasena = ft.TextField(label="Contraseña", password=True, width=300)

    guardar_btn = ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE)
    limpiar_btn = ft.ElevatedButton("Limpiar", icon=ft.Icons.CLEAR)
    volver_btn = ft.ElevatedButton(
        "Volver", icon=ft.Icons.ARROW_BACK, on_click=lambda e: volver_callback(page)
    )

    page.controls.clear()
    page.add(
        ft.Column(
            [
                ft.Text("Gestión de Usuarios", size=24, weight="bold"),
                nombre,
                apellido,
                email,
                usuario,
                contrasena,
                ft.Row([guardar_btn, limpiar_btn, volver_btn], spacing=10),
            ],
            spacing=10,
        )
    )
    page.update()
