"use client";

import { useState } from "react";
import PDFViewer from "./PDFViewer";

interface Recommendation {
  title: string;
  type: string;
  link: string;
  score: number;
}

interface RecommendationResultsProps {
  recommendations: Recommendation[];
}

export default function RecommendationResults({
  recommendations,
}: RecommendationResultsProps) {
  const [selectedPDF, setSelectedPDF] = useState<{
    url: string;
    title: string;
  } | null>(null);
  const getTypeIcon = (type: string) => {
    switch (type.toLowerCase()) {
      case "video":
        return "🎥";
      case "libro":
      case "book":
        return "📖";
      case "ejercicios":
      case "exercise":
        return "📝";
      case "tutorial":
        return "🎯";
      case "artículo":
      case "article":
        return "📄";
      case "repositorio":
      case "github":
        return "💻";
      case "presentacion":
      case "slides":
        return "📊";
      case "ejercicios_practicos":
      case "practice":
        return "🔧";
      case "examen":
      case "quiz":
        return "📋";
      default:
        return "📚";
    }
  };

  const getScoreColor = (score: number) => {
    if (score >= 8) return "text-green-600 dark:text-green-400";
    if (score >= 6) return "text-yellow-600 dark:text-yellow-400";
    return "text-orange-600 dark:text-orange-400";
  };

  const getScoreLabel = (score: number) => {
    if (score >= 8) return "Excelente";
    if (score >= 6) return "Bueno";
    return "Regular";
  };

  const getTypeColor = (type: string) => {
    switch (type.toLowerCase()) {
      case "video":
        return "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200";
      case "libro":
      case "book":
        return "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200";
      case "repositorio":
      case "github":
        return "bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-200";
      case "ejercicios":
      case "exercise":
      case "ejercicios_practicos":
      case "practice":
        return "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200";
      case "tutorial":
        return "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200";
      case "artículo":
      case "article":
        return "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200";
      case "presentacion":
      case "slides":
        return "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200";
      case "examen":
      case "quiz":
        return "bg-pink-100 text-pink-800 dark:bg-pink-900 dark:text-pink-200";
      default:
        return "bg-slate-100 text-slate-800 dark:bg-slate-900 dark:text-slate-200";
    }
  };

  const getTypeLabel = (type: string) => {
    switch (type.toLowerCase()) {
      case "video":
        return "Video";
      case "libro":
      case "book":
        return "Libro PDF";
      case "repositorio":
      case "github":
        return "Repositorio";
      case "ejercicios":
      case "exercise":
        return "Ejercicios";
      case "ejercicios_practicos":
      case "practice":
        return "Práctica";
      case "tutorial":
        return "Tutorial";
      case "artículo":
      case "article":
        return "Artículo";
      case "presentacion":
      case "slides":
        return "Presentación";
      case "examen":
      case "quiz":
        return "Examen";
      default:
        return type.charAt(0).toUpperCase() + type.slice(1);
    }
  };

  return (
    <div className="space-y-4">
      <div className="text-center mb-6">
        <h4 className="text-lg font-semibold text-slate-900 dark:text-white mb-2">
          Recomendaciones personalizadas
        </h4>
        <p className="text-sm text-slate-600 dark:text-slate-400">
          {recommendations.length} recursos encontrados, ordenados por
          relevancia
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
                  <span
                    className={`inline-block px-2 py-1 rounded-full text-xs font-medium ${getTypeColor(
                      rec.type
                    )}`}
                  >
                    {getTypeLabel(rec.type)}
                  </span>
                </div>
              </div>
              <div className="text-right">
                <div
                  className={`text-sm font-semibold ${getScoreColor(
                    rec.score
                  )}`}
                >
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
              {rec.type === "libro" || rec.type === "book" ? (
                <button
                  onClick={() =>
                    setSelectedPDF({ url: rec.link, title: rec.title })
                  }
                  className="inline-flex items-center space-x-1 text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm font-medium transition-colors"
                >
                  <span>Ver PDF</span>
                  <svg
                    className="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    />
                  </svg>
                </button>
              ) : (
                <a
                  href={rec.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center space-x-1 text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm font-medium transition-colors"
                >
                  <span>
                    {rec.type === "repositorio" || rec.type === "github"
                      ? "Ver Repositorio"
                      : rec.type === "video"
                      ? "Ver Video"
                      : "Acceder"}
                  </span>
                  <svg
                    className="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                    />
                  </svg>
                </a>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Información adicional */}
      <div className="mt-6 bg-slate-50 dark:bg-slate-700 rounded-lg p-4">
        <div className="flex items-start space-x-3">
          <div className="flex-shrink-0">
            <div className="w-8 h-8 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center">
              <span className="text-blue-600 dark:text-blue-400 text-sm">
                ℹ️
              </span>
            </div>
          </div>
          <div>
            <h5 className="font-medium text-slate-900 dark:text-white text-sm mb-1">
              ¿Cómo se calculan las recomendaciones?
            </h5>
            <p className="text-xs text-slate-600 dark:text-slate-400">
              Nuestro algoritmo utiliza <strong>Álgebra Lineal</strong> para
              analizar el rendimiento de estudiantes con perfiles similares al
              tuyo. Combina la competencia promedio de los recomendadores con la
              popularidad de cada recurso para generar un score de relevancia.
            </p>
          </div>
        </div>
      </div>

      {/* PDF Viewer Modal */}
      {selectedPDF && (
        <PDFViewer
          url={selectedPDF.url}
          title={selectedPDF.title}
          onClose={() => setSelectedPDF(null)}
        />
      )}
    </div>
  );
}
