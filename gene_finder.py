#Gene Finder tool
###LLM : Chatgpt-4o
###Prompt: "Write a python code to find a single gene in a sequence from a input file in fasta (.fna) format. 
###The output must be a region between start codon 'ATG' and stop codons 'TAA', 'TAG', 'TGA' inside the fasta file and consider three possible reading frames."

# genefinder.py

import os

# Codon table mapping codons to their corresponding amino acids
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

# Function to read a FASTA file and return the sequence
def load_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        return ''.join(line.strip() for line in fasta_file if not line.startswith('>'))

# Function to identify ORFs across all six reading frames
def discover_orfs_in_six_frames(seq):
    forward_frames = [seq[i:] for i in range(3)]  # Forward frames: 0, 1, 2
    reverse_seq = reverse_complement(seq)
    reverse_frames = [reverse_seq[i:] for i in range(3)]  # Reverse frames: 0, 1, 2
    all_frames = forward_frames + reverse_frames
    return [orf for frame in all_frames for orf in extract_orfs(frame)]

# Function to reverse complement a sequence
def reverse_complement(seq):
    complement_map = str.maketrans('ATGC', 'TACG')
    return seq.translate(complement_map)[::-1]

# Function to extract ORFs from a sequence frame
def extract_orfs(seq):
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs, start_pos = [], None

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        if start_pos is None and codon == start_codon:
            start_pos = i
        elif start_pos is not None and codon in stop_codons:
            orf = seq[start_pos:i + 3]
            orfs.append(orf)
            start_pos = None  # Reset after capturing ORF
    return orfs

# Function to find all possible proteins from an ORF
def find_all_proteins(orf):
    proteins = set()  # Use a set to store unique proteins
    for i in range(0, len(orf) - 2, 3):
        codon = orf[i:i+3]
        if codon == 'ATG':  # Start codon
            protein = []
            for j in range(i, len(orf) - 2, 3):
                codon = orf[j:j+3]
                amino_acid = CODON_TABLE.get(codon, '?')
                if amino_acid == '*':  # Stop codon
                    proteins.add(''.join(protein))  # Store the protein sequence in the set
                    break
                protein.append(amino_acid)
    return proteins

# Function to translate ORFs to all possible protein sequences
def translate_orfs_to_proteins(orfs):
    orf_protein_pairs = []  # Store ORF and corresponding protein sequence pairs
    for orf in orfs:
        proteins = find_all_proteins(orf)
        for protein in proteins:
            orf_protein_pairs.append((orf, protein))  # Store ORF and its protein
    return orf_protein_pairs

# Function to process each FASTA file in each folder and write all ORFs and translations to a single text file
def process_fasta_files_in_directory(directory_path, output_file):
    # Open a single output file to store results from all folders
    with open(output_file, 'w') as out_file:
        # Walk through each subdirectory
        for root, dirs, files in os.walk(directory_path):
            folder_name = os.path.basename(root)  # Get the folder name
            
            # Write folder name to the output file
            out_file.write(f"\nProcessing Folder: {folder_name}\n")
            out_file.write("=" * 50 + "\n")
            
            # Filter only .fna files in the current subdirectory
            fasta_files = [f for f in files if f.endswith('.fna')]
            
            # Process each .fna file found
            for fasta_file in fasta_files:
                file_path = os.path.join(root, fasta_file)
                out_file.write(f"\nProcessing file: {fasta_file}\n")
                
                # Load the sequence from the FASTA file
                sequence = load_fasta(file_path)
                out_file.write(f"Sequence loaded from {fasta_file}\n")

                # Find ORFs in six frames
                orfs = discover_orfs_in_six_frames(sequence)
                out_file.write(f"ORFs found in {fasta_file}: {len(orfs)}\n")

                # Translate ORFs to proteins and store both DNA ORF and protein
                orf_protein_pairs = translate_orfs_to_proteins(orfs)

                # Write the ORFs and proteins to the file and print them
                for i, (orf, protein) in enumerate(orf_protein_pairs, 1):
                    # Print ORF DNA and protein translation
                    print(f"\nORF {i} (DNA): {orf}")
                    print(f"Protein {i}: {protein}")
                    
                    # Write to file
                    out_file.write(f"\nORF {i} (DNA): {orf}\n")
                    out_file.write(f"Protein {i}: {protein}\n")

# Main block
if __name__ == "__main__":
    directory_path = "ncbi_dataset/data"  # Directory containing subfolders with FASTA files
    output_file = "all_orfs_and_proteins.txt"  # Output file for ORFs and translations from all folders
    process_fasta_files_in_directory(directory_path, output_file)

# To get the orfs of all 14 genomes you can use cat, less, or nano all_orfs_and_proteins.txt
