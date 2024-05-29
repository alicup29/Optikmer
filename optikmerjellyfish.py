import time
from Bio import SeqIO
from collections import Counter
from scipy.signal import argrelextrema
import argparse
import matplotlib.pyplot as plt
import math
import numpy as np
import random
import subprocess

def estimateValley(kmer_counts):
    valley = 0
    prev_max = -1
    
    for i in range(1, len(kmer_counts)):
        if prev_max < 0:
            prev_max = kmer_counts[i]
        elif kmer_counts[i] > prev_max:
            valley = i
            return valley
        else:
            prev_max = kmer_counts[i]

    return valley

def getKmerHistogram(histofile, kmer_len, output_dir):
    kmer_counts = {} # Dictionary of count -> number of kmers

    contents = open(histofile).readlines()
    max_xval = 200
    max_yval = 100000
    max_xval_updated = False
    
    for pair in contents:
      entry = pair.split(" ")
      kmer_count = int(entry[0])
      num_kmers = int(entry[1])
      
      kmer_counts[kmer_count] = num_kmers
      
      # For histograms with a large number of kmer counts, limit the x-axis
      if num_kmers < 100 and not max_xval_updated:
        max_xval = kmer_count
        max_xval_updated = True
    
    # Plot the histogram with matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(kmer_counts.keys(), kmer_counts.values())
    ax.set_xlabel("K-mer Abundance")
    ax.set_ylabel("Number of K-mers")
    ax.set_xlim(left=0, right=max_xval)
    ax.set_ylim(bottom=0, top=max_yval)
    plt.savefig(f'{output_dir}/k{kmer_len}.png')
    return kmer_counts

def jellyfishCount(k, rfile, output_dir):
  jellyfish_cmd = f"jellyfish count -m {k} -C -s 100M -o {output_dir}/output.jf {rfile}"
  subprocess.run(jellyfish_cmd.split(), check=True)
  output_file = f"{output_dir}/output.jf"
  histo_file = f"{output_dir}/output.jf.histo"
  jellyfish_cmd = ["jellyfish", "histo", output_file]
  with open(histo_file, "w") as f:
    subprocess.run(jellyfish_cmd, stdout=f, check=True)
  return histo_file

def main():
  # Track time to process each kmer length
  start_time = time.time()

  # Parse command-line arguments (fastq files)
  parser = argparse.ArgumentParser(
            prog='optikmer',
            description='Approximate the optimal k-mer length for de novo assembly.'
            )
  parser.add_argument('reads', 
                      metavar='F', 
                      type=str, 
                      nargs='+',
                      help='Trimmed FASTQ file(s)')
  parser.add_argument('-o', '--output', 
                      type=str, 
                      default='.',
                      help='Output directory to store PNGs and HTML files')
  parser.add_argument('-k', '--kmers',
                      type=int,
                      nargs='+',
                      default=[11, 21, 31, 41, 51, 61, 71, 81, 91],
                      help='K-mer length(s) to test (default: 11-91, skip 10)')
  args = parser.parse_args()
  
  # Obtain fastq files
  rfiles = args.reads
  output_dir = args.output
  kmer_lengths = args.kmers

  # Start HTML file
  html = ['<html><body>']

  # Set up variables to track the best kmer length
  best_unique_kmers = 0
  best_kmer = 0
  unique_kmer_dict = {}

  # Process each kmer length (9 total) for each file read
  for k in kmer_lengths:
    print(f'Processing k={k}', end='')
    for _ in range(3):
      print('.', end='', flush=True)
      time.sleep(0.5)

    for rfile in rfiles: 

      # Count the kmers using jellyfish and generate a histogram
      unique_kmers = 0
      histo_file = jellyfishCount(k, rfile, output_dir)
      kmer_counts = getKmerHistogram(histo_file, k, output_dir)
      valley = estimateValley(kmer_counts)

      for key in kmer_counts.keys():
        if key >= valley:
          unique_kmers += kmer_counts[key]
      print(f'k={k}, unique_kmers={unique_kmers}')
      unique_kmer_dict[k] = unique_kmers
      if unique_kmers > best_unique_kmers:
        best_unique_kmers = unique_kmers
        best_kmer = k

      # Clear the kmer counts for next kmer
      kmer_counts.clear()

  print(f'Best k={best_kmer}, unique_kmers={best_unique_kmers}')

  # Generate HTML report
  kmer_histogram = f'k{best_kmer}.png'
  html.append(f'<h1>Best k={best_kmer}')
  html.append(f'<h2>Unique K-mers: {best_unique_kmers}</h2>')
  html.append(f'<img src="{kmer_histogram}" alt="Histogram for k={best_kmer}"><br>')
  html.append('<h1>All Generated K-mer Histograms</h1>')

  for k in kmer_lengths:
    kmer_histogram = f'k{k}.png'
    html.append(f'<h2>k={k}</h2>')
    html.append(f'<h3>Unique K-mers: {unique_kmer_dict[k]}</h3>')
    html.append(f'<img src="{kmer_histogram}" alt="Histogram for k={k}"><br>')
  html.append('</body></html>')

  # Write HTML file
  with open(f'{output_dir}/optikmer_histogram_report.html', 'w') as f:
    f.write('\n'.join(html))
    print(f'Generated HTML report! ({output_dir}/histogram_report.html)')

  end_time = time.time()
  elapsed_time = end_time - start_time # time in minutes
  minutes = round(elapsed_time / 60, 2)
  if minutes < 60:
    print(f'Finished analysis in: {minutes} minute(s)')
  else:
    print(f'Finished analysis in: {round(elapsed_time / 60, 2)} hour(s)')
  
if __name__ == '__main__':
  main()