// Configuración de la API
const USE_LOCAL_BACKEND =
  process.env.NEXT_PUBLIC_USE_LOCAL_BACKEND === "true" ||
  process.env.NODE_ENV === "development";
const API_BASE_URL = USE_LOCAL_BACKEND
  ? "http://localhost:5000"
  : "https://recommender-api-ffpd.onrender.com";

export const API_ENDPOINTS = {
  CAREERS: `${API_BASE_URL}/api/careers`,
  SEMESTERS: (career: string) =>
    `${API_BASE_URL}/api/semesters/${encodeURIComponent(career)}`,
  COURSES: (career: string, semester: number) =>
    `${API_BASE_URL}/api/courses/${encodeURIComponent(career)}/${semester}`,
  RECOMMENDATIONS: `${API_BASE_URL}/api/recommendations`,
};

export default API_BASE_URL;
