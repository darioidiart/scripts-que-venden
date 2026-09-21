import os

# Cambiá "fotos" por el nombre de tu carpeta
carpeta = "./fotos"
contador = 0

for archivo in os.listdir(carpeta):
    viejo = os.path.join(carpeta, archivo)
    # Solo renombra archivos, no carpetas
    if os.path.isfile(viejo):
        contador += 1
        nuevo_nombre = f"producto-{contador}.jpg"
        nuevo = os.path.join(carpeta, nuevo_nombre)
        os.rename(viejo, nuevo)
        print(f"{archivo} -> {nuevo_nombre}")

print(f"\nListo! Renombre {contador} fotos")
