# DNA & Protein Sequence Toolkit 🧬

My first bioinformatics project!

This is a small Python program I made to practice working with biological sequences and Python. It takes a DNA sequence from a FASTA file and performs some basic sequence analysis.

### What it can do

* Find sequence length
* Calculate GC%
* Count A, T, G and C
* Find the reverse complement
* Transcribe DNA into RNA
* Translate DNA into protein
* Find a basic ORF
* Count amino acids
* Calculate approximate molecular weight
* Search for a motif

### Files

`main.py` — the main Python program

`sequence.fasta` — sample DNA sequence used for testing

### How to run

Make sure Python is installed, then run:

```bash
python main.py
```

The program will show a menu where you can choose what you want to analyse.

### Example

For the sample sequence:

```text
ATGAAACCCGGGTAA
```

the program can give:

```text
Length: 15
GC%: 46.67%
RNA: AUGAAACCCGGGUAA
Protein: MKPG*
ORF: ATGAAACCCGGGTAA
```

### Why I made this

I'm currently learning bioinformatics and wanted to start with something small that actually combines the biology I'm studying with programming.

This is a beginner project, so I'll probably keep improving it as I learn more. 🧬

