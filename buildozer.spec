[app]

# (str) Title of your application
title = Control de Contenedores

# (str) Package name
package.name = appcontenedores

# (str) Package domain (needed for android packaging)
package.domain = org.v3r8

# (str) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let it include directory)
source.include_dirs = assets

# (list) Application requirements
requirements = python3,flet

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (str) Android architecture to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1