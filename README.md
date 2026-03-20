Midterm exam
Your instructor has a GitHub repository containing a Python script (`gc_calculator.py`) that calculates GC content from a FASTA file. The script has multiple bugs. A test input file (`test_sequences.fa`) is provided in the repository.

**Repository URL:** `https://github.com/stevenchristian-unr/BCH709_midterm`

The expected behavior of the script:
```
python gc_calculator.py test_sequences.fa 10
```

Should output a tab-delimited table of all sequences with length >= 10 bp, showing the correct sequence ID, full sequence length, and GC content (%).

Expected output:
```
sequence_id	length	gc_content
gene1	38	50.00
gene2	14	71.43
gene3	12	50.00
gene4	16	50.00
```


Tasks:

(A) Fork the repository to your own GitHub account and clone it to your local machine (or Pronghorn). Show the exact commands you used. (3 points)

(B) Run the script with the test input. Describe what happens and identify all bugs in the code. For each bug, explain what the code does wrong, what the correct behavior should be, and which line(s) you will change. (9 points)

1. The interpreter stops before any code runs. Remove line 59 which is a extra space.
2. filter_by_length() compares len(seq) to a string and crashes. It should parse the CLI argument as an integer before filtering.
3. In parse_fasta(), each new sequence line replaces the previous one, so gene1 becomes only TTTGGGCCCAAA and gene3 becomes only its last line. It should append sequence lines until the next header.
4. Output uses gene1 chrI protein_coding instead of just gene1. It should use the first token after > as sequence_id.
5. Gene2 reports 0.00 and gene4 reports 25.00 because only uppercase G and C are counted. It should treat uppercase and lowercase bases the same.
Sequences exactly equal to the threshold are excluded. It should Include all sequences with length >= min_length, per the README.

(C) Fix all bugs, verify your corrected script produces the expected output, commit your changes with a descriptive commit message, push to your fork, and submit a pull request to the original repository. The pull request description must list each bug and how you fixed it. (8 points)


Submission: Provide the URL of your pull request.
