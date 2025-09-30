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
    'Estudiante_A': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.75, 'Calculo Diferencial': 4.4}},
    'Estudiante_B': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4, 'Calculo Diferencial': 4.25}},
    'Estudiante_C': {'carrera': 'Ingenieria de Sistemas', 'semestre': 2, 'grades': {'Algebra Lineal': 4.5, 'Calculo Diferencial': 4.75}},
}

#Recursos de estudio con su tipo y enlace
RESOURCES_DATA: dict[str, list[dict[str, str]]] = {
    "Algebra Lineal": [
        {"type": "video", "title": 'Introducción al Algebra Lineal', "link": "https://youtu.be/0Ndnzx6AyaA?si=Qkd4d8JkHb6I8_bg", 'recommended_by': 'Estudiante_A'},
        {"type": "video", "title": 'Curso de Matrices y Determinantes', "link": "https://www.youtube.com/watch?v=RJ96S2Pt3qU&list=PLeySRPnY35dEr2XewNdOjOl7Ft0tLIlKI", 'recommended_by': 'Estudiante_C'},
        {"type": "libro", "title": 'FUNDAMENTOS DE ÁLGEBRA LINEAL', "link": "https://recommender-api-ffpd.onrender.com/api/documents/Ingeniería de Sistemas/algebra_lineal/Fundamentos_de_álgebra_lineal-Ron_Larson.pdf", 'recommended_by': 'Estudiante_A'},
        
    ]
}


