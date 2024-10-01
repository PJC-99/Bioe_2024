import os
import logging

# Setup logging to a file
logging.basicConfig(filename='orf_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

# Function to check for an RBS sequence upstream of a start codon
def contains_rbs(sequence, start_pos, rbs_window=20):
    """Checks for a Shine-Dalgarno sequence (AGGAGG) in the upstream region of a start codon."""
    rbs_sequence = "AGGAGG"  # Shine-Dalgarno sequence
    upstream_start = max(0, start_pos - rbs_window)  # Ensure we don't go out of bounds
    upstream_region = sequence[upstream_start:start_pos]  # Extract the upstream region
    
    if rbs_sequence in upstream_region:
        logging.info(f"RBS found in upstream region {upstream_region} before start codon at position {start_pos}")
        return True
    else:
        logging.info(f"No RBS found in upstream region {upstream_region} before start codon at position {start_pos}")
        return False

# Function to read a FASTA file and return the sequence
def load_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        return ''.join(line.strip() for line in fasta_file if not line.startswith('>'))

# Function to identify ORFs across all six reading frames
def discover_orfs_in_six_frames(seq):
    min_codon_length = 100  # ORF must be at least 100 codons long (300 nucleotides)
    forward_frames = [seq[i:] for i in range(3)]  # Forward frames: 0, 1, 2
    reverse_seq = reverse_complement(seq)
    reverse_frames = [reverse_seq[i:] for i in range(3)]  # Reverse frames: 0, 1, 2
    all_frames = forward_frames + reverse_frames

    # Extract all ORFs
    all_orfs = [orf for frame in all_frames for orf in extract_orfs(frame)]

    # Filter ORFs that are at least 100 codons long
    filtered_orfs = [orf for orf in all_orfs if len(orf) // 3 >= min_codon_length]
    
    # Log the number of ORFs before and after filtering
    logging.info(f"Total ORFs found before filtering: {len(all_orfs)}")
    logging.info(f"Total ORFs after filtering (>= 100 codons): {len(filtered_orfs)}")

    return filtered_orfs

# Function to reverse complement a sequence
def reverse_complement(seq):
    complement_map = str.maketrans('ATGC', 'TACG')
    return seq.translate(complement_map)[::-1]

# Function to extract ORFs from a sequence frame with RBS filtering
def extract_orfs(seq, rbs_window=20):
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs, start_pos = [], None

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        if start_pos is None and codon == start_codon:
            # Only consider ORFs if they have an RBS upstream
            if contains_rbs(seq, i, rbs_window):
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
    total_orfs_found = 0  # Count total ORFs across all files
    total_proteins_translated = 0  # Count total translated proteins
    
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
                orf_count = len(orfs)
                total_orfs_found += orf_count
                out_file.write(f"ORFs found in {fasta_file}: {orf_count}\n")
                
                # Print a summary for the current file
                print(f"File: {fasta_file}, ORFs found: {orf_count}")

                # Translate ORFs to proteins and store both DNA ORF and protein
                orf_protein_pairs = translate_orfs_to_proteins(orfs)
                total_proteins_translated += len(orf_protein_pairs)

                # Write the ORFs and proteins to the file (not printing to terminal)
                for i, (orf, protein) in enumerate(orf_protein_pairs, 1):
                    codon_length = len(orf) // 3  # Calculate the ORF length in codons
                    
                    # Write to file (not printed to terminal)
                    out_file.write(f"\nORF {i} (Length: {codon_length} codons): {orf}\n")
                    out_file.write(f"Protein {i}: {protein}\n")

    # Print a final summary of all files processed
    print(f"Total ORFs found: {total_orfs_found}")
    print(f"Total proteins translated: {total_proteins_translated}")

# Main block
if __name__ == "__main__":
    directory_path = "ncbi_dataset/data"  # Directory containing subfolders with FASTA files
    output_file = "all_orfs_and_proteins.txt"  # Output file for ORFs and translations from all folders
    process_fasta_files_in_directory(directory_path, output_file)
