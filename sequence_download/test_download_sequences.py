
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from download_sequences import download_sequence


class TestDownloadSequence(unittest.TestCase):

    def test_archivo_existente(self):
        """Comprueba que no se descarga un FASTA que ya existe."""

        with TemporaryDirectory() as temporal:
            directorio = Path(temporal)
            archivo = directorio / "NC_045512.2.fasta"
            archivo.write_text(">NC_045512.2\nATGC\n")

            with patch("download_sequences.Entrez.efetch") as efetch_simulado:
                resultado = download_sequence(
                    "NC_045512.2",
                    "ejemplo@example.com",
                    directorio
                )

            self.assertEqual(resultado, archivo)
            self.assertTrue(archivo.exists())
            efetch_simulado.assert_not_called()

    def test_descarga_secuencia(self):
        """Comprueba que el FASTA se guarda correctamente."""

        fasta_simulado = ">NC_045512.2 ejemplo\nATGCGC\n"

        with TemporaryDirectory() as temporal:
            directorio = Path(temporal) / "datos"

            with patch("download_sequences.Entrez.efetch") as efetch_simulado:
                efetch_simulado.return_value.__enter__.return_value.read.return_value = fasta_simulado

                resultado = download_sequence(
                    "NC_045512.2",
                    "ejemplo@example.com",
                    directorio
                )

            archivo_esperado = directorio / "NC_045512.2.fasta"

            self.assertEqual(resultado, archivo_esperado)
            self.assertTrue(archivo_esperado.is_file())
            self.assertEqual(
                archivo_esperado.read_text(),
                fasta_simulado
            )

            efetch_simulado.assert_called_once_with(
                db="nuccore",
                id="NC_045512.2",
                rettype="fasta",
                retmode="text"
            )

    def test_error_descarga(self):
        """Comprueba que un error de NCBI no genera un FASTA."""

        with TemporaryDirectory() as temporal:
            directorio = Path(temporal)
            archivo = directorio / "NC_045512.2.fasta"

            with patch(
                "download_sequences.Entrez.efetch",
                side_effect=OSError("Error simulado de NCBI")
            ):
                with self.assertRaises(OSError):
                    download_sequence(
                        "NC_045512.2",
                        "ejemplo@example.com",
                        directorio
                    )

            self.assertFalse(archivo.exists())


if __name__ == "__main__":
    unittest.main()
