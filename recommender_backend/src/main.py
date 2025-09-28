# python src/main.py

import sys
sys.path.append('.')

from data.mock_data import ACADEMIC_DATA, RESOURCES_DATA, GRADES_DATA
from core.algebra import create_student_vectors, calculate_magnitudes
from core.recommender import recommend_resources

def run_console_app():
    """Función principal que ejecuta la aplicación de consola."""
    print("🎓 ¡Bienvenido al Sistema de Recomendación de Recursos de Estudio! 🎓")
    
    try:
        career = input("Ingresa tu carrera (Ej: Ingenieria de Sistemas): ")
        semester = int(input(f"Ingresa el semestre (Ej: 1, 2): "))
        
        available_courses = ACADEMIC_DATA.get(career, {}).get(semester)
        if not available_courses:
            print("Error: Carrera o semestre no encontrado.")
            return

        print("Cursos disponibles:", ", ".join(available_courses))
        target_course = input("¿Para qué curso necesitas recomendaciones?: ")

        if target_course not in available_courses:
            print("Error: Curso no válido.")
            return
            
    except ValueError:
        print("Error: El semestre debe ser un número.")
        return

    print("\n------------------------------------------------------")
    print(f"Buscando recomendaciones para '{target_course}'...")

    # --- ÁLGEBRA LINEAL: Crear vectores y calcular su magnitud ---
    # Filtramos estudiantes de la misma carrera y semestre
    relevant_students = {
        sid: data for sid, data in GRADES_DATA.items()
        if data['carrera'] == career and data['semestre'] == semester
    }
    
    if not relevant_students:
        print(f"No hay datos de estudiantes pasados para el semestre {semester} de {career}.")
        return

    student_vectors = create_student_vectors(relevant_students, available_courses)
    student_competence_scores = calculate_magnitudes(student_vectors)
    
    print("Análisis completado: Se calculó el 'Índice de Competencia' de estudiantes pasados usando la magnitud de sus vectores de calificación.")

    # --- OPTIMIZACIÓN: Obtener y rankear las recomendaciones ---
    recommendations = recommend_resources(target_course, RESOURCES_DATA, student_competence_scores)

    # --- MOSTRAR RESULTADOS ---
    print("\n------------------- TUS RECOMENDACIONES -------------------")
    if recommendations:
        for i, (title, data) in enumerate(recommendations):
            print(f"{i+1}. [{data['type']}] {title}")
            print(f"   Enlace: {data['link']} (Score de Relevancia: {data['score']:.2f})")
    else:
        print(f"Lo sentimos, no se encontraron recursos para '{target_course}'.")
    print("-----------------------------------------------------------\n")


if __name__ == "__main__":
    run_console_app()