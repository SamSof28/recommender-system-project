#!/usr/bin/env python3
"""
Script para agregar nuevos documentos al sistema de recomendación.
Uso: python add_document.py <ruta_del_archivo> <carrera> <materia> <tipo>
"""

import os
import sys
import shutil
from pathlib import Path

def add_document(file_path, career, subject, doc_type="libro", recommended_by="Sistema"):
    """
    Agrega un nuevo documento al sistema.
    
    Args:
        file_path: Ruta del archivo a agregar
        career: Carrera (ej: "Ingeniería de Sistemas")
        subject: Materia (ej: "Algebra Lineal")
        doc_type: Tipo de documento (libro, video, etc.)
        recommended_by: Quien lo recomienda
    """
    
    # Rutas base
    base_dir = Path(__file__).parent.parent
    documents_dir = base_dir / "data" / "documents"
    mock_data_file = base_dir / "data" / "mock_data.py"
    
    # Crear estructura de carpetas
    career_dir = documents_dir / career
    subject_dir = career_dir / subject.lower().replace(" ", "_")
    subject_dir.mkdir(parents=True, exist_ok=True)
    
    # Copiar archivo
    file_name = Path(file_path).name
    dest_path = subject_dir / file_name
    shutil.copy2(file_path, dest_path)
    
    print(f"✅ Archivo copiado a: {dest_path}")
    
    # Generar enlace para el sistema
    relative_path = f"{career}/{subject.lower().replace(' ', '_')}/{file_name}"
    link = f"http://localhost:5000/api/documents/{relative_path}"
    
    print(f"🔗 Enlace generado: {link}")
    
    # Mostrar código para agregar a mock_data.py
    print("\n📝 Agrega este código a tu RESOURCES_DATA en mock_data.py:")
    print("-" * 60)
    print(f'"{subject}": [')
    print(f'    {{"type": "{doc_type}", "title": "{file_name}", "link": "{link}", \'recommended_by\': \'{recommended_by}\'}},')
    print(']')
    print("-" * 60)
    
    return link

def main():
    if len(sys.argv) < 4:
        print("Uso: python add_document.py <ruta_del_archivo> <carrera> <materia> [tipo] [recomendado_por]")
        print("Ejemplo: python add_document.py libro.pdf 'Ingeniería de Sistemas' 'Cálculo Diferencial' 'libro' 'Profesor'")
        sys.exit(1)
    
    file_path = sys.argv[1]
    career = sys.argv[2]
    subject = sys.argv[3]
    doc_type = sys.argv[4] if len(sys.argv) > 4 else "libro"
    recommended_by = sys.argv[5] if len(sys.argv) > 5 else "Sistema"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no existe")
        sys.exit(1)
    
    try:
        link = add_document(file_path, career, subject, doc_type, recommended_by)
        print(f"\n🎉 Documento agregado exitosamente!")
        print(f"💡 Recuerda reiniciar el servidor Flask para que los cambios surtan efecto")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
