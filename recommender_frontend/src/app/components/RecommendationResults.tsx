'use client';

interface Recommendation {
  title: string;
  type: string;
  link: string;
  score: number;
}

interface RecommendationResultsProps {
  recommendations: Recommendation[];
}

export default function RecommendationResults({ recommendations }: RecommendationResultsProps) {
  const getTypeIcon = (type: string) => {
    switch (type.toLowerCase()) {
      case 'video':
        return '🎥';
      case 'libro':
      case 'book':
        return '📖';
      case 'ejercicios':
      case 'exercise':
        return '📝';
      case 'tutorial':
        return '🎯';
      case 'artículo':
      case 'article':
        return '📄';
      default:
        return '📚';
    }
  };

  const getScoreColor = (score: number) => {
    if (score >= 8) return 'text-green-600 dark:text-green-400';
    if (score >= 6) return 'text-yellow-600 dark:text-yellow-400';
    return 'text-orange-600 dark:text-orange-400';
  };

  const getScoreLabel = (score: number) => {
    if (score >= 8) return 'Excelente';
    if (score >= 6) return 'Bueno';
    return 'Regular';
  };

  return (
    <div className="space-y-4">
      <div className="text-center mb-6">
        <h4 className="text-lg font-semibold text-slate-900 dark:text-white mb-2">
          Recomendaciones personalizadas
        </h4>
        <p className="text-sm text-slate-600 dark:text-slate-400">
          {recommendations.length} recursos encontrados, ordenados por relevancia
        </p>
      </div>

      <div className="space-y-3">
        {recommendations.map((rec, index) => (
          <div
            key={index}
            className="bg-slate-50 dark:bg-slate-700 rounded-lg border border-slate-200 dark:border-slate-600 p-4 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="flex items-center space-x-3">
                <span className="text-2xl">{getTypeIcon(rec.type)}</span>
                <div>
                  <h5 className="font-medium text-slate-900 dark:text-white text-sm">
                    {rec.title}
                  </h5>
                  <p className="text-xs text-slate-600 dark:text-slate-400 capitalize">
                    {rec.type}
                  </p>
                </div>
              </div>
              <div className="text-right">
                <div className={`text-sm font-semibold ${getScoreColor(rec.score)}`}>
                  {rec.score.toFixed(1)}
                </div>
                <div className={`text-xs ${getScoreColor(rec.score)}`}>
                  {getScoreLabel(rec.score)}
                </div>
              </div>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex-1 bg-slate-200 dark:bg-slate-600 rounded-full h-2 mr-3">
                <div
                  className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full transition-all duration-500"
                  style={{ width: `${(rec.score / 10) * 100}%` }}
                ></div>
              </div>
              <a
                href={rec.link}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center space-x-1 text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm font-medium transition-colors"
              >
                <span>Acceder</span>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        ))}
      </div>

      {/* Información adicional */}
      <div className="mt-6 bg-slate-50 dark:bg-slate-700 rounded-lg p-4">
        <div className="flex items-start space-x-3">
          <div className="flex-shrink-0">
            <div className="w-8 h-8 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center">
              <span className="text-blue-600 dark:text-blue-400 text-sm">ℹ️</span>
            </div>
          </div>
          <div>
            <h5 className="font-medium text-slate-900 dark:text-white text-sm mb-1">
              ¿Cómo se calculan las recomendaciones?
            </h5>
            <p className="text-xs text-slate-600 dark:text-slate-400">
              Nuestro algoritmo utiliza <strong>Álgebra Lineal</strong> para analizar el rendimiento 
              de estudiantes con perfiles similares al tuyo. Combina la competencia promedio 
              de los recomendadores con la popularidad de cada recurso para generar un score de relevancia.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
