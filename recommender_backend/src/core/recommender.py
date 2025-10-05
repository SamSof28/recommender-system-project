# src/core/recommender.py
import numpy as np

def recommend_resources(target_course: str, all_resources: dict, student_competence: dict) -> list:
    """
    Recomienda recursos usando normalización para balancear la competencia
    de los recomendadores y la popularidad del recurso.
    """
    course_resources = all_resources.get(target_course, [])
    if not course_resources:
        return []

    # --- PASO 1: Pre-cálculo de valores brutos de competencia y popularidad ---
    
    # Agrupar recomendadores y calcular métricas brutas para cada recurso
    resources_metrics = {}
    for resource in course_resources:
        title = resource['title']
        if title not in resources_metrics:
            resources_metrics[title] = {'data': resource, 'recommenders': []}
        resources_metrics[title]['recommenders'].append(resource['recommended_by'])

    if not resources_metrics:
        return []

    # Calcular la competencia promedio y la popularidad para cada título
    raw_metrics = {}
    for title, info in resources_metrics.items():
        recommenders = info['recommenders']
        
        # Competencia promedio de los recomendadores para este recurso
        avg_competence = sum(student_competence.get(rec_id, 0) for rec_id in recommenders) / len(recommenders) if recommenders else 0
        
        # Popularidad (número de estudiantes únicos que lo recomiendan)
        popularity = len(set(recommenders))
        
        raw_metrics[title] = {'competence': avg_competence, 'popularity': popularity}

    # --- PASO 2: Normalización de las métricas a una escala de 0 a 1 ---
    
    # Extraer todos los valores de competencia y popularidad para encontrar los rangos
    competence_values = [data['competence'] for data in raw_metrics.values()]
    popularity_values = [data['popularity'] for data in raw_metrics.values()]
    
    min_comp = min(competence_values)
    max_comp = max(competence_values)
    min_pop = min(popularity_values)
    max_pop = max(popularity_values)

    # --- PASO 3: Cálculo del score final con valores normalizados ---
    
    recommendation_scores = {}
    
    # Pesos de Optimización (se mantienen igual, pero ahora actúan sobre valores escalados)
    w1_competence = 0.8
    w2_popularity = 0.2

    for title, metrics in raw_metrics.items():
        # Normalizar competencia
        # Se maneja el caso donde todos los valores son iguales para evitar división por cero
        norm_competence = 0.0
        if (max_comp - min_comp) > 0:
            norm_competence = (metrics['competence'] - min_comp) / (max_comp - min_comp)

        # Normalizar popularidad
        norm_popularity = 0.0
        if (max_pop - min_pop) > 0:
            norm_popularity = (metrics['popularity'] - min_pop) / (max_pop - min_pop)
        
        # Función Objetivo con valores normalizados
        normalized_score = (w1_competence * norm_competence) + (w2_popularity * norm_popularity)
        
        # Escalar el resultado final a un rango más amigable (ej. de 1 a 10)
        # Esto le da al usuario una puntuación final mucho más intuitiva.
        final_score = 1 + (normalized_score * 9)
        
        resource_data = resources_metrics[title]['data']
        recommendation_scores[title] = {
            'score': final_score,
            'type': resource_data['type'],
            'link': resource_data['link']
        }

    # Ordenar y devolver las recomendaciones
    return sorted(recommendation_scores.items(), key=lambda item: item[1]['score'], reverse=True)