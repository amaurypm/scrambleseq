#!/usr/bin/env python3
## Scramble biological sequences (protein/DNA/RNA) in different formats.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from random import shuffle
from copy import deepcopy

## Functions
def scramble_record(seq_record):
    new_record = deepcopy(seq_record)
    new_record.id = new_record.id + '_scrambled'
    #new_record.name = new_record.name + '_scrambled'
    new_record.description = new_record.description.replace(seq_record.id, new_record.id)
    seq_as_list = list(seq_record.seq)
    shuffle(seq_as_list)
    new_record.seq = Seq(''.join(seq_as_list), alphabet = seq_record.seq.alphabet)
    return new_record

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Scramble biological sequences (protein/DNA/RNA) in different formats. If not input file name is given it reads from the standard input. If not output file name is given it writes to standard output.")
    parser.add_argument('inseqfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input sequence file [default: stdin].')
    parser.add_argument('outseqfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Output sequence file [default: stdout].')
    parser.add_argument('-f', '--format', choices=['fasta','clustal', 'embl', 'genbank', 'imgt', 'phd', 'pir', 'tab'], default='fasta', help='Sequence format [default: %(default)s].')
    parser.add_argument('-v', '--version', action='version', version='0.9.0', help="Show program's version number and exit.")

    args=parser.parse_args()

    scrambled_seqs = []
    try:
        for record in SeqIO.parse(args.inseqfile, args.format):
            scrambled_seqs.append(scramble_record(record))

    except ValueError:
        sys.stderr.write("ERROR: Input has not a valid {} format.".format(args.format))
        sys.exit(1)

    SeqIO.write(scrambled_seqs, args.outseqfile, args.format)

## Running the script
if __name__ == "__main__":
        main()

