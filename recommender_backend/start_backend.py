#!/usr/bin/env python3
"""
Script para iniciar el backend local
"""
import os
import sys
import subprocess

def main():
    # Cambiar al directorio del backend
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(backend_dir)
    
    print("🚀 Iniciando el backend del sistema de recomendación...")
    print(f"📁 Directorio: {backend_dir}")
    
    # Verificar que el archivo app.py existe
    app_file = os.path.join(backend_dir, "api", "app.py")
    if not os.path.exists(app_file):
        print("❌ Error: No se encontró el archivo app.py")
        return 1
    
    try:
        # Iniciar el servidor Flask
        print("🌐 Iniciando servidor Flask en http://localhost:5000")
        print("📋 Endpoints disponibles:")
        print("   - GET  /api/careers")
        print("   - GET  /api/semesters/<career>")
        print("   - GET  /api/courses/<career>/<semester>")
        print("   - POST /api/recommendations")
        print("   - GET  /api/documents/<path:filename>")
        print("   - GET  /api/documents/list")
        print("\n💡 Presiona Ctrl+C para detener el servidor\n")
        
        # Ejecutar el servidor Flask
        subprocess.run([sys.executable, app_file], check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al iniciar el servidor: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
