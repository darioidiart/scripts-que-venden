import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def scrapear_ml(busqueda, paginas=2):
    print(f"🔍 Buscando: {busqueda}...")
    productos = []
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for pagina in range(1, paginas+1):
        url = f"https://listado.mercadolibre.com.ar/{busqueda.replace(' ', '-')}_Desde_{(pagina-1)*50+1}"
        print(f"📄 Página {pagina}")
        
        try:
            r = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            items = soup.find_all('li', class_='ui-search-layout__item')
            
            for item in items:
                try:
                    titulo = item.find('h2', class_='ui-search-item__title').text.strip()
                    precio_text = item.find('span', class_='andes-money-amount__fraction').text.strip()
                    precio = float(precio_text.replace('.',''))
                    link = item.find('a')['href']
                    
                    productos.append({
                        'titulo': titulo,
                        'precio': precio,
                        'link': link,
                        'fecha': datetime.now().strftime('%Y-%m-%d')
                    })
                except:
                    continue
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
    
    if productos:
        df = pd.DataFrame(productos)
        nombre = f"precios_{busqueda.replace(' ','_')}.xlsx"
        df.to_excel(nombre, index=False)
        print(f"✅ {len(productos)} productos en {nombre}")
        print(f"Barato: ${df['precio'].min()} | Caro: ${df['precio'].max()} | Promedio: ${df['precio'].mean():.0f}")
    else:
        print("❌ No se encontró nada")

if __name__ == "__main__":
    busqueda = input("¿Qué producto querés scrapear? Ej: zapatillas nike: ")
    scrapear_ml(busqueda)
