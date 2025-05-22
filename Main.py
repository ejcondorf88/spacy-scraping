import pandas as pd
import requests
from bs4 import BeautifulSoup
from analizador_frases import AnalizadorFrases
from analizador_palabras import AnalizadorPalabras

def main():
    # URL de la página
    url = "https://es.wikipedia.org/wiki/Anexo:AFI%27s_100_a%C3%B1os..._100_frases"
    
    print("Obteniendo datos de Wikipedia...")
    # Obtener la tabla
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabla = soup.find('table', {'class': 'wikitable'})
    
    print("Convirtiendo tabla a DataFrame...")
    # Convertir la tabla a DataFrame
    df = pd.read_html(str(tabla))[0]
    print(f"Columnas en el DataFrame: {df.columns.tolist()}")
    print(f"Número de filas: {len(df)}")
    
    print("\nCreando analizadores...")
    # Crear instancias de los analizadores
    analizador_frases = AnalizadorFrases(df)
    analizador_palabras = AnalizadorPalabras(df)
    
    # Análisis de frases
    print("\n=== Análisis de Frases ===")
    analizador_frases.mostrar_estadisticas()
    
    # Análisis de palabras
    print("\n=== Análisis de Palabras ===")
    analizador_palabras.analizar_palabras()

if __name__ == "__main__":
    main()
