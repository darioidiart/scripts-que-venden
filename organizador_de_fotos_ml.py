import os
from PIL import Image
import argparse

def organizar_fotos(carpeta_origen, prefijo="producto", ancho=1200):
    """
    Renombra, redimensiona y optimiza fotos para Mercado Libre / Tienda Online
    """
    if not os.path.exists(carpeta_origen):
        print(f"❌ No existe la carpeta: {carpeta_origen}")
        return

    archivos = [f for f in os.listdir(carpeta_origen) if f.lower().endswith(('.jpg','.jpeg','.png'))]
    archivos.sort()

    print(f"📸 Encontradas {len(archivos)} fotos...")

    for i, archivo in enumerate(archivos, 1):
        ruta_vieja = os.path.join(carpeta_origen, archivo)
        nuevo_nombre = f"{prefijo}_{i:03d}.jpg"
        ruta_nueva = os.path.join(carpeta_origen, nuevo_nombre)

        try:
            # Abrir, redimensionar y guardar optimizado
            with Image.open(ruta_vieja) as img:
                img = img.convert("RGB")
                w_percent = (ancho / float(img.size[0]))
                h_size = int((float(img.size[1]) * float(w_percent)))
                img = img.resize((ancho, h_size), Image.LANCZOS)
                img.save(ruta_nueva, "JPEG", quality=85, optimize=True)

            if ruta_vieja!= ruta_nueva:
                os.remove(ruta_vieja)

            print(f"✅ {archivo} -> {nuevo_nombre}")
        except Exception as e:
            print(f"⚠️ Error con {archivo}: {e}")

    print("\n¡Listo! Fotos listas para subir a ML.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organizador de fotos para e-commerce")
    parser.add_argument("carpeta", help="Carpeta con fotos")
    parser.add_argument("--prefijo", default="producto", help="Prefijo del nombre")
    args = parser.parse_args()

    organizar_fotos(args.carpeta, args.prefijo)
