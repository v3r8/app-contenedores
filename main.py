import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "App Contenedores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos de texto de la interfaz
    status_text = ft.Text("Estado GPS: Pendiente", size=14)
    image_text = ft.Text("Imagen: Ninguna", size=14)

    # Función que se ejecuta al seleccionar o hacer la foto
    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files:
            image_text.value = f"Imagen: {e.files[0].name}"
            status_text.value = "Estado: Imagen seleccionada"
            status_text.color = ft.Colors.GREEN
            page.update()

    # Inicialización del FilePicker y su registro en el overlay
    file_picker = ft.FilePicker()
    file_picker.on_result = on_dialog_result
    page.overlay.append(file_picker)
    page.update()

    def capturar_contenedor(e):
        status_text.value = "Estado: Abriendo selector..."
        status_text.color = ft.Colors.BLUE
        page.update()
        file_picker.pick_files(allow_multiple=False)

    # Botón principal
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

    # Añadir los elementos visuales a la página
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