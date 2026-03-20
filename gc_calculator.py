#!/usr/bin/env python3
"""
GC Content Calculator
Reads a FASTA file and calculates GC content for each sequence.
Output: tab-delimited file with sequence_id, length, gc_content
Usage: python gc_calculator.py <input.fa> <min_length>
"""

import sys

def parse_fasta(filename):
    """Parse a FASTA file and return a dictionary of {header: sequence}"""
    sequences = {}
    header = None

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                header = line[1:].split()[0]
                sequences[header] = ''
            else:
                sequences[header] += line

    return sequences

def calculate_gc(sequence):
    """Calculate GC content as a percentage"""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = gc_count / len(sequence) * 100
    return gc_content

def filter_by_length(sequences, min_length):
    """Filter sequences shorter than min_length"""
    filtered = {}
    for header, seq in sequences.items():
        if len(seq) >= min_length:
            filtered[header] = seq
    return filtered

def main():
    if len(sys.argv) < 3:
        print("Usage: python gc_calculator.py <input.fa> <min_length>")
        sys.exit(1)

    input_file = sys.argv[1]
    min_length = int(sys.argv[2])

    sequences = parse_fasta(input_file)
    filtered = filter_by_length(sequences, min_length)

    print("sequence_id\tlength\tgc_content")
    for header, seq in filtered.items():
        gc = calculate_gc(seq)
        print(f"{header}\t{len(seq)}\t{gc:.2f}")

if __name__ == '__main__':
    main()
