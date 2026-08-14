# GC Content Analysis
# Author: Akshat Vishwakarma

dna = "ATGCGTACGTTAGC"

# Validate DNA sequence
valid_bases = "ATGC"

if all(base in valid_bases for base in dna):
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence")

# Count nucleotides
A = dna.count("A")
T = dna.count("T")
G = dna.count("G")
C = dna.count("C")

print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

# Calculate GC content
gc_content = (G + C) / len(dna) * 100

print("GC Content:", round(gc_content, 2), "%")
