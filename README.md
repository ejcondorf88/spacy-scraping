# Análisis de Frases Célebres del Cine (AFI)

Este proyecto realiza un análisis de las 100 frases más famosas del cine según el listado de la AFI (American Film Institute), extraídas de Wikipedia. Utiliza técnicas de procesamiento de lenguaje natural para analizar tanto las frases como las palabras más comunes.

## Estructura del Proyecto

- `Main.py`: Script principal que descarga la tabla de frases, la procesa y muestra estadísticas.
- `analizador_frases.py`: Analiza estadísticas sobre los años y películas con más frases.
- `analizador_palabras.py`: Analiza los verbos y adjetivos más comunes usando spaCy.
- `requirements.txt`: Lista de dependencias necesarias.

## Requisitos

- Python 3.8+
- pip
- Acceso a internet (para descargar la tabla de Wikipedia y el modelo de spaCy)

## Instalación

1. **Clona el repositorio y entra a la carpeta:**
   ```bash
   git clone <URL-del-repo>
   cd dispositivos-moviles/01
   ```
2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En Mac/Linux
   source venv/bin/activate
   ```
3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Instala el modelo de spaCy para español:**
   ```bash
   python -m spacy download es_core_news_sm
   ```

## Uso

Ejecuta el script principal:
```bash
python Main.py
```

El programa descargará la tabla de frases, mostrará estadísticas de los años y películas con más frases, y analizará los verbos y adjetivos más comunes en las frases.

## Notas
- Si ves advertencias sobre `read_html`, puedes ignorarlas por ahora, pero en el futuro será recomendable actualizar el código para usar `StringIO`.
- El script requiere conexión a internet para descargar los datos y el modelo de spaCy la primera vez.

## Autor
- [Tu Nombre] 