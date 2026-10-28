# BLAST TOOLS IN PYTHON

import subprocess

# Create a nucleotide BLAST database (run this command in the terminal):
# makeblastdb -in data/chimpance.fasta -dbtype nucl -out data/database/db_chimpance

def run_makeblastdb(input_fasta, dbtype, output):
    """
    Create a local BLAST database from a FASTA file.

    Parameters
    ----------
    input_fasta : str
        Path to the input FASTA file containing the sequences.

    dbtype : str
        Type of sequences in the database.
        "nucl" for nucleotide sequences.
        "prot" for protein sequences.

    output : str
        Output path and prefix for the BLAST database files.

    Notes
    -----
    The output directory must already exist.

    On Windows, avoid spaces in the output path if
    makeblastdb encounters database path errors.
    """

    command = [
        "makeblastdb",
        "-in", input_fasta,
        "-dbtype", dbtype,
        "-out", output
    ]

    print("Running:", command)

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)
    print("Exit code:", result.returncode)

    if result.returncode == 0:
        print(f"BLAST database created: {output}")
    else:
        print("Error: BLAST database creation failed.")


def run_blastn(query, db, output="resultado.tsv", evalue=1e-10, outfmt="6", max_target_seqs=10, num_threads=1):
    """
    Run a BLASTN search against a local BLAST database.

    Parameters
    ----------
    query : str
        Path to the FASTA file containing the query sequences.

    db : str
        Path or prefix of the formatted BLAST database.

    output : str
        Path to the output file.
        Default: "resultado.tsv".

    evalue : float
        Maximum E-value threshold.
        Default: 1e-10.

    outfmt : str
        BLAST output format.
        Default: "6" (tabular format without headers).

        Default output columns (outfmt 6):

        qseqid   : Query sequence ID.
        sseqid   : Subject sequence ID.
        pident   : Percentage of identical matches.
        length   : Alignment length.
        mismatch : Number of mismatches.
        gapopen  : Number of gap openings.
        qstart   : Start position in the query.
        qend     : End position in the query.
        sstart   : Start position in the subject.
        send     : End position in the subject.
        evalue   : Expectation value.
        bitscore : Bit score.

        Example of custom column selection:
        "6 qseqid sseqid pident length evalue bitscore"

    max_target_seqs : int
        Maximum number of target sequences to retain.
        Default: 10.

    num_threads : int
        Number of threads used by BLAST.
        Default: 1.
    """

    command = [
        "blastn",
        "-query", query,
        "-db", db,
        "-out", output,
        "-evalue", str(evalue),
        "-outfmt", outfmt,
        "-max_target_seqs", str(max_target_seqs),
        "-num_threads", str(num_threads)
    ]

    print("Running:", command)

    subprocess.run(command, check=True)

    print(f"Results saved to: {output}")


def run_blastp(query, db, output="resultado.tsv", evalue=1e-10, outfmt="6", max_target_seqs=10, num_threads=1):
    """
    Run a BLASTP protein sequence search against a local protein database.

    Parameters
    ----------
    query : str
        Path to the FASTA file containing the query protein sequences.
    
    db : str
        Path or prefix of the formatted protein BLAST database..

    output : str
        Path to the output file.
        Default: "resultado.tsv".

    evalue : float
        Maximum E-value threshold.
        Default: 1e-10.

    outfmt : str
        BLAST output format.
        Default: "6" (tabular format without headers).

        Default output columns (outfmt 6):

        qseqid   : Query sequence ID.
        sseqid   : Subject sequence ID.
        pident   : Percentage of identical matches.
        length   : Alignment length.
        mismatch : Number of mismatches.
        gapopen  : Number of gap openings.
        qstart   : Start position in the query.
        qend     : End position in the query.
        sstart   : Start position in the subject.
        send     : End position in the subject.
        evalue   : Expectation value.
        bitscore : Bit score.

        Example of custom column selection:
        "6 qseqid sseqid pident length evalue bitscore"

    max_target_seqs : int
        Maximum number of target sequences to retain.
        Default: 10.

    num_threads : int
        Number of threads used by BLAST.
        Default: 1.
    """

    command = [
        "blastp",
        "-query", query,
        "-db", db,
        "-out", output,
        "-evalue", str(evalue),
        "-outfmt", outfmt,
        "-max_target_seqs", str(max_target_seqs),
        "-num_threads", str(num_threads)
    ]

    print("Running", command)

    subprocess.run(command, check=True)

    print(f"Results saved to: {output}")