# GC Content Analysis

Python utilities for calculating the GC content of nucleotide sequences, including global GC percentage and local GC distribution using non-overlapping windows.

## Overview

GC content represents the proportion of guanine (G) and cytosine (C) nucleotides in a sequence.

It is a commonly used metric in bioinformatics for characterizing nucleotide composition and examining differences across genomic regions.

This module provides reusable functions for calculating GC content using Python and Biopython.

## Features

- Calculate the global GC percentage of a nucleotide sequence.
- Calculate local GC percentages using non-overlapping windows.
- Support customizable window sizes.
- Handle a final window shorter than the specified window size.
- Validate empty sequences and invalid window parameters.
- Include automated unit tests using Python's `unittest` framework.

## Project Structure

```text
gc_analysis/
├── calculate_gc.py
├── test_calculate_gc.py
└── README.md
```

## Requirements

- Python 3
- Biopython

Install the required dependency:

```bash
pip install biopython
```

## Available Functions

### `calcular_gc(secuencia)`

Calculates the overall GC percentage of a nucleotide sequence.

**Parameters**

- `secuencia` (`str`): Input nucleotide sequence.

**Returns**

- `float`: GC percentage.

**Example**

```python
from calculate_gc import calcular_gc

sequence = "ATGCGCATAT"

gc = calcular_gc(sequence)

print(f"GC content: {gc:.2f}%")
```

**Expected output**

```text
GC content: 40.00%
```

### `calcular_gc_ventanas(secuencia, window=1000)`

Calculates GC percentages across non-overlapping windows.

**Parameters**

- `secuencia` (`str`): Input nucleotide sequence.
- `window` (`int`): Window size in nucleotides. Default: `1000`.

**Returns**

- `list`: GC percentages for each window.

**Example**

```python
from calculate_gc import calcular_gc_ventanas

sequence = "ATGCGCATAT"

gc_windows = calcular_gc_ventanas(sequence, window=4)

print(gc_windows)
```

**Expected output**

```text
[50.0, 50.0, 0.0]
```

The sequence is divided into three non-overlapping windows:

| Window | Sequence | GC (%) |
|---|---|---|
| 1 | ATGC | 50.0 |
| 2 | GCAT | 50.0 |
| 3 | AT | 0.0 |

The final window contains fewer nucleotides because the sequence length is not divisible by the window size.

## Unit Testing

The `test_calculate_gc.py` file contains eight automated unit tests.

These tests cover:

- Global GC percentage calculations.
- GC calculations using non-overlapping windows.
- Invalid window sizes, including decimal, negative and zero values.
- Window sizes larger than the sequence.
- Empty nucleotide sequences.
- Sequences with 0% and 100% GC content.

To run the tests from the `gc_analysis` directory:

```bash
python -m unittest -v test_calculate_gc
```

Alternatively, run the test file directly:

```bash
python test_calculate_gc.py
```

A successful execution displays:

```text
Ran 8 tests

OK
```

## Limitations

- The module does not explicitly validate all nucleotide characters.
- Ambiguous nucleotide handling follows the default behavior of Biopython's `gc_fraction()` function.
- GC windows are non-overlapping; overlapping sliding windows are not implemented.
- The functions operate on nucleotide sequences provided in memory and do not directly read FASTA files.

## Development Status

The GC analysis module is implemented and includes automated unit tests.

It is part of the [Bioinformatics Tools in Python](https://github.com/scivera10/bioinformatics-tools-python) repository, a collection of reusable Python utilities for bioinformatics.
