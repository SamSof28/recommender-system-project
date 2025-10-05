import numpy as np

# Importamos GRADES_DATA aquí para poder verificar el rol del recomendador
from data.mock_data import GRADES_DATA

def recommend_resources(target_course: str, all_resources: dict, student_competence: dict) -> list:
    """
    Recomienda recursos usando normalización y dando un trato especial a las
    recomendaciones de profesores.
    """
    course_resources = all_resources.get(target_course, [])
    if not course_resources:
        return []

    # --- PASO 1: Pre-cálculo de valores brutos ---
    resources_metrics = {}
    for resource in course_resources:
        title = resource['title']
        if title not in resources_metrics:
            resources_metrics[title] = {'data': resource, 'recommenders': []}
        resources_metrics[title]['recommenders'].append(resource['recommended_by'])

    if not resources_metrics:
        return []

    raw_metrics = {}
    
    # El valor más alto posible de competencia para un estudiante (ej. 3 materias con 5.0)
    # sqrt(5^2 + 5^2 + 5^2) = 8.66. Usamos un valor superior para los profesores.
    PROFESSOR_COMPETENCE_SCORE = 10.0

    for title, info in resources_metrics.items():
        recommenders = info['recommenders']
        
        # --- LÓGICA MEJORADA PARA COMPETENCIA ---
        total_competence = 0
        for rec_id in recommenders:
            # Verificamos si el recomendador es un profesor
            recommender_info = GRADES_DATA.get(rec_id, {})
            if recommender_info.get('role') == 'professor':
                total_competence += PROFESSOR_COMPETENCE_SCORE
            else:
                total_competence += student_competence.get(rec_id, 0)
        
        avg_competence = total_competence / len(recommenders) if recommenders else 0
        popularity = len(set(recommenders))
        
        raw_metrics[title] = {'competence': avg_competence, 'popularity': popularity}

    # --- PASO 2: Normalización (sin cambios) ---
    competence_values = [data['competence'] for data in raw_metrics.values()]
    popularity_values = [data['popularity'] for data in raw_metrics.values()]
    
    min_comp = min(competence_values)
    max_comp = max(competence_values)
    min_pop = min(popularity_values)
    max_pop = max(popularity_values)

    # --- PASO 3: Cálculo del score final (mejorado) ---
    recommendation_scores = {}
    w1_competence = 0.8
    w2_popularity = 0.2

    for title, metrics in raw_metrics.items():
        # Normalización mejorada para evitar división por cero
        norm_competence = 0.0
        if (max_comp - min_comp) > 0:
            norm_competence = (metrics['competence'] - min_comp) / (max_comp - min_comp)
        else:
            # Si solo hay un recurso, usar un valor base basado en la competencia absoluta
            # Escalar la competencia a un rango de 0-1 usando un valor de referencia
            reference_competence = 10.0  # Valor de referencia para profesores
            norm_competence = min(metrics['competence'] / reference_competence, 1.0)

        norm_popularity = 0.0
        if (max_pop - min_pop) > 0:
            norm_popularity = (metrics['popularity'] - min_pop) / (max_pop - min_pop)
        else:
            # Si solo hay un recurso, usar la popularidad absoluta normalizada
            # Un recurso recomendado por 3 personas = 0.6, por 1 persona = 0.2
            norm_popularity = min(metrics['popularity'] / 5.0, 1.0)
        
        normalized_score = (w1_competence * norm_competence) + (w2_popularity * norm_popularity)
        final_score = 1 + (normalized_score * 9)
        
        resource_data = resources_metrics[title]['data']
        recommendation_scores[title] = {
            'score': final_score,
            'type': resource_data['type'],
            'link': resource_data['link']
        }

    return sorted(recommendation_scores.items(), key=lambda item: item[1]['score'], reverse=True)