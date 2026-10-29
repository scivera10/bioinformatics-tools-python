
import unittest

from sequence_quality import (
    count_ambiguous_bases,
    calculate_ambiguous_percentage,
    count_iupac_ambiguous_bases,
    find_invalid_bases,
    calculate_iupac_ambiguous_percentage,
    summarize_sequence_quality
)


class TestSequenceQuality(unittest.TestCase):

    def test_count_ambiguous_bases(self):
        """Test counting N bases."""
        self.assertEqual(count_ambiguous_bases("ATGCNN"), 2)
        self.assertEqual(count_ambiguous_bases("atgcnn"), 2)
        self.assertEqual(count_ambiguous_bases("ATGC"), 0)

    def test_calculate_ambiguous_percentage(self):
        """Test the percentage of N bases."""
        self.assertAlmostEqual(
            calculate_ambiguous_percentage("ATGCNN"),
            33.3333333,
            places=6
        )
        self.assertEqual(
            calculate_ambiguous_percentage("ATGC"), 0.0
        )
        self.assertEqual(
            calculate_ambiguous_percentage("NNNN"), 100.0
        )

    def test_count_iupac_ambiguous_bases(self):
        """Test counting ambiguous IUPAC positions."""
        self.assertEqual(
            count_iupac_ambiguous_bases("ATGCRYNN"), 4
        )
        self.assertEqual(
            count_iupac_ambiguous_bases("atgcry"), 2
        )
        self.assertEqual(
            count_iupac_ambiguous_bases("ATGC"), 0
        )

    def test_find_invalid_bases(self):
        """Test identification of invalid DNA characters."""
        self.assertEqual(
            find_invalid_bases("ATGCXYZ"), {"X", "Z"}
        )
        self.assertEqual(
            find_invalid_bases("ATGCXXX"), {"X"}
        )
        self.assertEqual(
            find_invalid_bases("ATGCRYNN"), set()
        )

    def test_calculate_iupac_ambiguous_percentage(self):
        """Test the percentage of ambiguous IUPAC positions."""
        self.assertEqual(
            calculate_iupac_ambiguous_percentage("ATGCRYNN"),
            50.0
        )
        self.assertEqual(
            calculate_iupac_ambiguous_percentage("ATGC"),
            0.0
        )
        self.assertEqual(
            calculate_iupac_ambiguous_percentage("NNNN"),
            100.0
        )

    def test_summarize_sequence_quality(self):
        """Test the complete sequence quality summary."""
        result = summarize_sequence_quality("ATGCRYNNXZ")

        self.assertEqual(result["length"], 10)
        self.assertEqual(result["n_count"], 2)
        self.assertEqual(result["n_percentage"], 20.0)
        self.assertEqual(result["iupac_ambiguous_count"], 4)
        self.assertEqual(result["iupac_ambiguous_percentage"], 40.0)
        self.assertEqual(result["invalid_bases"], {"X", "Z"})

    def test_invalid_input_type(self):
        """Test TypeError for non-string inputs."""
        functions = [
            count_ambiguous_bases,
            calculate_ambiguous_percentage,
            count_iupac_ambiguous_bases,
            find_invalid_bases,
            calculate_iupac_ambiguous_percentage,
            summarize_sequence_quality
        ]

        for function in functions:
            with self.subTest(function=function.__name__):
                with self.assertRaises(TypeError):
                    function(123)

    def test_empty_sequence(self):
        """Test the behavior of empty sequences."""
        self.assertEqual(count_ambiguous_bases(""), 0)
        self.assertEqual(count_iupac_ambiguous_bases(""), 0)

        functions = [
            calculate_ambiguous_percentage,
            find_invalid_bases,
            calculate_iupac_ambiguous_percentage,
            summarize_sequence_quality
        ]

        for function in functions:
            with self.subTest(function=function.__name__):
                with self.assertRaises(ValueError):
                    function("")


if __name__ == "__main__":
    unittest.main()
