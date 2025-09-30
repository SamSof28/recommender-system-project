# Instrucciones para Desarrollo Local

## Problema Identificado

El dropdown de carreras no aparecía porque el frontend estaba intentando conectarse a un servidor remoto (`recommender-api-ffpd.onrender.com`) en lugar del backend local.

## Solución Implementada

### 1. Configuración de API Centralizada

Se creó el archivo `recommender_frontend/src/app/config/api.ts` que maneja las URLs del backend de forma centralizada.

### 2. Actualización del Frontend

Se actualizaron los componentes para usar la configuración centralizada:

- `RecommendationForm.tsx`
- `page.tsx`

### 3. Script de Inicio del Backend

Se creó `recommender_backend/start_backend.py` para facilitar el inicio del servidor local.

## Cómo Ejecutar el Proyecto

### Paso 1: Iniciar el Backend

```bash
cd recommender_backend
python start_backend.py
```

El servidor se iniciará en `http://localhost:5000`

### Paso 2: Iniciar el Frontend

```bash
cd recommender_frontend
npm run dev
```

El frontend se iniciará en `http://localhost:3000`

## Verificación

1. Abre `http://localhost:3000` en tu navegador
2. El dropdown de "Carrera" debería mostrar:
   - Ingenieria de Sistemas
   - Derecho

## Configuración de Entorno

Para cambiar entre backend local y remoto, modifica la variable `USE_LOCAL_BACKEND` en `recommender_frontend/src/app/config/api.ts`:

```typescript
const USE_LOCAL_BACKEND = true; // Para usar backend local
const USE_LOCAL_BACKEND = false; // Para usar backend remoto
```

## Endpoints del Backend

- `GET /api/careers` - Obtener lista de carreras
- `GET /api/semesters/<career>` - Obtener semestres de una carrera
- `GET /api/courses/<career>/<semester>` - Obtener cursos de una carrera y semestre
- `POST /api/recommendations` - Obtener recomendaciones
- `GET /api/documents/<path:filename>` - Servir documentos
- `GET /api/documents/list` - Listar documentos disponibles
