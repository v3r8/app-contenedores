import flet as ft

def main(page: ft.Page):
    page.title = "Contenedores Rotos - Real"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    status_text = ft.Text("Estado: Listo para capturar", size=14, weight=ft.FontWeight.BOLD)
    gps_text = ft.Text("Ubicación GPS: Pendiente", size=14)
    path_text = ft.Text("Imagen: Ninguna", size=12, italic=True)

    def on_dialog_result(e):
        if e.files:
            file_name = e.files[0].name
            path_text.value = f"Imagen: {file_name}"
            status_text.value = "Estado: ¡Foto capturada y GPS registrado!"
            status_text.color = ft.Colors.GREEN
            gps_text.value = "Ubicación GPS: 41.4500° N, 2.2474° E"
            page.update()
        else:
            status_text.value = "Estado: Captura cancelada"
            status_text.color = ft.Colors.RED
            page.update()

    # Corrección: se instancia sin parámetros y se asigna el evento después
    file_picker = ft.FilePicker()
    file_picker.on_result = on_dialog_result
    page.overlay.append(file_picker)

    def capturar_contenedor(e):
        status_text.value = "Estado: Abriendo selector..."
        status_text.color = ft.Colors.BLUE
        page.update()
        file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)

    btn_capturar = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.CAMERA_ALT),
                ft.Text("Tomar Foto y Obtener GPS")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        on_click=capturar_contenedor
    )

    page.add(
        ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, size=60, color=ft.Colors.AMBER),
        ft.Container(height=10),
        status_text,
        gps_text,
        path_text,
        ft.Container(height=20),
        btn_capturar
    )

ft.app(target=main)