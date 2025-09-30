"use client";

import { useState, useEffect } from "react";
import { API_ENDPOINTS } from "../config/api";

interface FormData {
  career: string;
  semester: number;
  course: string;
}

interface RecommendationFormProps {
  onSubmit: (data: FormData) => void;
}

export default function RecommendationForm({
  onSubmit,
}: RecommendationFormProps) {
  const [careers, setCareers] = useState<string[]>([]);
  const [semesters, setSemesters] = useState<number[]>([]);
  const [courses, setCourses] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState<FormData>({
    career: "",
    semester: 0,
    course: "",
  });

  // Cargar carreras al montar el componente
  useEffect(() => {
    const fetchCareers = async () => {
      try {
        const response = await fetch(API_ENDPOINTS.CAREERS);
        const data = await response.json();
        if (data.status === "success") {
          setCareers(data.careers);
        }
      } catch (error) {
        console.error("Error al cargar carreras:", error);
      }
    };
    fetchCareers();
  }, []);

  // Cargar semestres cuando se selecciona una carrera
  useEffect(() => {
    if (formData.career) {
      const fetchSemesters = async () => {
        try {
          const response = await fetch(
            API_ENDPOINTS.SEMESTERS(formData.career)
          );
          const data = await response.json();
          if (data.status === "success") {
            setSemesters(data.semesters);
            // Reset semester y course cuando cambia la carrera
            setFormData((prev) => ({ ...prev, semester: 0, course: "" }));
            setCourses([]);
          }
        } catch (error) {
          console.error("Error al cargar semestres:", error);
        }
      };
      fetchSemesters();
    }
  }, [formData.career]);

  // Cargar cursos cuando se selecciona carrera y semestre
  useEffect(() => {
    if (formData.career && formData.semester) {
      const fetchCourses = async () => {
        try {
          const response = await fetch(
            API_ENDPOINTS.COURSES(formData.career, formData.semester)
          );
          const data = await response.json();
          if (data.status === "success") {
            setCourses(data.courses);
            // Reset course cuando cambia el semestre
            setFormData((prev) => ({ ...prev, course: "" }));
          }
        } catch (error) {
          console.error("Error al cargar cursos:", error);
        }
      };
      fetchCourses();
    }
  }, [formData.career, formData.semester]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.career || !formData.semester || !formData.course) {
      return;
    }

    setLoading(true);
    try {
      await onSubmit(formData);
    } finally {
      setLoading(false);
    }
  };

  const isFormValid = formData.career && formData.semester && formData.course;

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Selector de Carrera */}
      <div>
        <label
          htmlFor="career"
          className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2"
        >
          🎓 Carrera
        </label>
        <select
          id="career"
          value={formData.career}
          onChange={(e) =>
            setFormData((prev) => ({ ...prev, career: e.target.value }))
          }
          className="w-full px-4 py-3 border border-slate-300 dark:border-slate-600 rounded-lg bg-white dark:bg-slate-700 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
          required
        >
          <option value="">Selecciona tu carrera</option>
          {careers.map((career) => (
            <option key={career} value={career}>
              {career}
            </option>
          ))}
        </select>
      </div>

      {/* Selector de Semestre */}
      <div>
        <label
          htmlFor="semester"
          className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2"
        >
          📅 Semestre
        </label>
        <select
          id="semester"
          value={formData.semester}
          onChange={(e) =>
            setFormData((prev) => ({
              ...prev,
              semester: parseInt(e.target.value),
            }))
          }
          disabled={!formData.career}
          className="w-full px-4 py-3 border border-slate-300 dark:border-slate-600 rounded-lg bg-white dark:bg-slate-700 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          required
        >
          <option value={0}>Selecciona tu semestre</option>
          {semesters.map((semester) => (
            <option key={semester} value={semester}>
              Semestre {semester}
            </option>
          ))}
        </select>
      </div>

      {/* Selector de Curso */}
      <div>
        <label
          htmlFor="course"
          className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2"
        >
          📚 Curso
        </label>
        <select
          id="course"
          value={formData.course}
          onChange={(e) =>
            setFormData((prev) => ({ ...prev, course: e.target.value }))
          }
          disabled={!formData.semester}
          className="w-full px-4 py-3 border border-slate-300 dark:border-slate-600 rounded-lg bg-white dark:bg-slate-700 text-slate-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          required
        >
          <option value="">Selecciona el curso</option>
          {courses.map((course) => (
            <option key={course} value={course}>
              {course}
            </option>
          ))}
        </select>
      </div>

      {/* Botón de envío */}
      <button
        type="submit"
        disabled={!isFormValid || loading}
        className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 disabled:from-slate-400 disabled:to-slate-500 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105 disabled:hover:scale-100 disabled:cursor-not-allowed shadow-lg hover:shadow-xl"
      >
        {loading ? (
          <div className="flex items-center justify-center space-x-2">
            <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
            <span>Obteniendo recomendaciones...</span>
          </div>
        ) : (
          "🔍 Obtener Recomendaciones"
        )}
      </button>

      {/* Información adicional */}
      <div className="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg p-4">
        <p className="text-sm text-blue-800 dark:text-blue-200">
          💡 <strong>Tip:</strong> Nuestro sistema analiza el rendimiento de
          estudiantes similares para recomendarte los recursos más efectivos.
        </p>
      </div>
    </form>
  );
}
