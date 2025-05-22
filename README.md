# Análisis de Frases Célebres del Cine (AFI)

Este proyecto realiza un análisis de las 100 frases más famosas del cine según el listado de la AFI (American Film Institute), extraídas de Wikipedia. Utiliza técnicas de procesamiento de lenguaje natural para analizar tanto las frases como las palabras más comunes.

## Características

- Descarga automática de la tabla de frases desde Wikipedia
- Análisis estadístico de años y películas con más frases célebres
- Procesamiento de lenguaje natural para identificar verbos y adjetivos más comunes
- Visualización de resultados en formato tabular

## Estructura del Proyecto

```
.
├── Main.py                 # Script principal
├── analizador_frases.py    # Análisis de estadísticas por año y película
├── analizador_palabras.py  # Análisis de verbos y adjetivos con spaCy
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet (para descargar datos y modelos)

## Instalación

1. **Clona el repositorio y entra a la carpeta:**
   ```bash
   git clone <URL-del-repo>
   cd dispositivos-moviles/01
   ```

2. **Crea y activa un entorno virtual (recomendado):**
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

Para ejecutar el análisis completo:

```bash
python Main.py
```

El programa realizará las siguientes acciones:
1. Descargará la tabla de frases desde Wikipedia
2. Mostrará estadísticas de años y películas con más frases
3. Analizará los verbos y adjetivos más comunes
4. Presentará los resultados en formato tabular

## Solución de Problemas

- Si encuentras advertencias sobre `read_html`, estas son normales y no afectan el funcionamiento del programa
- Asegúrate de tener una conexión estable a internet para la primera ejecución
- Si el modelo de spaCy no se descarga correctamente, intenta ejecutar el comando de instalación manualmente

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:
1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

- Elian Condor

## Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio.