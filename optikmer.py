from collections import Counter
from Bio import SeqIO
import random
import matplotlib.pyplot as plt
import math
import argparse

# Initialize possible k-mer lengths & empty dictionary for k-mer counts
kmer_lengths = [11, 21, 31, 41, 51, 61, 71, 81, 91]
test_kmer_lengths = [18]
test_kmer_lengths_2 = [19]
kmer_counts = Counter()

# plot the distribution of kmer counts for specific kmer length
def plotKmerCounts(k):
  plt.hist(kmer_counts.values(), bins=range(1, 200))
  plt.xlabel('K-mer abundance')
  plt.ylabel('Number of k-mers')
  plt.ylim(0, 200000)
  plt.title(f'k={k}')
  plt.savefig(f'histograms/k{k}.png')
  plt.close()

def getSampleReads(fastq_file):
  reads = []
  record_count = 0
  for record in SeqIO.parse(fastq_file, "fastq"):
    reads.append(str(record.seq))
    record_count += 1
  return random.sample(reads, math.ceil(record_count * 0.75)) # sample 10% of reads
  # return random.sample(reads, 10000) # sample 10000

def recordKmers(reads, kmer_len): # also used by kmergenie
  # Sample reads for k-mer counting
  for read in reads: # 10000 sampled reads of varying lengths 
    for i in range(len(read) - kmer_len + 1): # count each unique kmer in each read
      kmer_counts[read[i:i+kmer_len]] += 1
  plotKmerCounts(kmer_len)

def main():
  # Parse command-line arguments (fastq files)
  parser = argparse.ArgumentParser(description='Estimate the optimal k-mer length for de novo assembly using sampling.')
  parser.add_argument('reads', type=str, help='A list of DNA sequencing reads (strings) in fastq format.')
  args = parser.parse_args()
  
  # Obtain fastq files
  rfiles = args.reads

  # Extract reads from each fastq file with getReads function (defined above)
  # and record it in kmer_counts dictionary
  file_reads = getSampleReads(rfiles)
  for k in kmer_lengths:
    recordKmers(file_reads, k)
    kmer_counts.clear()
  
  # Plot the distribution of kmer counts for each kmer length
    
if __name__ == '__main__':
  main()


# Example usage
# reads = ["GGATCTTCCAGCAGACGCTCGGCAAAGTCCTGAATCGCATCGCCTTCCAGCGTTGCCGAAAAGAGCAGGGTCTGTTTACGCCAGCGCGTTTCGCCAGCAA",
#          "TTATGAGAGGTTGGTCATATTATCGCGGGGAAACGAACCGAGGATTTGACAAAGCAATGCTGCGCCAACGTCTGGCACATGTTCAACGTAGGCCCGAAAT",
#          "GATCGCTAACCTGTTGCTGGCTCCGTACTTCAAGCAAATTGCCGATGACTACCAGCAGGCGCTGCGTGATGTCGTTGGTTATGCAGTA",
#          "AGGCTTTTGCTTATTAACTTTTATATAATATGTTGTTAATACCCCCAACA",
#          "CCAGCAGGCTGGCATTTCCTCCTTACCCTTTTAACTCCTTGTTATTGTGC",
#          "GTATTTCTATGTTATGTTTATAAATATTTTCTGGTGGTTTTGGATTATTA",
#           "TCTGCTTCCTCCATTTGTATTAGAAACATGATGGTAGACTTTGCTTTGTT",
#           "AGCTAATGTAACCCTGGTGCCTAGAATAATCCTTTGCACATAGTAGCATC",]
# optimal_k, kmer_counts = estimateOptKmerLen(reads)

# print(f"Estimated optimal k-mer length: {optimal_k}")
# You can analyze the kmer_counts dictionary further
