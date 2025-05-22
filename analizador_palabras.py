import pandas as pd
import spacy
from collections import Counter

class AnalizadorPalabras:
    def __init__(self, df):
        self.df = df
        self.nlp = spacy.load("es_core_news_sm")
        
    def analizar_palabras(self):
        # Concatenar todas las frases
        todas_frases = " ".join(self.df['Frase'].astype(str))
        
        # Procesar el texto con spaCy
        doc = self.nlp(todas_frases)
        
        # Encontrar verbos
        verbos = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        verbos_comunes = Counter(verbos).most_common(10)
        
        print("\nTop 10 verbos más comunes:")
        for verbo, count in verbos_comunes:
            print(f"{verbo}: {count} veces")
            
        # Encontrar adjetivos
        adjetivos = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
        adjetivos_comunes = Counter(adjetivos).most_common(10)
        
        print("\nTop 10 adjetivos más comunes:")
        for adjetivo, count in adjetivos_comunes:
            print(f"{adjetivo}: {count} veces") 