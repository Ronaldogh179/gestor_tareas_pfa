from src.datos.repositorio import RepositorioTareas
from src.logica.gestor import GestorTareas
from src.logica.tarea import Tarea

def main():
    repo = RepositorioTareas()
    gestor = GestorTareas(repo)

    print("=== 1. DEMOSTRACIÓN DE DOCSTRING (Requisito del Profesor) ===")
    # Esto muestra la documentación de la clase automáticamente
    help(Tarea)
    
    print("\n=== 2. EJECUCIÓN DEL PROGRAMA ===")
    try:
        # Caso correcto: Agregamos tareas
        gestor.agregar_tarea("Terminar el laboratorio de Python")
        gestor.agregar_tarea("Subir proyecto a GitHub")
        
        # Caso error: Intentamos agregar un duplicado para probar la validación
        print("\nIntentando agregar duplicado...")
        gestor.agregar_tarea("terminar el laboratorio de python")

    except ValueError as e:
        print(f"[ERROR CAPTURADO]: {e}")

    print("\n=== 3. ESTADO FINAL DE LAS TAREAS ===")
    for t in repo.obtener_todas():
        print(t)

if __name__ == "__main__":
    main()