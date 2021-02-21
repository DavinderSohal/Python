dna = "ACGCAGAATGCTTAGGACTAGTTAC"
rna = dna.replace("T", "U")
print("DNA: " + dna)
print("RNA: " + rna)
length_rna = len(rna)
print("Middle letter: " + rna[length_rna//2])
