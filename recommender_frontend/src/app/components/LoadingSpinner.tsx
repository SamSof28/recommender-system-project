export default function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="relative">
        {/* Spinner principal */}
        <div className="w-12 h-12 border-4 border-slate-200 dark:border-slate-700 border-t-blue-600 rounded-full animate-spin"></div>
        
        {/* Spinner secundario */}
        <div className="absolute top-0 left-0 w-12 h-12 border-4 border-transparent border-r-purple-600 rounded-full animate-spin" style={{ animationDirection: 'reverse', animationDuration: '1.5s' }}></div>
      </div>
      
      <div className="mt-4 text-center">
        <p className="text-slate-600 dark:text-slate-400 font-medium">
          Analizando datos académicos...
        </p>
        <p className="text-xs text-slate-500 dark:text-slate-500 mt-1">
          Utilizando algoritmos de Álgebra Lineal
        </p>
      </div>
      
      {/* Puntos animados */}
      <div className="flex space-x-1 mt-3">
        <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
        <div className="w-2 h-2 bg-purple-600 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
        <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
      </div>
    </div>
  );
}
