# Sistema de Recomendación de Recursos de Estudio - API

API REST desarrollada en Flask para el sistema de recomendación de recursos de estudio basado en competencias estudiantiles.

## 🚀 Características

- **Recomendaciones inteligentes** basadas en competencias de estudiantes
- **API REST** con endpoints bien documentados
- **CORS habilitado** para integración con frontend
- **Manejo de errores** robusto
- **Validación de datos** completa

## 📋 Endpoints Disponibles

### 1. Obtener Carreras

```http
GET /api/careers
```

**Respuesta:**

```json
{
  "status": "success",
  "careers": ["Ingenieria de Sistemas", "Derecho"]
}
```

### 2. Obtener Semestres

```http
GET /api/semesters/{career}
```

**Respuesta:**

```json
{
  "status": "success",
  "career": "Ingenieria de Sistemas",
  "semesters": [1, 2]
}
```

### 3. Obtener Cursos

```http
GET /api/courses/{career}/{semester}
```

**Respuesta:**

```json
{
  "status": "success",
  "career": "Ingenieria de Sistemas",
  "semester": 2,
  "courses": ["Algebra Lineal", "Calculo Diferencial", ...]
}
```

### 4. Obtener Recomendaciones

```http
POST /api/recommendations
Content-Type: application/json

{
  "career": "Ingenieria de Sistemas",
  "semester": 2,
  "course": "Algebra Lineal"
}
```

**Respuesta:**

```json
{
  "status": "success",
  "carrera": "Ingenieria de Sistemas",
  "semestre": 2,
  "curso": "Algebra Lineal",
  "recommendations": [
    {
      "title": "Introducción al Algebra Lineal",
      "type": "video",
      "link": "https://youtu.be/...",
      "score": 4.0
    }
  ]
}
```

## 🛠️ Instalación y Ejecución

### Opción 1: Ejecución Local

1. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

2. **Ejecutar la API:**

```bash
python api/app.py
```

3. **Acceder a la API:**

```
http://localhost:5000
```

### Opción 2: Docker

1. **Construir la imagen:**

```bash
docker build -t recommender-api .
```

2. **Ejecutar el contenedor:**

```bash
docker run -p 5000:5000 recommender-api
```

### Opción 3: Docker Compose

```bash
docker-compose up --build
```

## 🌐 Despliegue

### Heroku

1. Crear archivo `Procfile`:

```
web: python api/app.py
```

2. Desplegar:

```bash
git push heroku main
```

### Railway

1. Conectar repositorio de GitHub
2. Configurar variables de entorno
3. Desplegar automáticamente

### Render

1. Conectar repositorio de GitHub
2. Configurar build command: `pip install -r requirements.txt`
3. Configurar start command: `python api/app.py`

## 📁 Estructura del Proyecto

```
api/
├── app.py              # Aplicación principal Flask
├── config.py           # Configuraciones
└── README.md           # Documentación

data/
├── mock_data.py        # Datos de prueba
└── documents/          # Recursos de estudio

src/
├── core/
│   ├── algebra.py      # Cálculos de álgebra lineal
│   └── recommender.py  # Lógica de recomendación
└── main.py             # Aplicación de consola

requirements.txt        # Dependencias Python
Dockerfile             # Configuración Docker
docker-compose.yml     # Orquestación Docker
```

## 🔧 Variables de Entorno

- `FLASK_ENV`: Entorno de ejecución (development/production)
- `PORT`: Puerto de la aplicación (default: 5000)
- `SECRET_KEY`: Clave secreta para Flask

## 📝 Notas de Desarrollo

- La API está configurada para desarrollo con `debug=True`
- CORS está habilitado para permitir conexiones desde frontend
- Los datos se cargan desde `data/mock_data.py`
- El sistema de recomendación usa álgebra lineal para calcular competencias

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abrir un Pull Request
