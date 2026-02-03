class Tarea:
    """
    Representa una tarea individual con validaciones.
    
    Atributos:
        id (int): Identificador único.
        descripcion (str): Detalle de la tarea.
        completado (bool): Estado de la tarea.
    """

    def __init__(self, id_t: int, descripcion: str):
        """
        Inicializa la tarea. Lanza error si la descripción está vacía.
        
        Args:
            id_t (int): ID único.
            descripcion (str): Texto de la tarea.
        """
        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
            
        self.id = id_t
        self.descripcion = descripcion
        self.completado = False

    def __str__(self):
        estado = "[X]" if self.completado else "[ ]"
        return f"Tarea {self.id}: {self.descripcion} {estado}"