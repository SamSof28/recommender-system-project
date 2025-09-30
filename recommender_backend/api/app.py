from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS  # Necesario para conectar con Next.js (Frontend)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.core.recommender import recommend_resources
from src.core.algebra import create_student_vectors, calculate_magnitudes
from data.mock_data import ACADEMIC_DATA, RESOURCES_DATA, GRADES_DATA

app = Flask(__name__) # Instancia de Flask
CORS(app, origins=['*']) # Configuración de CORS para permitir conexiones desde cualquier origen

# Configurar la carpeta de documentos como archivos estáticos
DOCUMENTS_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data', 'documents')

@app.route('/api/careers', methods=['GET'])
def get_careers():
    """Endpoint para obtener todas las carreras disponibles."""
    try:
        careers = list(ACADEMIC_DATA.keys())
        return jsonify({
            "status": "success",
            "careers": careers
        })
    except Exception as e:
        return jsonify({"error": f"Error al obtener carreras: {str(e)}"}), 500

@app.route('/api/semesters/<career>', methods=['GET'])
def get_semesters(career):
    """Endpoint para obtener los semestres disponibles para una carrera."""
    try:
        if career not in ACADEMIC_DATA:
            return jsonify({'error': 'Carrera no encontrada'}), 404
            
        semesters = list(ACADEMIC_DATA[career].keys())
        return jsonify({
            "status": "success",
            "career": career,
            "semesters": semesters
        })
    except Exception as e:
        return jsonify({"error": f"Error al obtener semestres: {str(e)}"}), 500

@app.route('/api/courses/<career>/<int:semester>', methods=['GET'])
def get_courses(career, semester):
    """Endpoint para obtener los cursos disponibles para una carrera y semestre."""
    try:
        if career not in ACADEMIC_DATA:
            return jsonify({'error': 'Carrera no encontrada'}), 404
            
        if semester not in ACADEMIC_DATA[career]:
            return jsonify({'error': 'Semestre no encontrado'}), 404
            
        courses = ACADEMIC_DATA[career][semester]
        return jsonify({
            "status": "success",
            "career": career,
            "semester": semester,
            "courses": courses
        })
    except Exception as e:
        return jsonify({"error": f"Error al obtener cursos: {str(e)}"}), 500

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint para obtener recomendaciones. 
    Es mejor usar POST para enviar datos estructurados (JSON).
    """
    data = request.get_json() # Obtener datos JSON de la solicitud

    # 1. Validar los datos recibidos
    carrera = data.get('career')
    semestre = data.get('semester')
    curso = data.get('course')

    if not carrera or not semestre or not curso:
        return jsonify({'error': 'Datos incompletos'}), 400

    try:
        # 2. Validar que la carrera y semestre existen en los datos
        available_courses = ACADEMIC_DATA.get(carrera, {}).get(semestre)
        if not available_courses:
            return jsonify({'error': 'Carrera o semestre no encontrado'}), 400
            
        if curso not in available_courses:
            return jsonify({'error': 'Curso no válido para esta carrera y semestre'}), 400

        # 3. Filtrar estudiantes de la misma carrera y semestre
        relevant_students = {
            sid: data for sid, data in GRADES_DATA.items()
            if data['carrera'] == carrera and data['semestre'] == semestre
        }
        
        if not relevant_students:
            return jsonify({'error': 'No hay datos de estudiantes para esta carrera y semestre'}), 404

        # 4. Crear vectores de estudiantes y calcular competencias
        student_vectors = create_student_vectors(relevant_students, available_courses)
        student_competence_scores = calculate_magnitudes(student_vectors)
        
        # 5. Obtener recomendaciones
        recommendations = recommend_resources(curso, RESOURCES_DATA, student_competence_scores)
        
        # 6. Formatear recomendaciones para la respuesta
        formatted_recommendations = []
        for title, data in recommendations:
            formatted_recommendations.append({
                "title": title,
                "type": data['type'],
                "link": data['link'],
                "score": round(data['score'], 2)
            })
        
        # 7. Devolver la respuesta
        return jsonify({
            "status": "success",
            "carrera": carrera,
            "semestre": semestre,
            "curso": curso,
            "recommendations": formatted_recommendations
        })

    except Exception as e:
        # 8. Manejo de errores
        return jsonify({"error": f"Error en el sistema de recomendación: {str(e)}"}), 500

@app.route('/api/documents/<path:filename>')
def serve_document(filename):
    """Endpoint para servir documentos PDF y otros archivos."""
    try:
        # Construir la ruta completa del archivo
        file_path = os.path.join(DOCUMENTS_FOLDER, filename)
        
        # Verificar que el archivo existe
        if not os.path.exists(file_path):
            return jsonify({"error": "Archivo no encontrado"}), 404
        
        # Verificar que el archivo está dentro de la carpeta de documentos (seguridad)
        if not os.path.abspath(file_path).startswith(os.path.abspath(DOCUMENTS_FOLDER)):
            return jsonify({"error": "Acceso denegado"}), 403
        
        # Determinar el tipo MIME basado en la extensión
        if filename.lower().endswith('.pdf'):
            mimetype = 'application/pdf'
        elif filename.lower().endswith('.doc'):
            mimetype = 'application/msword'
        elif filename.lower().endswith('.docx'):
            mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        else:
            mimetype = 'application/octet-stream'
        
        # Servir el archivo
        return send_file(file_path, mimetype=mimetype, as_attachment=False)
        
    except Exception as e:
        return jsonify({"error": f"Error al servir el archivo: {str(e)}"}), 500

@app.route('/api/documents/list')
def list_documents():
    """Endpoint para listar todos los documentos disponibles."""
    try:
        documents = []
        
        def scan_directory(directory, relative_path=""):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                relative_item_path = os.path.join(relative_path, item) if relative_path else item
                
                if os.path.isdir(item_path):
                    scan_directory(item_path, relative_item_path)
                else:
                    # Solo incluir archivos de documentos
                    if item.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
                        documents.append({
                            "filename": relative_item_path.replace("\\", "/"),  # Normalizar separadores
                            "name": item,
                            "size": os.path.getsize(item_path),
                            "type": os.path.splitext(item)[1].lower()
                        })
        
        scan_directory(DOCUMENTS_FOLDER)
        
        return jsonify({
            "status": "success",
            "documents": documents,
            "total": len(documents)
        })
        
    except Exception as e:
        return jsonify({"error": f"Error al listar documentos: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
