
from Bio.SeqUtils import gc_fraction


def calcular_gc(secuencia):
    """
    Calcula el porcentaje GC de una secuencia nucleotídica.

    Args:
        secuencia (str): Secuencia de nucleótidos.

    Returns:
        float: Porcentaje de guanina y citosina.
    """
    if len(secuencia) == 0:
        raise ValueError("La secuencia no puede estar vacía")
        
    gc = gc_fraction(secuencia) * 100
    return gc


def calcular_gc_ventanas(secuencia, window=1000):
    """
    Calcula el porcentaje GC en ventanas no solapadas.

    Args:
        secuencia (str): Secuencia de nucleótidos.
        window (int): Tamaño de las ventanas.

    Returns:
        list: Porcentajes GC de cada ventana.
    """
    if not isinstance(window, int) or isinstance(window, bool):
        raise TypeError("El tamaño de ventana debe ser un número entero")

    if window <= 0:
        raise ValueError("El tamaño de ventana debe ser mayor que 0")
    
    if len(secuencia) == 0:
        raise ValueError("La secuencia no puede estar vacía")

    gc_fragmentos = []

    for inicio in range(0, len(secuencia), window):
        fin = min(inicio + window, len(secuencia))
        fragmento = secuencia[inicio:fin]

        gc_fragmento = calcular_gc(fragmento)
        gc_fragmentos.append(gc_fragmento)

    return gc_fragmentos
