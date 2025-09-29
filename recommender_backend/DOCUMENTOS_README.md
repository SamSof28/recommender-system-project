# 📚 Guía de Gestión de Documentos

## 🎯 **Cómo agregar nuevos documentos al sistema**

### **Método 1: Usando el script automatizado (Recomendado)**

1. **Ubicación del script**: `recommender_backend/scripts/add_document.py`

2. **Uso básico**:

```bash
cd recommender_backend
python scripts/add_document.py "ruta/al/archivo.pdf" "Ingeniería de Sistemas" "Cálculo Diferencial"
```

3. **Uso completo**:

```bash
python scripts/add_document.py "ruta/al/archivo.pdf" "Ingeniería de Sistemas" "Cálculo Diferencial" "libro" "Profesor Juan"
```

**Parámetros**:

- `ruta_del_archivo`: Ruta completa al archivo que quieres agregar
- `carrera`: Nombre de la carrera (ej: "Ingeniería de Sistemas")
- `materia`: Nombre de la materia (ej: "Cálculo Diferencial")
- `tipo`: Tipo de documento (opcional, por defecto: "libro")
- `recomendado_por`: Quien lo recomienda (opcional, por defecto: "Sistema")

### **Método 2: Manual**

1. **Copiar el archivo** a la estructura de carpetas:

```
recommender_backend/data/documents/
├── Ingeniería de Sistemas/
│   ├── algebra_lineal/
│   │   └── tu_archivo.pdf
│   └── calculo_diferencial/
│       └── otro_archivo.pdf
└── Derecho/
    └── introduccion_al_derecho/
        └── documento.pdf
```

2. **Agregar a `mock_data.py`**:

```python
RESOURCES_DATA: dict[str, list[dict[str, str]]] = {
    "Tu Materia": [
        {
            "type": "libro",
            "title": "Nombre del Documento",
            "link": "http://localhost:5000/api/documents/Ingeniería de Sistemas/tu_materia/tu_archivo.pdf",
            'recommended_by': 'Quien lo recomienda'
        },
    ]
}
```

## 🔧 **Configuración del servidor**

### **Endpoints disponibles**:

1. **Servir documentos**: `GET /api/documents/<ruta_del_archivo>`

   - Ejemplo: `http://localhost:5000/api/documents/Ingeniería de Sistemas/algebra_lineal/libro.pdf`

2. **Listar documentos**: `GET /api/documents/list`
   - Devuelve todos los documentos disponibles con metadatos

### **Tipos de archivo soportados**:

- PDF (`.pdf`)
- Word (`.doc`, `.docx`)
- Texto (`.txt`)

## 🚀 **Cómo usar en el frontend**

### **Visualización de PDFs**:

- Los PDFs se abren en un visor modal integrado
- Botón "Ver PDF" para documentos tipo "libro"
- Botón "Acceder" para enlaces externos

### **Estructura de enlaces**:

```typescript
interface Recommendation {
  title: string; // Título del documento
  type: string; // Tipo: "libro", "video", "ejercicios", etc.
  link: string; // URL del documento
  score: number; // Puntuación de relevancia
}
```

## 📁 **Estructura de carpetas recomendada**

```
data/documents/
├── Ingeniería de Sistemas/
│   ├── algebra_lineal/
│   ├── calculo_diferencial/
│   ├── algoritmos_poo/
│   └── matematicas_discretas/
├── Derecho/
│   ├── introduccion_al_derecho/
│   ├── derecho_romano/
│   └── teoria_del_estado/
└── Otras Carreras/
    └── materia/
```

## ⚠️ **Consideraciones importantes**

1. **Seguridad**: Los archivos solo se sirven desde la carpeta `documents/`
2. **Nombres de archivos**: Usa nombres sin espacios o con guiones bajos
3. **Tamaño**: Los archivos grandes pueden tardar en cargar
4. **Formato**: Los PDFs se visualizan mejor en el visor integrado

## 🔄 **Flujo completo de trabajo**

1. **Agregar documento** usando el script
2. **Copiar el código** generado a `mock_data.py`
3. **Reiniciar el servidor** Flask
4. **Probar** en el frontend

## 🐛 **Solución de problemas**

### **Error "Archivo no encontrado"**:

- Verifica que el archivo existe en la ruta correcta
- Revisa que la URL en `mock_data.py` sea correcta

### **Error "Acceso denegado"**:

- El archivo está fuera de la carpeta `documents/`
- Mueve el archivo a la estructura correcta

### **PDF no se visualiza**:

- Verifica que el servidor Flask esté corriendo
- Revisa la consola del navegador para errores
- Prueba abrir el enlace directamente

## 📞 **Soporte**

Si tienes problemas, revisa:

1. Los logs del servidor Flask
2. La consola del navegador
3. Que el archivo esté en la ubicación correcta
4. Que la URL sea accesible directamente
