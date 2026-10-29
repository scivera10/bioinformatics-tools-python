
from Bio import Entrez
from pathlib import Path


def download_sequence(accession, email, output_dir):
    """
    Descarga una secuencia de nucleótidos desde NCBI
    y la guarda en un archivo FASTA.

    Args:
        accession (str): Identificador de acceso de NCBI.
        email (str): Correo electrónico para NCBI.
        output_dir (str | Path): Directorio de salida.

    Returns:
        Path: Ruta del archivo FASTA generado o existente.
    """

    # Configurar el correo electrónico para NCBI
    Entrez.email = email

    # Preparar el directorio de salida
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generar el nombre del archivo FASTA
    output_path = output_dir / f"{accession}.fasta"

    # Comprobar si el archivo ya existe
    if output_path.exists():
        print(f"La secuencia {accession} ya existe en {output_path}")
        return output_path

    # Descargar la secuencia desde NCBI
    with Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="fasta",
        retmode="text"
    ) as respuesta:
        fasta = respuesta.read()

    # Guardar la secuencia en formato FASTA
    with open(output_path, "w") as archivo:
        archivo.write(fasta)

    print(f"La secuencia {accession} se ha guardado en {output_path}")

    return output_path
