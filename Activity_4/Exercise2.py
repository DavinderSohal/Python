"""
Create a variable containing the DNA sequence: ACGCAGAATGCTTAGGACTAGTTAC
Turn it into a RNA sequence, which means changing all the ‘T’ values into ‘U’ values.
Finally, print out the middle letter in the middle of the sequence to the console.
"""

dna = "ACGCAGAATGCTTAGGACTAGTTAC"
rna = dna.replace("T", "U")
print("DNA: " + dna)
print("RNA: " + rna)
length_rna = len(rna)
print("Middle letter: " + rna[length_rna // 2])
