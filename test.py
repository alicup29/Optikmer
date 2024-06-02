# def kMers(tSeq, k):
#   kFreq = set()
#   for i in range(0, len(tSeq) - k + 1):
#     kFreq.add(tSeq[i:i+k])
#   return len(kFreq)

# tSeq = ""
# with open("DNA.txt", "r") as f:
#   for line in f:
#     if line.startswith(">"):
#       continue
#     tSeq += line.strip()

# max_unique_kmers = 0
# max_k = 0

# for k in range(1, 100):
#   num_kmers = kMers(tSeq, k)
#   if num_kmers > max_unique_kmers:
#     max_unique_kmers = num_kmers
#     max_k = k

# reads = ["GGATCTTCCAGCAGACGCTCGGCAAAGTCCTGAATCGCATCGCCTTCCAGCGTTGCCGAAAAGAGCAGGGTCTGTTTACGCCAGCGCGTTTCGCCAGCAA",
#          "TTATGAGAGGTTGGTCATATTATCGCGGGGAAACGAACCGAGGATTTGACAAAGCAATGCTGCGCCAACGTCTGGCACATGTTCAACGTAGGCCCGAAAT",
#          "GATCGCTAACCTGTTGCTGGCTCCGTACTTCAAGCAAATTGCCGATGACTACCAGCAGGCGCTGCGTGATGTCGTTGGTTATGCAGTA"]

# print(f"Max unique kmers: {max_unique_kmers} when k = {max_k}")

# testseq = "GGATCTTCCAG"
# i = 5
# k = 12
# print(testseq[i:i+k])

# for i in range(len(testseq) - k + 1):
#   print("ran")

# print("~/Downloads/SRR28691205.fastq.gz".endswith('.gz'))

import os
import subprocess

def jellyfishCount(k, rfile, output_dir):
  rfile = os.path.expanduser(rfile)
  output_file = f"{output_dir}/output.jf"
  histo_file = f"{output_dir}/output.jf.histo"
  
  # Count k-mers with jellyfish
  jellyfish_count_cmd = f"gunzip -c {rfile} | jellyfish count -m {k} -C -s 100M -o {output_file} /dev/fd/0"
  subprocess.run(jellyfish_count_cmd, shell=True, check=True)
  
  # Generate histogram with jellyfish
  jellyfish_histo_cmd = f"jellyfish histo -o {histo_file} {output_file}"
  subprocess.run(jellyfish_histo_cmd, shell=True, check=True)
  
  return histo_file

# Example usage:
print(jellyfishCount(21, "~/Downloads/SRR28691205.fastq", "realdata"))