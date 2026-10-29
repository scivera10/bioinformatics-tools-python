# NCBI Sequence Download

Python utilities for downloading nucleotide sequences from the NCBI Nucleotide database using accession numbers and saving them in FASTA format.

## Overview

The National Center for Biotechnology Information (NCBI) provides access to biological sequence databases through its Entrez system.

This module uses Biopython's `Bio.Entrez` interface to retrieve nucleotide sequences programmatically.

It provides a reusable function for downloading sequences, organizing output files, and avoiding unnecessary downloads when a corresponding file already exists.

## Features

- Download nucleotide sequences from NCBI using accession numbers.
- Retrieve sequences in FASTA format.
- Automatically create output directories.
- Generate FASTA filenames from accession numbers.
- Check whether a sequence file already exists before downloading.
- Return the path of the downloaded or existing FASTA file.
- Include automated unit tests with simulated NCBI responses.

## Project Structure

```text
sequence_download/
├── download_sequences.py
├── test_download_sequences.py
└── README.md
```

## Requirements

- Python 3
- Biopython
- Internet connection for downloading sequences from NCBI
- A valid email address for configuring NCBI Entrez requests

Install Biopython:

```bash
pip install biopython
```

## Available Functions

### `download_sequence(accession, email, output_dir)`

Downloads a nucleotide sequence from the NCBI Nucleotide database and saves it as a FASTA file.

If a file with the corresponding accession number already exists in the specified directory, the function returns its path without performing another download.

**Parameters**

- `accession` (`str`): NCBI nucleotide accession number.
- `email` (`str`): Email address used to identify requests to NCBI.
- `output_dir` (`str | Path`): Directory where the FASTA file will be saved.

**Returns**

- `Path`: Path to the downloaded or existing FASTA file.

## Usage Example

```python
from download_sequences import download_sequence

accession = "NM_000546.6"
email = "your_email@example.com"
output_dir = "./data"

output_path = download_sequence(
    accession=accession,
    email=email,
    output_dir=output_dir
)

print(output_path)
```

**Expected output path**

```text
data/NM_000546.6.fasta
```

The function automatically creates the `data/` directory if it does not already exist.

### Reading the downloaded FASTA file

The downloaded sequence can be read using Biopython's `SeqIO` module:

```python
from Bio import SeqIO

record = SeqIO.read(output_path, "fasta")

print(record.id)
print(len(record.seq))
```

This allows access to the sequence identifier and nucleotide sequence for subsequent bioinformatics analyses.

## File Management

The function constructs the output filename using the accession number:

```text
<accession>.fasta
```

For example:

```text
data/
└── NM_000546.6.fasta
```

Before downloading, the function checks whether the output path already exists.

- **Existing file:** Returns the file path without contacting NCBI.
- **Missing file:** Downloads the sequence and creates the FASTA file.
- **Download error:** Propagates the exception rather than returning a successful download result.

This approach reduces unnecessary requests to NCBI and supports reproducible file organization.

## Unit Testing

The `test_download_sequences.py` file contains three automated unit tests implemented using Python's `unittest` framework.

| Test | Description |
|---|---|
| `test_archivo_existente` | Verifies that an existing FASTA file is reused without requesting another download. |
| `test_descarga_secuencia` | Verifies that a downloaded FASTA sequence is written correctly and that its path is returned. |
| `test_error_descarga` | Verifies that a simulated NCBI request error is propagated and no FASTA file is created. |

The tests use `unittest.mock` to simulate NCBI responses and `tempfile.TemporaryDirectory` to manage temporary files.

**No real NCBI requests are performed during unit testing.**

### Running the tests

From the `sequence_download` directory:

```bash
python -m unittest -v test_download_sequences
```

Alternatively:

```bash
python test_download_sequences.py
```

A successful execution displays a summary similar to:

```text
Ran 3 tests

OK
```

## Limitations

- The function downloads one nucleotide record per call.
- Downloaded FASTA content is not independently validated.
- Existing files are reused without checking their integrity.
- Invalid accession numbers and network failures are not handled through custom exception classes.
- The module does not currently support bulk downloads, automatic retries, or rate-limit management.

## Development Status

The sequence download module is implemented and includes three automated unit tests.

It is part of the [Bioinformatics Tools in Python](https://github.com/scivera10/bioinformatics-tools-python) repository, a collection of reusable Python utilities for bioinformatics workflows.
