#Base de datos de cursos por carrera y semestre
# import pandas as pd

ACADEMIC_DATA = {
    "Ingenieria de Sistemas": {
        1: ["Pensamiento Algoritmico", "Algebra y Trigonometria", "Analisis Geometrico", "Introduccion a la Ing. de Sistemas"],
        2: ["Algebra Lineal", "Calculo Diferencual", "Procesos de Negocios", "Algoritmos y Programación Orientada a Objetos", "Matematicas Discretas"],
    },
    "Derecho": {
        1: ["Introduccion al Derecho", "Derecho Romano", "Teoria del Estado", "Personas", "Expresion Oral y Escrita"],
        2: ["Teoria de la Constitucion", "Bienes I: Derechos Patrimoniales", "Teoria de las relaciones del Trabajo", "Analisis del Discurso y Argumentacion Juridica", "Fundamentos del Derecho Penal", "Metodologias Activas para la Compresion de Problemas"]
    }
}   

# --- DATOS DE ESTUDIANTES Y PROFESORES CON ROLES Y VARIEDAD ---
GRADES_DATA = {
    # --- PROFESORES (Rol especial para darles máxima competencia) ---
    'Gildardo Orrego': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'role': 'professor', 'grades': {'Matematicas Discretas': 5.0}},
    'Jose Jesus Torres': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'role': 'professor', 'grades': {'Algebra Lineal': 5.0}},

    # --- ESTUDIANTES DE ALTO RENDIMIENTO (Notas: 4.6 - 5.0) ---
    'Estudiante_Top_01': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.9, 'Calculo Diferencial': 4.8, 'Matematicas Discretas': 4.9}},
    'Estudiante_Top_02': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.8, 'Calculo Diferencial': 4.9, 'Matematicas Discretas': 4.8}},
    'Estudiante_Top_03': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.7, 'Calculo Diferencial': 4.6, 'Matematicas Discretas': 4.7}},
    'Estudiante_Top_04': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 5.0, 'Calculo Diferencial': 4.8, 'Matematicas Discretas': 4.6}},

    # --- ESTUDIANTES DE RENDIMIENTO MEDIO (Notas: 3.8 - 4.5) ---
    'Estudiante_Med_01': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.0, 'Calculo Diferencial': 3.8, 'Matematicas Discretas': 4.1}},
    'Estudiante_Med_02': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.5, 'Calculo Diferencial': 4.2, 'Matematicas Discretas': 4.0}},
    'Estudiante_Med_03': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.2, 'Calculo Diferencial': 4.0, 'Matematicas Discretas': 4.3}},
    'Estudiante_Med_04': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.9, 'Calculo Diferencial': 4.1, 'Matematicas Discretas': 4.0}},
    'Estudiante_Med_05': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.3, 'Calculo Diferencial': 4.2, 'Matematicas Discretas': 4.1}},
    'Estudiante_Med_06': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.1, 'Calculo Diferencial': 3.9, 'Matematicas Discretas': 4.0}},

    # --- ESTUDIANTES DE RENDIMIENTO REGULAR (Notas: 3.0 - 3.7) ---
    'Estudiante_Reg_01': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.5, 'Calculo Diferencial': 3.0, 'Matematicas Discretas': 3.2}},
    'Estudiante_Reg_02': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.0, 'Calculo Diferencial': 3.1, 'Matematicas Discretas': 3.3}},
    'Estudiante_Reg_03': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.7, 'Calculo Diferencial': 3.5, 'Matematicas Discretas': 3.6}},
    'Estudiante_Reg_04': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.2, 'Calculo Diferencial': 3.4, 'Matematicas Discretas': 3.1}},
    'Estudiante_Reg_05': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.6, 'Calculo Diferencial': 3.3, 'Matematicas Discretas': 3.5}},
}


#Recursos de estudio con su tipo y enlace
RESOURCES_DATA: dict[str, list[dict[str, str]]] = {
    "Algebra Lineal": [
        # Recurso MUY ALTO: Recomendado por un profesor y los mejores estudiantes.
        {"type": "libro", "title": 'FUNDAMENTOS DE ÁLGEBRA LINEAL (Ron Larson)', "link": "https://recommender-api-ffpd.onrender.com/api/documents/Ingeniería de Sistemas/algebra_lineal/Fundamentos_de_álgebra_lineal-Ron_Larson.pdf", 'recommended_by': 'Jose Jesus Torres'},
        {"type": "libro", "title": 'FUNDAMENTOS DE ÁLGEBRA LINEAL (Ron Larson)', "link": "https://recommender-api-ffpd.onrender.com/api/documents/Ingeniería de Sistemas/algebra_lineal/Fundamentos_de_álgebra_lineal-Ron_Larson.pdf", 'recommended_by': 'Estudiante_Top_01'},
        {"type": "libro", "title": 'FUNDAMENTOS DE ÁLGEBRA LINEAL (Ron Larson)', "link": "https://recommender-api-ffpd.onrender.com/api/documents/Ingeniería de Sistemas/algebra_lineal/Fundamentos_de_álgebra_lineal-Ron_Larson.pdf", 'recommended_by': 'Estudiante_Top_04'},

        # Recurso ALTO: Popular entre estudiantes de alto y medio rendimiento.
        {"type": "video", "title": 'La Esencia del Álgebra Lineal (3Blue1Brown)', "link": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", 'recommended_by': 'Estudiante_Top_01'},
        {"type": "video", "title": 'La Esencia del Álgebra Lineal (3Blue1Brown)', "link": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", 'recommended_by': 'Estudiante_Top_02'},
        {"type": "video", "title": 'La Esencia del Álgebra Lineal (3Blue1Brown)', "link": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", 'recommended_by': 'Estudiante_Med_02'},

        # Recurso MEDIO: Popular entre estudiantes de rendimiento medio.
        {"type": "video", "title": 'Curso de Matrices y Determinantes', "link": "https://www.youtube.com/watch?v=RJ96S2Pt3qU", 'recommended_by': 'Estudiante_Top_03'},
        {"type": "video", "title": 'Curso de Matrices y Determinantes', "link": "https://www.youtube.com/watch?v=RJ96S2Pt3qU", 'recommended_by': 'Estudiante_Med_03'},
        {"type": "video", "title": 'Curso de Matrices y Determinantes', "link": "https://www.youtube.com/watch?v=RJ96S2Pt3qU", 'recommended_by': 'Estudiante_Med_05'},

    ],

    "Matematicas Discretas": [
        {"type": "repositorio", "title": 'Matemáticas Discretas - Recursos Completos', "link": "https://github.com/OrregoGildardo/MatematicasDiscretas/", 'recommended_by': 'Gildardo Orrego'},
        {"type": "repositorio", "title": 'Matemáticas Discretas - Recursos Completos', "link": "https://github.com/OrregoGildardo/MatematicasDiscretas/", 'recommended_by': 'Estudiante_Top_01'},
        {"type": "repositorio", "title": 'Matemáticas Discretas - Recursos Completos', "link": "https://github.com/OrregoGildardo/MatematicasDiscretas/", 'recommended_by': 'Estudiante_Top_02'}
    ]
}


