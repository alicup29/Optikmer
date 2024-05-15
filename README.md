# Optikmer
Project for CSE 185

Group Members:
Steven Nguyen A16858016
Amick Licup A17038320
Annapurna Saladi A17417895

Description:
Given a set of reads in the form of fastq files, Optikmer will compute the k-mer abundance histogram for many values of k. Then, it predicts the number of distinct k-mers in the dataset and returns the k-mer length that maximizes this number. Optikmer will be compared to kmerGenie and jellyfish. We will implement Optikmer using a Python script, including its libraries Collections, Matplotlib, and potentially more. 

Benchmarking:
For benchmarking, we will compare our tool’s results to kmergenie as seen in lab 2 with the same datasets, as well as comparing their runtimes to estimate how it can be improved. Specifically against kmergenie and jellyfish to display the histograms.


Test Dataset:
We plan to test our tool against the data in the C. elegans data set found on the NCBI (National Center for Biotechnology Information) SRA (short read archive) site.
https://www.ncbi.nlm.nih.gov/sra/SRX24381198[accn]

