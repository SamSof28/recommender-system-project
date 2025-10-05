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

GRADES_DATA = {
    'Estudiante_IS_01': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.7, 'Calculo Diferencial': 4.5, 'Matematicas Discretas': 4.8}},
    'Estudiante_IS_02': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.0, 'Calculo Diferencial': 3.8, 'Matematicas Discretas': 4.1}},
    'Estudiante_IS_03': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.5, 'Calculo Diferencial': 4.7, 'Matematicas Discretas': 4.0}},
    'Estudiante_IS_04': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.5, 'Calculo Diferencial': 3.0, 'Matematicas Discretas': 3.2}},
    'Estudiante_IS_05': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.9, 'Calculo Diferencial': 4.8, 'Matematicas Discretas': 4.9}},
    'Estudiante_IS_06': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.2, 'Calculo Diferencial': 4.0, 'Matematicas Discretas': 4.3}},
    'Estudiante_IS_07': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.9, 'Calculo Diferencial': 3.7, 'Matematicas Discretas': 3.5}},
    'Estudiante_IS_08': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.1, 'Calculo Diferencial': 4.2, 'Matematicas Discretas': 4.0}},
    'Estudiante_IS_09': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.6, 'Calculo Diferencial': 4.5, 'Matematicas Discretas': 4.7}},
    'Estudiante_IS_10': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.0, 'Calculo Diferencial': 3.1, 'Matematicas Discretas': 3.3}},
    'Estudiante_IS_11': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.3, 'Calculo Diferencial': 4.2, 'Matematicas Discretas': 4.1}},
    'Estudiante_IS_12': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.8, 'Calculo Diferencial': 4.9, 'Matematicas Discretas': 4.8}},
    'Estudiante_IS_13': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.7, 'Calculo Diferencial': 3.5, 'Matematicas Discretas': 3.9}},
    'Estudiante_IS_14': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.4, 'Calculo Diferencial': 4.3, 'Matematicas Discretas': 4.5}},
    'Estudiante_IS_15': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.0, 'Calculo Diferencial': 4.1, 'Matematicas Discretas': 4.2}},
    'Estudiante_IS_16': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.6, 'Calculo Diferencial': 4.7, 'Matematicas Discretas': 4.6}},
    'Estudiante_IS_17': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 3.2, 'Calculo Diferencial': 3.0, 'Matematicas Discretas': 3.1}},
    'Estudiante_IS_18': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.0, 'Calculo Diferencial': 3.9, 'Matematicas Discretas': 4.0}},
    'Estudiante_IS_19': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.3, 'Calculo Diferencial': 4.4, 'Matematicas Discretas': 4.3}},
    'Estudiante_IS_20': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.7, 'Calculo Diferencial': 4.6, 'Matematicas Discretas': 4.7}},
    'Gildardo Orrego': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Matematicas Discretas': 5}},
}

#Recursos de estudio con su tipo y enlace
RESOURCES_DATA: dict[str, list[dict[str, str]]] = {
    "Algebra Lineal": [
        {"type": "video", "title": 'Introducción al Algebra Lineal', "link": "https://youtu.be/0Ndnzx6AyaA?si=Qkd4d8JkHb6I8_bg", 'recommended_by': 'Estudiante_A'},
        {"type": "video", "title": 'Curso de Matrices y Determinantes', "link": "https://www.youtube.com/watch?v=RJ96S2Pt3qU&list=PLeySRPnY35dEr2XewNdOjOl7Ft0tLIlKI", 'recommended_by': 'Estudiante_C'},
        {"type": "libro", "title": 'FUNDAMENTOS DE ÁLGEBRA LINEAL', "link": "https://recommender-api-ffpd.onrender.com/api/documents/Ingeniería de Sistemas/algebra_lineal/Fundamentos_de_álgebra_lineal-Ron_Larson.pdf", 'recommended_by': 'Estudiante_A'},
    ],
    "Matematicas Discretas": [
        {"type": "repositorio", "title": 'Matemáticas Discretas - Recursos Completos', "link": "https://github.com/OrregoGildardo/MatematicasDiscretas/", 'recommended_by': 'Gildardo Orrego'},
    ]
}


