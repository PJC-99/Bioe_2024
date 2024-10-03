#!/bin/bash

# Find all .fna files in the current directory and subdirectories
files=$(find . -type f -name "*.fna")

# Check if any .fna files were found
if [ -z "$files" ]; then
    echo "No .fna files found."
    exit 1
fi

# Loop over each genome file
for file in $files; do
    echo "Processing file: $file"

    # Define Prokka output directory and prefix
    output_prokka="prokka_output_$(basename "$file" .fna)"
    prefix_prokka="prokka_genes_$(basename "$file" .fna)"
    gbk_file="$output_prokka/$prefix_prokka.gbk"

    # Run Prokka on the genome file
    echo "Running Prokka for $file..."
    prokka --outdir "$output_prokka" --prefix "$prefix_prokka" --quiet "$file" > /dev/null

    # Check if the Prokka output exists
    if [ -f "$gbk_file" ]; then
        # Count the number of genes annotated by Prokka by counting the lines with "CDS" in the GBK output
        num_genes_prokka=$(grep -c "CDS" "$gbk_file")
        echo "Prokka annotated $num_genes_prokka genes for $file."

        # Output the result to a text file
        echo "$file has $num_genes_prokka genes using Prokka." >> gene_counts_prokka.txt
    else
        echo "Prokka output not found for $file"
    fi
done
