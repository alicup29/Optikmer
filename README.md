# Optikmer
Optikmer is a demonstration project for CSE 185 for estimating the k-mer length associated with the highest amount of distinct k-mers given one or more (filtered) fastq files. It is inspired by k-mer counting programs such as kmerGenie and jellyfish in terms of using a sampling approach to approximate the best k-mer length for de-novo assembly. See <a href='http://kmergenie.bx.psu.edu/' target='blank'>kmerGenie<a> or <a href='https://github.com/gmarcais/Jellyfish' target='blank'>jellyfish<a> for more references.

# Installation Instructions
Optikmer is a command-line tool that requires several prerequisite libraries to be installed:
```pip install biopython```
```pip install matplotlib```
```pip install scipy```

Once the required libraries are successfully installed, ```optikmer``` can be installed with the following command: (To be added soon)
```python optikmer.py install``` OR ```python3 optikmer.py install```

If successfully installed, please refer to 
```optikmer --help```
for further help.

# Basic Usage
The basic usage of ```optikmer``` is: (To be added soon)
```optikmer [file1.fasta] [file2.fasta]...```

To run ```optikmer``` on a test example using existing repo files:
```optikmer public/shortfrag_trimmed_1.fq```
(For now use: python (or python3) optikmer.py public/shortfrag_trimmed_1.fq for a test

# optikmer options
Optikmer requires at least one filtered/trimmed fastq file. There are no other required options.

# Contributors
Project assembled by:
- Steven Nguyen (ID: A16858016)
- Amick Licup (ID: A17038320)
- Annapurna Saladi (ID: A17417895)
