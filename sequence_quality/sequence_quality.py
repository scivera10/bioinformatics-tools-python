
"""Basic quality metrics for DNA nucleotide sequences."""


def count_ambiguous_bases(sequence):
    """
    Count positions represented by 'N' in a nucleotide sequence.

    Args:
        sequence (str): Nucleotide sequence.

    Returns:
        int: Number of positions represented by 'N'.

    Raises:
        TypeError: If the sequence is not a string.
    """
    if not isinstance(sequence, str):
        raise TypeError("The sequence must be a string.")

    n_count = sequence.upper().count("N")
    return n_count


def calculate_ambiguous_percentage(sequence):
    """
    Calculate the percentage of positions represented by 'N'.

    Args:
        sequence (str): Nucleotide sequence.

    Returns:
        float: Percentage of positions represented by 'N'.

    Raises:
        TypeError: If the sequence is not a string.
        ValueError: If the sequence is empty.
    """
    n_count = count_ambiguous_bases(sequence)

    if len(sequence) == 0:
        raise ValueError("The sequence cannot be empty.")

    n_percentage = (n_count / len(sequence)) * 100
    return n_percentage


def count_iupac_ambiguous_bases(sequence):
    """
    Count positions containing ambiguous IUPAC codes in a DNA sequence.

    Args:
        sequence (str): DNA nucleotide sequence.

    Returns:
        int: Number of positions containing ambiguous IUPAC codes.

    Raises:
        TypeError: If the sequence is not a string.
    """
    if not isinstance(sequence, str):
        raise TypeError("The sequence must be a string.")

    ambiguous_codes = {
        "R", "Y", "S", "W", "K", "M",
        "B", "D", "H", "V", "N"
    }

    ambiguous_count = sum(
        1 for base in sequence.upper()
        if base in ambiguous_codes
    )

    return ambiguous_count


def find_invalid_bases(sequence):
    """
    Identify characters outside the IUPAC DNA nucleotide alphabet.

    Args:
        sequence (str): DNA nucleotide sequence.

    Returns:
        set: Unique invalid characters found in the sequence.

    Raises:
        TypeError: If the sequence is not a string.
        ValueError: If the sequence is empty.
    """
    if not isinstance(sequence, str):
        raise TypeError("The sequence must be a string.")

    if len(sequence) == 0:
        raise ValueError("The sequence cannot be empty.")

    ambiguous_codes = {
        "R", "Y", "S", "W", "K", "M",
        "B", "D", "H", "V", "N"
    }

    standard_bases = {"A", "T", "G", "C"}
    valid_bases = standard_bases.union(ambiguous_codes)

    invalid_bases = set(sequence.upper()).difference(valid_bases)

    return invalid_bases


def calculate_iupac_ambiguous_percentage(sequence):
    """
    Calculate the percentage of positions with ambiguous IUPAC codes.

    Args:
        sequence (str): DNA nucleotide sequence.

    Returns:
        float: Percentage of ambiguous IUPAC positions.

    Raises:
        TypeError: If the sequence is not a string.
        ValueError: If the sequence is empty.
    """
    iupac_ambiguous_count = count_iupac_ambiguous_bases(sequence)

    if len(sequence) == 0:
        raise ValueError("The sequence cannot be empty.")

    iupac_ambiguous_percentage = (
        iupac_ambiguous_count / len(sequence)
    ) * 100

    return iupac_ambiguous_percentage


def summarize_sequence_quality(sequence):
    """
    Summarize basic quality metrics of a DNA nucleotide sequence.

    Args:
        sequence (str): DNA nucleotide sequence.

    Returns:
        dict: Sequence length, N count and percentage, IUPAC ambiguity
              metrics, and unique invalid characters.

    Raises:
        TypeError: If the sequence is not a string.
        ValueError: If the sequence is empty.
    """
    if not isinstance(sequence, str):
        raise TypeError("The sequence must be a string.")

    if len(sequence) == 0:
        raise ValueError("The sequence cannot be empty.")

    quality_summary = {
        "length": len(sequence),
        "n_count": count_ambiguous_bases(sequence),
        "n_percentage": calculate_ambiguous_percentage(sequence),
        "iupac_ambiguous_count": count_iupac_ambiguous_bases(sequence),
        "iupac_ambiguous_percentage": calculate_iupac_ambiguous_percentage(sequence),
        "invalid_bases": find_invalid_bases(sequence),
    }

    return quality_summary
