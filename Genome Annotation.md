# Genome annotation results for Q1, Q2


# Question 1
## Given the amino acid sequence:  KVRMFTSELDIMLSVNGPADQIKYFCRHWT*
## What is the number of amino acids in the encoded
## peptide (not including the stop codon)? Additonally, how many bases are
## contained in the open reading frame of the DNA sequence encoding the
## amino acids (including the stop codon)

aas = "KVRMFTSELDIMLSVNGPADQIKYFCRHWT*"

count_aminoacids = len(aas)-1 # Count the amino acids without the stop codon, the substraction accounts for the stop codon

total_counts = (count_aminoacids * 3) + 3 # Count the amino acids with the stop codon (tmes 3 bases, plus 3 for stop codon)

print("Number of amino acids:", total_counts ,   
      "\nTotal_number of nuc bases in the orf (with stop codon):", count_aminoacids)

# Output:

Number of amino acids: 93 
Total_number of nuc bases in the orf (with stop codon): 30

# Question 2
## Run prodigal on one of the genomes you have previously downloaded. Using command line tools, count how many genes were annotated
## (you can use any of the output formats for this but some are easier than others).

### Load the powershell environment with file type .ps1
### Instal powershell with command line in terminal: "sudo apt-get update" if trying to instal the plugin fails
### sudo apt-get update
### sudo apt-get install -y powershell
# Instal Prodigal through the terminal with command line: sudo apt-get install prodigal


Get-ChildItem -Recurse -Filter *.fna -Path "/workspaces/Bioe_2024/ncbi_dataset" | ForEach-Object {
    prodigal -i $_.FullName -o /dev/stdout | Select-String -Pattern "CDS" | Measure-Object -Line
}

### Get-ChildItem -Recurse -Filter *.fna recursively seaches for .fna files in my workspace path given so i dont have to make a new folder with the raw .fna files
### For each object: equivalent to a for loop, it runs prodigal tool, $.FullName uses the path to the .fna file
### I used standard output to make it more organized and easier to read: -o /dev/stdout
### I pipelined it to select the string pattern coding sequences: CDS and measure object lines to count

# Output:

-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1860725 bp seq created, 46.25 pct GC
Locating all potential starts and stops...92480 nodes
Looking for GC bias in different frames...frame bias scores: 1.27 0.19 1.54
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1860725 bp)...done!

-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3284204 bp seq created, 66.61 pct GC
Locating all potential starts and stops...191980 nodes
Looking for GC bias in different frames...frame bias scores: 0.73 0.11 2.16
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2648638 bp)...done!
Finding genes in sequence #2 (412348 bp)...done!
Finding genes in sequence #3 (45704 bp)...done!
Finding genes in sequence #4 (177466 bp)...done!
Lines Words Characters Property
----- ----- ---------- --------
 1866                  
 3248                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2257487 bp seq created, 40.40 pct GC
Locating all potential starts and stops...96476 nodes
Looking for GC bias in different frames...frame bias scores: 2.65 0.14 0.21
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2257487 bp)...done!
 2032                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1830138 bp seq created, 38.15 pct GC
Locating all potential starts and stops...72389 nodes
Looking for GC bias in different frames...frame bias scores: 2.68 0.13 0.19
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1830138 bp)...done!
 1748                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3294955 bp seq created, 57.22 pct GC
Locating all potential starts and stops...213618 nodes
Looking for GC bias in different frames...frame bias scores: 0.83 0.28 1.89
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2117144 bp)...done!
Finding genes in sequence #2 (1177787 bp)...done!
 3152                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1230230 bp seq created, 40.58 pct GC
Locating all potential starts and stops...40543 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1230230 bp)...done!
 1063                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1138011 bp seq created, 52.77 pct GC
Locating all potential starts and stops...73375 nodes
Looking for GC bias in different frames...frame bias scores: 2.03 0.23 0.74
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1138011 bp)...done!
 1009                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1667867 bp seq created, 38.87 pct GC
Locating all potential starts and stops...71998 nodes
Looking for GC bias in different frames...frame bias scores: 1.71 0.15 1.14
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1667867 bp)...done!
 1579                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1590815 bp seq created, 43.30 pct GC
Locating all potential starts and stops...51125 nodes
Looking for GC bias in different frames...frame bias scores: 1.67 0.24 1.09
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1551335 bp)...done!
Finding genes in sequence #2 (39456 bp)...done!
 1776                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...4033488 bp seq created, 47.49 pct GC
Locating all potential starts and stops...219838 nodes
Looking for GC bias in different frames...frame bias scores: 2.21 0.16 0.62
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2961149 bp)...done!
Finding genes in sequence #2 (1072315 bp)...done!
 3594                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1042519 bp seq created, 41.31 pct GC
Locating all potential starts and stops...37422 nodes
Looking for GC bias in different frames...frame bias scores: 2.60 0.20 0.20
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1042519 bp)...done!
  897                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1643831 bp seq created, 39.19 pct GC
Locating all potential starts and stops...71171 nodes
Looking for GC bias in different frames...frame bias scores: 1.58 0.14 1.28
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1643831 bp)...done!
 1505                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1234409 bp seq created, 40.57 pct GC
Locating all potential starts and stops...40703 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1229853 bp)...done!
Finding genes in sequence #2 (4532 bp)...done!
 1063                  
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]         
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.     
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2365589 bp seq created, 35.33 pct GC
Locating all potential starts and stops...86378 nodes
Looking for GC bias in different frames...frame bias scores: 2.54 0.16 0.29
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2365589 bp)...done!
 2383


 # Question 3 
## Run prodigal on all of the genomes you have previously downloaded. Using command line tools, find which genome has the highest
## number of genes. Put all your code into a shell script, and put your code
## on the repository on Github where you keep your README with the solutions to this assignment.


### Initialize variables to track the genome with the maximum CDS count

$maxCDS = 0
$maxGenome = ""

# Search for all .fna files in the directory and subdirectories
Get-ChildItem -Recurse -Filter *.fna -Path "/workspaces/Bioe_2024/ncbi_dataset" | ForEach-Object {

### Define the output GFF file name based on the input .fna file name
    $outputGff = "$($_.FullName).gff"

    ###Run Prodigal on the genome file and suppress stdout/stderr output
    prodigal -i $_.FullName -o $outputGff -f gff > $null 2>&1
    
### Count the number of genes (CDS) by searching for "CDS" in the GFF file
    $cdsCount = (Get-Content $outputGff | Select-String -Pattern "CDS").Count

### Display the genome file name and its gene count
    Write-Output "$($_.FullName) has $cdsCount genes."

### Check if this genome has the highest number of genes
    if ($cdsCount -gt $maxCDS) {
        $maxCDS = $cdsCount
        $maxGenome = $_.FullName
    }
}

### Output the genome with the highest number of CDS
Write-Output "Genome with the highest number of genes: $maxGenome ($maxCDS genes)"

# Ouput:
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna has 1866 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna has 3248 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna has 2032 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna has 1748 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna has 3152 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna has 1063 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna has 1009 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna has 1579 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna has 1776 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna has 3594 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna has 897 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna has 1505 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna has 1063 genes.
/workspaces/Bioe_2024/ncbi_dataset/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna has 2383 genes.
Genome with the highest number of genes: /workspaces/Bioe_2024/ncbi_dataset/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna (3594 genes)






























