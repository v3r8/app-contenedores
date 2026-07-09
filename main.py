import speech_recognition as sr
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.utils import platform

# Lógica de permisos para Android
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.RECORD_AUDIO, Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])

# Importamos la librería para hardware móvil
try:
    from plyer import gps
except ImportError:
    gps = None

class AppReporteContenedores(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        layout.add_widget(MDLabel(text="Reporte de Incidencias", halign="center", font_style="H5"))
        
        self.txt_ubicacion = MDTextField(hint_text="Ubicación GPS", readonly=True)
        layout.add_widget(self.txt_ubicacion)
        
        self.txt_descripcion = MDTextField(hint_text="Descripción del daño", multiline=True)
        layout.add_widget(self.txt_descripcion)
        
        btn_gps = MDRaisedButton(text="Obtener Ubicación", on_release=self.obtener_gps)
        btn_voz = MDRaisedButton(text="Dictar Incidencia", on_release=self.iniciar_voz)
        
        layout.add_widget(btn_gps)
        layout.add_widget(btn_voz)
        
        screen.add_widget(layout)
        return screen

    def obtener_gps(self, instance):
        self.txt_ubicacion.text = "Detectando ubicación..."
        if gps:
            try:
                gps.configure(on_location=self.on_gps_location)
                gps.start()
            except Exception as e:
                self.txt_ubicacion.text = "Error al activar GPS"
        else:
            self.txt_ubicacion.text = "Badalona, ES (Simulado)"

    def on_gps_location(self, **kwargs):
        self.txt_ubicacion.text = f"Lat: {kwargs.get('lat')}, Lon: {kwargs.get('lon')}"

    def iniciar_voz(self, instance):
        self.txt_descripcion.text = "Escuchando... hable ahora."
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                texto = recognizer.recognize_google(audio, language="es-ES")
                self.txt_descripcion.text = texto
        except Exception:
            self.txt_descripcion.text = "Error al reconocer voz."

if __name__ == '__main__':
    AppReporteContenedores().run()
    