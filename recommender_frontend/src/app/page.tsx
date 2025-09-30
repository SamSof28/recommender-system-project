"use client";

import { useState, useEffect } from "react";
import RecommendationForm from "./components/RecommendationForm";
import RecommendationResults from "./components/RecommendationResults";
import LoadingSpinner from "./components/LoadingSpinner";

interface Recommendation {
  title: string;
  type: string;
  link: string;
  score: number;
}

export default function Home() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRecommendations = async (formData: {
    career: string;
    semester: number;
    course: string;
  }) => {
    setLoading(true);
    setError(null);
    setRecommendations([]);

    try {
      const response = await fetch(
        "https://recommender-api-ffpd.onrender.com/api/recommendations",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      if (!response.ok) {
        throw new Error("Error al obtener recomendaciones");
      }

      const data = await response.json();

      if (data.status === "success") {
        setRecommendations(data.recommendations);
      } else {
        throw new Error(data.error || "Error desconocido");
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800">
      {/* Header */}
      <header className="border-b border-slate-200 dark:border-slate-700 bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">🎓</span>
              </div>
              <h1 className="text-xl font-semibold text-slate-900 dark:text-white">
                Sistema de Recomendación Académico
              </h1>
            </div>
            <div className="text-sm text-slate-600 dark:text-slate-400">
              Basado en Álgebra Lineal
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-slate-900 dark:text-white mb-4">
            Encuentra los mejores recursos de estudio
          </h2>
          <p className="text-xl text-slate-600 dark:text-slate-400 max-w-3xl mx-auto">
            Nuestro sistema utiliza algoritmos de Álgebra Lineal y Optimización
            para recomendarte recursos académicos personalizados basados en tu
            perfil de estudiante.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Formulario */}
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-700 p-8">
            <h3 className="text-2xl font-semibold text-slate-900 dark:text-white mb-6">
              Configura tu perfil académico
            </h3>
            <RecommendationForm onSubmit={handleRecommendations} />
          </div>

          {/* Resultados */}
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-700 p-8">
            <h3 className="text-2xl font-semibold text-slate-900 dark:text-white mb-6">
              Tus recomendaciones
            </h3>

            {loading && <LoadingSpinner />}

            {error && (
              <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-4">
                <p className="text-red-800 dark:text-red-200 text-sm">
                  {error}
                </p>
              </div>
            )}

            {recommendations.length > 0 && (
              <RecommendationResults recommendations={recommendations} />
            )}

            {!loading && !error && recommendations.length === 0 && (
              <div className="text-center py-12">
                <div className="w-16 h-16 bg-slate-100 dark:bg-slate-700 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl">📚</span>
                </div>
                <p className="text-slate-600 dark:text-slate-400">
                  Completa el formulario para obtener recomendaciones
                  personalizadas
                </p>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200 dark:border-slate-700 bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center text-slate-600 dark:text-slate-400">
            <p>
              Sistema de Recomendación Académico • Desarrollado con Next.js y
              Álgebra Lineal
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
