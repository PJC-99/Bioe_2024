#Gene Finder tool
###LLM : Chatgpt-4o
###Prompt: "Write a python code to find a single gene in a sequence from a input file in fasta (.fna) format. 
###The output must be a region between start codon 'ATG' and stop codons 'TAA', 'TAG', 'TGA' inside the fasta file and consider three possible reading frames."

# genefinder.py

import os
from Bio import SeqIO

# Define start and stop codons
START_CODON = "ATG"
STOP_CODONS = {"TAA", "TAG", "TGA"}

def find_gene_in_frame(sequence, frame):
    """
    This function finds a gene in a specific reading frame.
    The gene is considered to be the region between a start codon (ATG)
    and the first valid stop codon (TAA, TAG, TGA) in the same reading frame.
    """
    seq_in_frame = sequence[frame:]
    
    for i in range(0, len(seq_in_frame) - 2, 3):
        codon = seq_in_frame[i:i+3]
        
        if codon == START_CODON:
            for j in range(i + 3, len(seq_in_frame) - 2, 3):
                stop_codon = seq_in_frame[j:j+3]
                if stop_codon in STOP_CODONS:
                    return seq_in_frame[i:j+3]
    
    return None

def find_gene_in_sequence(sequence):
    for frame in range(3):
        gene = find_gene_in_frame(sequence, frame)
        if gene:
            return gene, frame
    return None, None

def read_fasta_and_find_gene(fasta_file):
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq).upper()
        
        gene, frame = find_gene_in_sequence(sequence)
        
        if gene:
            print(f"Gene found in reading frame {frame + 1} in file {fasta_file}:")
            print(gene)
        else:
            print(f"No gene found in the sequence of file {fasta_file}.")

def process_all_fasta_files(main_directory):
    """
    This function traverses the 'fasta_files' folder, opens each FASTA file in its respective folder,
    and applies the gene-finding function.
    """
    # Path to the 'fasta_files' folder
    fasta_dir = os.path.join(main_directory, "ncbi_dataset/data")
    
    # List all folders in 'fasta_files'
    for folder in os.listdir(fasta_dir):
        folder_path = os.path.join(fasta_dir, folder)
        
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder}")
            
            # List all files in the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".fna"):  # Ensure we only pick FASTA files
                    fasta_file = os.path.join(folder_path, file_name)
                    
                    # Call the function to read and process the FASTA file
                    read_fasta_and_find_gene(fasta_file)

# Example usage
if __name__ == "__main__":
    # Define the main directory (the root directory where the script is)
    main_directory = os.getcwd()  # Get the current working directory (should be 'main')
    
    # Process all FASTA files inside each folder in 'fasta_files'
    process_all_fasta_files(main_directory)

