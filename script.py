import os

# Ruta de la carpeta principal en Dropbox
ruta_dropbox = "/ruta/a/tu/carpeta/principal"

# Crear 400 carpetas
for i in range(1, 401):
    nombre_carpeta = f"Carpeta_{i}"
    ruta_completa = os.path.join(ruta_dropbox, nombre_carpeta)
    os.makedirs(ruta_completa)
    print(f"Carpeta creada: {ruta_completa}")

print("¡Todas las carpetas han sido creadas!")
