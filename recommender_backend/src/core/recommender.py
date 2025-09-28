def recommend_resources(target_course: str, all_resources: dict, student_competence: dict) -> list:
    """Recomienda recursos basado en la competencia de los recomendadores y la popularidad."""
    course_resources = all_resources.get(target_course, [])
    if not course_resources:
        return []

    recommendation_scores = {}

    # Pesos de Optimización (w1: competencia, w2: popularidad)
    w1_competence = 0.8  # 80% de peso a la calidad del recomendador 
    w2_popularity = 0.2 # 20% de peso a la popularidad (cantidad de recomendadores)

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
        
        # Calcular la competencia promedio de los recomendadores
        total_competence = sum(student_competence.get(recomend, 0) for recomend in recommenders)
        avg_competence = total_competence / len(recommenders) if recommenders else 0
        
        # Calcular popularidad
        popularity = len(recommenders)
        
        # Score final (la función objetivo a maximizar)
        score = (w1_competence * avg_competence) + (w2_popularity * popularity)
        
        if score > 0:
            recommendation_scores[title] = {
                'score': score,
                'type': info['data']['type'],
                'link': info['data']['link']
            }

    # Ordenar y devolver las recomendaciones
    return sorted(recommendation_scores.items(), key=lambda item: item[1]['score'], reverse=True)