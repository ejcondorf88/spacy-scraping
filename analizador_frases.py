import pandas as pd

class AnalizadorFrases:
    def __init__(self, df):
        self.df = df
        
    def mostrar_estadisticas(self):
        # Año con más frases
        año_mas_frases = self.df['Año'].value_counts().idxmax()
        num_frases_año = self.df['Año'].value_counts().max()
        print(f"\nAño con más frases: {año_mas_frases} ({num_frases_año} frases)")
        
        # Autor con más frases
        autor_mas_frases = self.df['Película'].value_counts().idxmax()
        num_frases_autor = self.df['Película'].value_counts().max()
        print(f"Autor con más frases: {autor_mas_frases} ({num_frases_autor} frases)")
        
        # Top 3 años con más frases
        print("\nTop 3 años con más frases:")
        top_3_años = self.df['Año'].value_counts().head(3)
        for año, count in top_3_años.items():
            print(f"{año}: {count} frases")
            
        # Top 3 autores con más frases
        print("\nTop 3 autores con más frases:")
        top_3_autores = self.df['Película'].value_counts().head(3)
        for autor, count in top_3_autores.items():
            print(f"{autor}: {count} frases") 