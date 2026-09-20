import flet as ft

def main(page: ft.Page):
    page.title = "Control de Contenedores"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Elementos visuales iniciales para comprobar que la app arranca correctamente
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Icon(ft.icons.CONTAINER, size=60, color=ft.colors.BLUE),
                    ft.Text("Control de Contenedores", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Estado: Conectado y estable", size=14, color=ft.colors.GREEN),
                    ft.Container(height=20),
                    ft.ElevatedButton("Iniciar Operación", icon=ft.icons.PLAY_ARROW)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main)