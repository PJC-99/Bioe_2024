# Initialize variables to track the genome with the maximum CDS count
$maxCDS = 0
$maxGenome = ""

# Search for all .fna files in the directory and subdirectories
Get-ChildItem -Recurse -Filter *.fna -Path "/workspaces/Bioe_2024/ncbi_dataset" | ForEach-Object {

    # Define the output GFF file name based on the input .fna file name
    $outputGff = "$($_.FullName).gff"

    # Run Prodigal on the genome file and suppress stdout/stderr output
    prodigal -i $_.FullName -o $outputGff -f gff > $null 2>&1

    # Count the number of genes (CDS) by searching for "CDS" in the GFF file
    $cdsCount = (Get-Content $outputGff | Select-String -Pattern "CDS").Count

    # Display the genome file name and its gene count
    Write-Output "$($_.FullName) has $cdsCount genes."

    # Check if this genome has the highest number of genes
    if ($cdsCount -gt $maxCDS) {
        $maxCDS = $cdsCount
        $maxGenome = $_.FullName
    }
}

# Output the genome with the highest number of CDS
Write-Output "Genome with the highest number of genes: $maxGenome ($maxCDS genes)"
