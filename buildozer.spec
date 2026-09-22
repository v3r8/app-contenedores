[app]

# (str) Título de tu aplicación
title = Mi Aplicacion

# (str) Nombre del paquete
package.name = miapp

# (str) Dominio del paquete
package.domain = org.flet

# (list) Archivos fuente a incluir
source.include_exts = py,png,jpg,atlas

# (list) Requisitos de la aplicación
requirements = python3,flet

# (int) Versión de la API de destino de Android
android.targetsdk = 34

# (int) Versión mínima de la API que soportará tu APK
android.minsdk = 26

# (str) Arquitectura de Android compatible (64-bit para tu móvil)
android.archs = arm64-v8a

# (list) Permisos necesarios (opcional)
# android.permissions = INTERNET

[buildozer]

# (int) Nivel de registro (0 = solo errores, 1 = info, 2 = debug)
log_level = 2

# (int) Modo de depuración al construir (0 = release, 1 = debug)
android.debug_identity = 1