from collections import Counter
import random
import matplotlib.pyplot as plt

kmer_lengths = [11, 21, 31, 41, 51, 61, 71, 81, 91]
 
# return a range instead of a specific kmer length

def estimateOptKmerLen(reads, kmer_lengths, sample_size=4): # also used by kmergenie
  """
  Estimates the optimal k-mer length for de novo assembly using sampling.

  Args:
      reads: A list of DNA sequencing reads (strings).
      k_min: Minimum k-mer length to consider (default: 15).
      k_max: Maximum k-mer length to consider (default: 35).
      sample_size: Number of reads to sample for k-mer counting (default: 10000).

  Returns:
      The estimated optimal k-mer length and its corresponding k-mer count distribution.
  """

  # Sample reads for k-mer counting
  sampled_reads = random.sample(reads, sample_size)

  # Initialize empty dictionary for k-mer counts
  kmer_counts = Counter()

  # Explore k-mer lengths within the specified range
  for k in kmer_lengths:
    for read in sampled_reads:
      for i in range(len(read) - k + 1):
        kmer = read[i:i+k]
        kmer_counts[kmer] += 1

  # Visualize kmer abundance histogram
  plt.hist(kmer_counts.values(), bins=100, color='blue', alpha=0.7)
  plt.show()

  return kmer_counts

# Example usage
reads = ["GGATCTTCCAGCAGACGCTCGGCAAAGTCCTGAATCGCATCGCCTTCCAGCGTTGCCGAAAAGAGCAGGGTCTGTTTACGCCAGCGCGTTTCGCCAGCAA",
         "TTATGAGAGGTTGGTCATATTATCGCGGGGAAACGAACCGAGGATTTGACAAAGCAATGCTGCGCCAACGTCTGGCACATGTTCAACGTAGGCCCGAAAT",
         "GATCGCTAACCTGTTGCTGGCTCCGTACTTCAAGCAAATTGCCGATGACTACCAGCAGGCGCTGCGTGATGTCGTTGGTTATGCAGTA",
         "AGGCTTTTGCTTATTAACTTTTATATAATATGTTGTTAATACCCCCAACA",
         "CCAGCAGGCTGGCATTTCCTCCTTACCCTTTTAACTCCTTGTTATTGTGC",
         "GTATTTCTATGTTATGTTTATAAATATTTTCTGGTGGTTTTGGATTATTA",
          "TCTGCTTCCTCCATTTGTATTAGAAACATGATGGTAGACTTTGCTTTGTT",
          "AGCTAATGTAACCCTGGTGCCTAGAATAATCCTTTGCACATAGTAGCATC",]
optimal_k, kmer_counts = estimateOptKmerLen(reads)

print(f"Estimated optimal k-mer length: {optimal_k}")
# You can analyze the kmer_counts dictionary further
