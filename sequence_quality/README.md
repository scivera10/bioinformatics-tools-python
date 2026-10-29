# Nucleotide Sequence Quality Assessment

Python utilities for evaluating basic quality metrics of DNA nucleotide sequences, including ambiguous nucleotides, IUPAC ambiguity codes, and invalid characters.

## Overview

Sequence quality assessment is an important step in bioinformatics workflows, particularly before performing genomic comparisons or downstream sequence analyses.

Nucleotide sequences may contain ambiguous positions where the exact nucleotide identity is unknown or partially determined.

This module provides reusable Python functions for identifying and quantifying these positions, validating nucleotide characters, and generating basic sequence quality summaries.

## Features

- Count nucleotide positions represented by `N`.
- Calculate the percentage of unknown nucleotide positions.
- Identify and count ambiguous IUPAC nucleotide codes.
- Calculate the percentage of ambiguous IUPAC positions.
- Detect characters outside the IUPAC DNA alphabet.
- Generate a summary of basic sequence quality metrics.
- Validate input types and handle empty sequences.
- Include automated unit tests using Python's `unittest` framework.

## Project Structure

```text
sequence_quality/
├── sequence_quality.py
├── test_sequence_quality.py
└── README.md
```

## Requirements

- Python 3

The module uses only Python's standard built-in functionality and does not require external dependencies.

**Optional:** Biopython can be used to read nucleotide sequences from FASTA files before applying these functions.

To install Biopython:

```bash
pip install biopython
```

## Available Functions

### `count_ambiguous_bases(sequence)`

Counts the number of nucleotide positions represented by `N`, regardless of case.

**Parameters**

- `sequence` (`str`): Input nucleotide sequence.

**Returns**

- `int`: Number of positions containing `N`.

**Example**

```python
from sequence_quality import count_ambiguous_bases

sequence = "ATGCNNATGnN"

n_count = count_ambiguous_bases(sequence)

print(n_count)
```

**Expected output**

```text
4
```

### `calculate_ambiguous_percentage(sequence)`

Calculates the percentage of nucleotide positions represented by `N` relative to the total sequence length.

\[
N\text{ percentage} = \frac{\text{Number of N positions}}{\text{Sequence length}} \times 100
\]

**Parameters**

- `sequence` (`str`): Input nucleotide sequence.

**Returns**

- `float`: Percentage of positions containing `N`.

**Example**

```python
from sequence_quality import calculate_ambiguous_percentage

sequence = "ATGCNNATGnN"

percentage = calculate_ambiguous_percentage(sequence)

print(f"N percentage: {percentage:.2f}%")
```

**Expected output**

```text
N percentage: 36.36%
```

### `count_iupac_ambiguous_bases(sequence)`

Counts positions containing ambiguous IUPAC nucleotide codes.

The following codes are recognized:

| Code | Possible nucleotides |
|---|---|
| R | A or G |
| Y | C or T |
| S | G or C |
| W | A or T |
| K | G or T |
| M | A or C |
| B | C, G or T |
| D | A, G or T |
| H | A, C or T |
| V | A, C or G |
| N | A, C, G or T |

**Parameters**

- `sequence` (`str`): Input DNA nucleotide sequence.

**Returns**

- `int`: Number of ambiguous IUPAC positions.

**Example**

```python
from sequence_quality import count_iupac_ambiguous_bases

sequence = "ATGCRYNN"

ambiguous_count = count_iupac_ambiguous_bases(sequence)

print(ambiguous_count)
```

**Expected output**

```text
4
```

### `calculate_iupac_ambiguous_percentage(sequence)`

Calculates the percentage of positions containing ambiguous IUPAC nucleotide codes.

**Parameters**

- `sequence` (`str`): Input DNA nucleotide sequence.

**Returns**

- `float`: Percentage of ambiguous IUPAC positions.

**Example**

```python
from sequence_quality import calculate_iupac_ambiguous_percentage

sequence = "ATGCRYNN"

percentage = calculate_iupac_ambiguous_percentage(sequence)

print(f"IUPAC ambiguity: {percentage:.2f}%")
```

**Expected output**

```text
IUPAC ambiguity: 50.00%
```

### `find_invalid_bases(sequence)`

Identifies characters that do not belong to the standard or ambiguous IUPAC DNA nucleotide alphabet.

The accepted alphabet includes `A`, `T`, `G`, `C` and the eleven ambiguous IUPAC codes.

**Parameters**

- `sequence` (`str`): Input DNA nucleotide sequence.

**Returns**

- `set`: Unique invalid characters found in the sequence.

**Example**

```python
from sequence_quality import find_invalid_bases

sequence = "ATGCRYNNXZ"

invalid_bases = find_invalid_bases(sequence)

print(invalid_bases)
```

**Expected output**

```text
{'X', 'Z'}
```

The order of elements may vary because the function returns a Python set.

Repeated invalid characters are reported only once.

### `summarize_sequence_quality(sequence)`

Combines the five previous functions into a single sequence quality summary.

**Parameters**

- `sequence` (`str`): Input DNA nucleotide sequence.

**Returns**

- `dict`: Dictionary containing sequence length, ambiguity counts and percentages, and invalid characters.

**Example**

```python
from sequence_quality import summarize_sequence_quality

sequence = "ATGCRYNNXZ"

quality_summary = summarize_sequence_quality(sequence)

for key, value in quality_summary.items():
    print(f"{key}: {value}")
```

**Expected output**

```text
length: 10
n_count: 2
n_percentage: 20.0
iupac_ambiguous_count: 4
iupac_ambiguous_percentage: 40.0
invalid_bases: {'X', 'Z'}
```

The summary contains six quality indicators:

| Metric | Description |
|---|---|
| `length` | Total sequence length |
| `n_count` | Number of N positions |
| `n_percentage` | Percentage of N positions |
| `iupac_ambiguous_count` | Number of ambiguous IUPAC positions |
| `iupac_ambiguous_percentage` | Percentage of ambiguous IUPAC positions |
| `invalid_bases` | Set of unique invalid characters |

## Working with FASTA Files

The module processes nucleotide sequences provided as Python strings.

FASTA files can be read separately using Biopython's `SeqIO` module:

```python
from Bio import SeqIO
from sequence_quality import summarize_sequence_quality

record = SeqIO.read("sequence.fasta", "fasta")

sequence = str(record.seq)

quality_summary = summarize_sequence_quality(sequence)

print(quality_summary)
```

The nucleotide sequence is converted to a string before being passed to the quality assessment functions.

## Unit Testing

The `test_sequence_quality.py` file contains eight automated unit tests implemented using Python's `unittest` framework.

These tests verify:

- Counting N positions in nucleotide sequences.
- Calculating N percentages.
- Counting ambiguous IUPAC positions.
- Identifying invalid nucleotide characters.
- Calculating IUPAC ambiguity percentages.
- Generating complete quality summaries.
- Handling invalid input types.
- Handling empty nucleotide sequences.

### Running the tests

From the `sequence_quality` directory:

```bash
python -m unittest -v test_sequence_quality
```

Alternatively:

```bash
python test_sequence_quality.py
```

A successful execution displays:

```text
Ran 8 tests

OK
```

The unit tests use predefined nucleotide sequences and do not require an Internet connection or external sequence databases.

## Error Handling

The functions implement basic input validation:

- **`TypeError`** is raised when an input is not a string.
- **`ValueError`** is raised for empty sequences in functions that require a non-zero sequence length or explicitly reject empty input.

The two counting functions return `0` for empty strings.

## Limitations

- The module evaluates basic nucleotide sequence characteristics, not raw sequencing read quality.
- FASTQ quality scores, sequencing coverage, and read-level quality metrics are not assessed.
- The functions do not automatically read FASTA files.
- Only the IUPAC DNA nucleotide alphabet is considered valid.
- Ambiguity percentages use the total sequence length, including any invalid characters.
- Invalid characters are identified as unique symbols, rather than counted individually.
- No automatic sequence acceptance or rejection thresholds are implemented.
- The module does not detect sequencing errors, biological mutations, or structural variants.

These metrics provide an initial assessment of sequence completeness and ambiguity but do not constitute a comprehensive genomic quality-control pipeline.

## Development Status

The nucleotide sequence quality assessment module is implemented and includes eight automated unit tests.

It is part of the [Bioinformatics Tools in Python](https://github.com/scivera10/bioinformatics-tools-python) repository, a collection of reusable Python utilities for bioinformatics workflows.
