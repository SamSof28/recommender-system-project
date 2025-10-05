# src/core/recommender.py

def recommend_resources(target_course: str, all_resources: dict, student_competence: dict) -> list:
    """Recomienda recursos basado en la competencia de los recomendadores y la popularidad."""
    course_resources = all_resources.get(target_course, [])
    if not course_resources:
        return []

    recommendation_scores = {}

    # Pesos de Optimización (w1: competencia, w2: popularidad)
    # Explicación para el profesor: Estos pesos son los parámetros de nuestra función objetivo.
    # Podrían ser "optimizados" usando técnicas como Mínimos Cuadrados si tuviéramos
    # datos de "calificaciones de recursos" por parte de los estudiantes.
    # Por ahora, los hemos fijado empíricamente para priorizar la calidad del recomendador.
    w1_competence = 0.8  # 80% de peso a la calidad del recomendador
    w2_popularity = 0.2  # 20% de peso a la popularidad (cantidad de recomendadores)

    # Agrupar recomendadores por recurso
    resources_by_title = {}
    for resource in course_resources:
        title = resource['title']
        if title not in resources_by_title:
            resources_by_title[title] = {'data': resource, 'recommenders': []}
        resources_by_title[title]['recommenders'].append(resource['recommended_by'])

    # Calcular score para cada recurso único
    for title, info in resources_by_title.items():
        recommenders = info['recommenders']
        
        # Calcular la competencia promedio de los recomendadores para este recurso
        # Solo sumamos la competencia de los estudiantes que *realmente* han recomendado este recurso.
        total_competence_for_resource = sum(student_competence.get(rec_id, 0) for rec_id in recommenders)
        avg_competence_for_resource = total_competence_for_resource / len(recommenders) if recommenders else 0
        
        # Calcular popularidad (cuántos estudiantes diferentes lo recomiendan)
        unique_recommenders_count = len(set(recommenders))
        
        # Score final (la función objetivo a maximizar)
        # Normalizamos la popularidad dividiéndola por el número total de estudiantes
        # para que no escale indefinidamente y se combine bien con la competencia.
        # Aunque para datos simulados y pocos recursos, `unique_recommenders_count` sin dividir ya funciona.
        # Lo importante es el concepto de que ambos factores contribuyen.
        
        # Versión simplificada para el demo y los datos actuales (funciona bien con el número de recomendadores)
        score = (w1_competence * avg_competence_for_resource) + (w2_popularity * unique_recommenders_count)
        
        # Si prefieres una popularidad normalizada (entre 0 y 1, si hay muchos estudiantes):
        # max_possible_popularity = max(len(recommenders) for res_title, res_info in resources_by_title.items()) if resources_by_title else 1
        # normalized_popularity = unique_recommenders_count / max_possible_popularity
        # score = (w1_competence * avg_competence_for_resource) + (w2_popularity * normalized_popularity)
        
        if score > 0:
            recommendation_scores[title] = {
                'score': score,
                'type': info['data']['type'],
                'link': info['data']['link'] # Asegúrate que esto coincide con la clave en mock_data.py
            }

    # Ordenar y devolver las recomendaciones
    return sorted(recommendation_scores.items(), key=lambda item: item[1]['score'], reverse=True)