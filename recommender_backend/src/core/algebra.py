import numpy as np

def create_student_vectors(students_data: dict, courses: list[str]) -> dict:
    """Crea la matriz Estudiante vs Curso"""
    student_vectors = {}
    for student_id, data in students_data.items():
        vector = np.zeros(len(courses))
        for course_name, grade in data['grades'].items():
            if course_name in courses:
                index = courses.index(course_name)
                vector[index] = grade
        student_vectors[student_id] = vector
    return student_vectors

def calculate_magnitudes(student_vectors: dict) -> dict:
    """
    Calcula la magnitud (norma L2) de cada vector estudiantil.
    Este es nuestro "Índice de Competencia".
    """
    student_magnitudes = {}
    for student_id, vector in student_vectors.items():
        magnitude = np.linalg.norm(vector) 
        student_magnitudes[student_id] = magnitude
    return student_magnitudes




