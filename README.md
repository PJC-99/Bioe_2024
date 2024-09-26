# Foundations of Bioengineering Lab Project Repository
## Go to the Ncbi Dataset website
### Unzipping the File

    $ unzip ncbi_dataset.zip
    
### Unzipped Dataset

    $ [jorgecpd@login509-02-r HW-3]$ unzip ncbi_dataset.zip
    Archive:  ncbi_dataset.zip
      inflating: README.md
      inflating: ncbi_dataset/data/data_summary.tsv
      inflating: ncbi_dataset/data/assembly_data_report.jsonl
      inflating: ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna
      inflating: ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna
      inflating: ncbi_dataset/data/dataset_catalog.json
      inflating: md5sum.txt
      
### Finding the column with the size data

        $ cut -f 1, 11 ncbi_dataset/data/data_summary.tsv
        
### Output of this command

        $ Organism Scientific Name        Size
        Vibrio cholerae O1 biovar El Tor str. N16961    4033464
        Pasteurella multocida subsp. multocida str. Pm70        2257487
        Lactococcus lactis subsp. lactis Il1403 2365589
        Brucella melitensis bv. 1 str. 16M      3294931
        Helicobacter pylori 26695       1667867
        Thermotoga maritima MSB8        1860725
        Deinococcus radiodurans R1 = ATCC 13939 = DSM 20539     3284156
        Treponema pallidum subsp. pallidum str. Nichols 1138011
        Aquifex aeolicus VF5    1590791
        Chlamydia trachomatis D/UW-3/CX 1042519
        Chlamydia pneumoniae CWL029     1230230
        Helicobacter pylori J99 1643831
        Haemophilus influenzae Rd KW20  1830138
        Chlamydia pneumoniae AR39       1229853

### Sorting the list 

        $ inputfilepath="Size_list.txt"
        outputfilepath="sorted_list.txt"
        awk '{print $NF, $0}' $inputfilepath | sort -nr | cut -d" " -f2- > $outputfilepath
        cat $sorted_list.txt"
        Vibrio cholerae O1 biovar El Tor str. N16961    4033464
        Brucella melitensis bv. 1 str. 16M      3294931
        Deinococcus radiodurans R1 = ATCC 13939 = DSM 20539     3284156
        Lactococcus lactis subsp. lactis Il1403 2365589
        Pasteurella multocida subsp. multocida str. Pm70        2257487
        Thermotoga maritima MSB8        1860725
        Haemophilus influenzae Rd KW20  1830138
        Helicobacter pylori 26695       1667867
        Helicobacter pylori J99 1643831
        Aquifex aeolicus VF5    1590791
        Chlamydia pneumoniae CWL029     1230230
        Chlamydia pneumoniae AR39       1229853
        Treponema pallidum subsp. pallidum str. Nichols 1138011
        Chlamydia trachomatis D/UW-3/CX 1042519
        Organism Scientific Name        Size

### Finding the largest and smallest genome 

        $ head -n 1 sorted_list.txt
        Vibrio cholerae O1 biovar El Tor str. N16961    4033464

        $ tail -n 2 sorted_list.txt
        Chlamydia trachomatis D/UW-3/CX 1042519
        Organism Scientific Name        Size

### Outputting only the genome size for largest genome

        $ head -n 1 sorted_list.txt > largestgenome.txt
        cat largestgenome.txt
        cut -f 2 largestgenome.txt > largestgenomenumber
        cat largestgenomenumber
        
        4033464

### Outputting only the genome size for smallest genome

        $ tail -n 2  sorted_list.txt > smallestgenome.txt
        cat smallestgenome.txt
        cut -f 2 smallestgenome.txt > smallestgnumber
        head -n 1 smallestgnumber > smallestgenomenumber
        cat smallestgenomenumber

        1042519

### Finding the number of genomes that contain at least 2+ "c" without the word "coccus"

        $ 

        

        



        


        

        

