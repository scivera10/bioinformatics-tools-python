# Bioinformatics Tools in Python

A collection of Python tools for bioinformatics analyses.

This project aims to develop reusable Python functions
for running bioinformatics software.

## BLAST Tools

Python functions for running NCBI BLAST+ locally.

### Available functions

- `run_makeblastdb()`: Create a local BLAST database from FASTA sequences.
- `run_blastn()`: Perform nucleotide sequence searches.
- `run_blastp()`: Perform protein sequence searches.

## Requirements

- Python 3
- NCBI BLAST+ installed and available in the system PATH.

## Project Structure

- `blast_py/blast_tools.py`: Python functions for BLAST.
- `blast_py/data/`: Example FASTA sequences.

## Development Status

This project is under active development.

Additional bioinformatics tools and functions will be added progressively.