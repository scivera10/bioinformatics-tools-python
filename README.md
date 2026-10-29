# Bioinformatics Tools in Python

A collection of reusable Python tools for biological sequence analysis, sequence retrieval, quality assessment, and bioinformatics workflows.

## Overview

This repository contains modular Python utilities designed to support common bioinformatics tasks.

The tools are developed with an emphasis on code readability, reusability, documentation, and automated testing.

## Available Tools

### BLAST Tools (`blast_py/`)

Utilities for running local NCBI BLAST+ searches and managing sequence databases.

### GC Analysis (`gc_analysis/`)

Functions for calculating GC content in nucleotide sequences, including global GC percentages and non-overlapping sequence windows.

### Sequence Download (`sequence_download/`)

Tools for retrieving nucleotide sequences from NCBI using accession identifiers and saving them in FASTA format.

### Sequence Quality (`sequence_quality/`)

Functions for evaluating basic nucleotide sequence quality, including sequence length, ambiguous IUPAC codes, and invalid characters.

## Requirements

- Python 3
- Biopython
- NCBI BLAST+ for BLAST-related tools

## Testing

The sequence analysis modules include automated unit tests implemented using Python's `unittest` framework.

## Development Status

This repository is under active development. Additional utilities for sequence analysis and bioinformatics workflows will be incorporated progressively.
