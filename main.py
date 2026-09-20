import flet as ft

def main(page: ft.Page):
    page.title = "App Contenedores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    status_text = ft.Text("Estado GPS: Pendiente", size=14)
    image_text = ft.Text("Imagen: Ninguna", size=14)

    def capturar_contenedor(e):
        status_text.value = "Estado: Botón pulsado correctamente"
        status_text.color = ft.colors.GREEN
        image_text.value = "Imagen: Modo seguro activo"
        page.update()

    btn_capturar = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.icons.CAMERA_ALT),
                ft.Text("Tomar Foto y Obtener GPS"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=capturar_contenedor,
    )

    page.add(
        ft.Column(
            [
                status_text,
                image_text,
                btn_capturar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )