import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "App Contenedores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos de texto de la interfaz
    status_text = ft.Text("Estado GPS: Pendiente", size=14)
    image_text = ft.Text("Imagen: Ninguna", size=14)

    def capturar_contenedor(e):
        status_text.value = "Estado: Botón pulsado correctamente"
        status_text.color = ft.Colors.GREEN
        image_text.value = "Imagen: Modo seguro activo"
        page.update()

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

# ESTA LÍNEA ES NECESARIA PARA QUE LA APP SE QUEDE ABIERTA:
if __name__ == "__main__":
    ft.app(target=main)