def kMers(tSeq, k):
  kFreq = set()
  for i in range(0, len(tSeq) - k + 1):
    kFreq.add(tSeq[i:i+k])
  return len(kFreq)

tSeq = ""
with open("DNA.txt", "r") as f:
  for line in f:
    if line.startswith(">"):
      continue
    tSeq += line.strip()

max_unique_kmers = 0
max_k = 0

for k in range(1, 100):
  num_kmers = kMers(tSeq, k)
  if num_kmers > max_unique_kmers:
    max_unique_kmers = num_kmers
    max_k = k

reads = ["GGATCTTCCAGCAGACGCTCGGCAAAGTCCTGAATCGCATCGCCTTCCAGCGTTGCCGAAAAGAGCAGGGTCTGTTTACGCCAGCGCGTTTCGCCAGCAA",
         "TTATGAGAGGTTGGTCATATTATCGCGGGGAAACGAACCGAGGATTTGACAAAGCAATGCTGCGCCAACGTCTGGCACATGTTCAACGTAGGCCCGAAAT",
         "GATCGCTAACCTGTTGCTGGCTCCGTACTTCAAGCAAATTGCCGATGACTACCAGCAGGCGCTGCGTGATGTCGTTGGTTATGCAGTA"]

print(f"Max unique kmers: {max_unique_kmers} when k = {max_k}")

