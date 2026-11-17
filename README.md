# Análisis de Canciones Clásicas del Rock

Proyecto desarrollado en Python para analizar un conjunto de canciones clásicas del rock utilizando las librerías NumPy, Pandas, SciPy y Matplotlib.

## Descripción

El programa permite analizar un dataset de canciones de rock y visualizar información relevante mediante estadísticas y gráficos.

Los datos incluyen:

- Título de la canción
- Artista
- Género
- Duración
- Año de lanzamiento
- Reproducciones en millones

## Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- SciPy
- Matplotlib

## Estructura del proyecto

```
📁 Proyecto
│
├── main.py
├── analisis.py
├── canciones_rock.csv
├── requirement.txt
└── README.md
```

## Funcionalidades

### 1. Top 5 canciones más escuchadas

Muestra las cinco canciones con mayor cantidad de reproducciones.

### 2. Reproducciones por género

Agrupa las canciones por género y calcula el total de reproducciones.

### 3. Gráfico por género

Genera un gráfico de barras con las reproducciones acumuladas por género.

### 4. Gráfico de canciones más escuchadas

Muestra un gráfico con las canciones que tienen más reproducciones.

### 5. Resumen y exploración en la interfaz web

La interfaz muestra estadísticas generales de la colección, permite buscar por canción o artista y filtrar el catálogo por género. Los gráficos y las canciones se cargan desde `canciones_rock.csv`.

## Dataset

El archivo `canciones_rock.csv` contiene información de 20 canciones clásicas del rock con sus respectivas reproducciones en plataformas de streaming.

Ejemplo:

| Título | Artista | Género |
|----------|----------|----------|
| Bohemian Rhapsody | Queen | Rock clásico |
| Highway to Hell | AC/DC | Hard rock |
| Enter Sandman | Metallica | Heavy metal |

## Instalación

1. Clonar o descargar el proyecto.

2. Instalar las dependencias:

```bash
pip install -r requirement.txt
```

## Ejecución

Ejecutar:

```bash
python main.py
```

### Interfaz web

Iniciá el servidor local:

```bash
python app.py
```

Después, abrí <http://127.0.0.1:8000> en el navegador. Para detenerlo, presioná `Ctrl+C` en la terminal.

## Menú del programa

```
===== MENÚ =====

1 - Top 5 canciones
2 - Reproducciones por género
3 - Gráfico por género
4 - Gráfico canciones más escuchadas
0 - Salir
```

## Autoras

- Cecilia Muo
- Lucia Ballester Gañez
- Lucia Amarilla

## Materia

Ciencia de Datos
