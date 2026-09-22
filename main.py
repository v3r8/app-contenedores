import flet as ft


def main(page: ft.Page):
    page.title = "Control de Contenedores"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Control de Contenedores",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text("Estado: Conectado", size=16, color=ft.colors.GREEN),
                ft.ElevatedButton("Iniciar Operación"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )