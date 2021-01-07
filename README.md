# scrambleseq
Scramble biological sequences (protein/DNA/RNA) in different formats.

## Usage
```
scrambleseq [-h] [-f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}] [-v] [inseqfile] [outseqfile]

Scramble biological sequences (protein/DNA/RNA) in different formats. If not input file name is given it reads from the standard input. If not output file name is given it writes to standard output.

positional arguments:
  inseqfile             Input sequence file [default: stdin].
  outseqfile            Output sequence file [default: stdout].

optional arguments:
  -h, --help            show this help message and exit
  -f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}, --format {fasta,clustal,embl,genbank,imgt,phd,pir,tab}
                        Sequence format [default: fasta].
  -v, --version         Show program's version number and exit.
```

## Installation
This is a Python script, so, you can just run the scrambleseq.py file or put a symbolic link in any directory of your PATH. The second option is recommend.

## Dependencies
* Python3:
    * Biopython
    * argparse
    * random
    * copy
