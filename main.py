import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "App Contenedores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Inicialización correcta del FilePicker y su registro en el overlay
    file_picker = ft.FilePicker()
    file_picker.on_result = on_dialog_result
    page.overlay.append(file_picker)
    page.update()  # <-- ¡Importante! Se actualiza la página aquí para que el móvil lo reconozca

    def capturar_contenedor(e):
        status_text.value = "Estado: Abriendo selector..."
        status_text.color = ft.Colors.BLUE
        page.update()
        file_picker.pick_files(allow_multiple=False)

    # Elementos visuales de tu interfaz
    status_text = ft.Text("Estado GPS: Pendiente", size=14)
    image_text = ft.Text("Imagen: Ninguna", size=14)

    btn_capturar = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.CAMERA_ALT),
                ft.Text("Tomar Foto y Obtener GPS"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=capturar_contenedor,
    )

    # Añadir los controles principales a la vista
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

# Ejecutar la aplicación Flet
ft.app(target=main)