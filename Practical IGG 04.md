
# Practical IGG 04

## Finding Genes and linkages with Ensembl Genome Browsers

This practical is done on 03/11/2022, Thursday.

In this practical I've done finding genes and linkages on EGB.

### What is EGB?

EGB (Ensembl Genome Browsers) is browser that provides access to organised information or annotated data from the analysis of biological data, originally stored in several relevant biological databases.

1. In this practical I've explored a region on a genome, a gene and a transcript finding with the help of EGB.
2. With the help of this browser I can able to find/ where to view gene trees, sequence variation, and possible regions involved in gene regulation in Ensembl.
3. I can see particular interest of gene sequence, protein or a genpme in Ensembl.
4. I've learned different ways to present the results in Ensembl (including the gene, location, transcript and variation tabs)

This practical devided into two parts.

## Part 1 Exploring EGB

### Genesand transcripts: The gene tab

In this section, I'm using the human ESPN gene to explore the basic architecture of EGB. This gene encodes a multifunctional actin-bundling protein with a major role in mediating sensory transduction in various mechanosensory and chemosensory cells. Mutations in this gene are associated with deafness.

### Procedure:

### 1. First of all went at, https://www.ensembl.org/index.html link. 
On the main page of EGB, in the search bar I've typed ESPN and clicked on go button and I've got a list of hits with the human gene at the top.

### 2. Clicked on the gene name or Ensembl ID (Link). 

### 3. Explored the some of the links in the left-hand navigation column. 

1. To view the genomic sequence clicked on Sequence at the left of the page.
2. The sequence is shown in FASTA format. Examine the FASTA file header.
3. To show Variations, clicked on ‘Configure this page’ link found at the left. 
4. Went to ‘Show variations’ and select ‘Yes show links) ➔then go to Line numbering and select Relative to sequence, ➔click at the top right(Save and close)
5. To check if my gene is found in other databases, so went to the left-hand menu and select External references. This contains links to the gene in other projects, such as EntrezGene.
6. To find out more about the individual transcripts of this gene, 
7. clicked on Transcript comparison in the left-hand menu
8. Then scroll down to the bottom of the menu (on the left) ➔clicked on‘Select transcripts button’to choose the transcripts I liked to see.
9. Selected protein-coding transcripts, then close the menu.


### 4. Explored the transcript tab

1. To explore one splice isoform. Clicked on Show transcript table at the top.
2. Clicked on the ID for the ESPN-217(ENST00000645284.1)
In the Transcript tab for ESPN-217, in the left hand navigation column provides several options for the transcript ESPN-217. Clicked on the Exons link.
3. To change the display (for example, to show more flanking sequence, or to show full introns), went to and clicked on Configure this page➔change the display options accordingly.
4. Data download: to export the sequence, including the colours, clicked Download view as RTF. A Rich Text Format document generated that can be opened in word processor such as MS Word.
5. Then clicked on the cDNA link to see the spliced transcript sequence.
6. UnTranslated Regions (UTRs) are highlighted in dark yellow, 
7. codons are highlighted in light yellow, and 
8. exon sequence is shown in black or blue letters to show exon divides. 
9. Sequence variants are represented by highlighted nucleotides and clickable IUPAC codes are above the sequence.

### 5. General identifiers link at the left.

This page saw information from other databases such as RefSeq, UniProtKB, CCDS and others, that match to the Ensembl transcript and protein.
1. In the Gene tab, clicked on GO table to see GO terms from the Gene Ontology consortium. www.geneontology.org
2. Clicked on the to see a guide to the three-letter evidence codes.
3. In the Transcript tab, clicked on Protein summaryto view domains from Pfam, PROSITE, Superfamily, InterPro, and more.
4. Clicked on Domains & featuresto show a table of this information.

From performing procedure stated above found following results, which I've added as an image.

![Screenshot%202022-11-04%20094653.png](attachment:Screenshot%202022-11-04%20094653.png)

![Screenshot%202022-11-04%20094721.png](attachment:Screenshot%202022-11-04%20094721.png)

## Part 2: Linkage Analysis

### Linkage disequilibrium

A measure of how often two variants or specific sequences are inherited together.

## r2:  

The correlation between a pair of loci. It varies from 0 (loci are in completelinkageequilibrium, i.e., are independent) to 1 (loci are in completelinkagedisequilibrium and coinherited).

## D': 

The difference between the observed and the expected frequency of a given haplotype. If two loci are independent (i.e. inlinkageequilibrium and therefore not coinherited at all), the D' value will be 0

Gene variant rs2708377 has been associated with perceived bitterness of caffeine, in the PEL (Peruvian in Lima, Peru) population of the 1000 Genomes project. 

In this experiment, I've explored following aspects:

•Linkage Disequilibrium (LD)in the Ensembl genome browser

•Pairwise LD data by population -with rs10772420 associated with perceived bitterness of quinine 

•LD Manhattan plot 

•Variants in high LD, LD plot andLD table

## 1.Experiment 1: Finding Pairwise LD between 2 variants

### Procedure:

1. Went to Linkage Disequilibrium Calculator (https://www.ensembl.org/Homo_sapiens/Tools/LD?db=core;g=ENSG00000215912;r=1:2635976-2801717) 

2. Select New job ➔ Choose Calculation: select LD for a given list of variants ➔ provide a name for your job ➔ select Homo sapien as species ➔ select the population of interest, e.g., PEL population ➔ Type rs2708377and rs10772420 in two rolls in the paste data section

3. Scroll down and set r2 to 0 and D’ also to 0 ➔ then click on run

4. When job is completed clicked to view results: r2 and D’ for the different populations vary indicating that taste of bitterness differ between populations.

5. Narrow the result down to PEL ➔ scroll down to PEL population and examine the results.

## 2.Experiment 2: Finding variants in Linkage Disequilibrium (LD) with a candidate variant in the Ensembl genome browser 

### Procedure:

1. Go to EGB at https://www.ensembl.org/index.html

2. At the ensembl.org main page, typed rs2708377 into the search bar ➔ clicked the Go button. I got 1 variant for human.

3. Clicked on the link to open the variant tab

4. I've noticed a message that states “this variant maps to 3 locations”

5. Clicked on the drop-down menu for ‘Select a location’ and select location: 12:11063716 (forward strand)

6. Then scrolled down to the ‘Explore this Variant, section and click on Linkage Disequilibrium tab

7. In the Linkage Disequilibrium tab selected Peruvian in Lima, Perupopulation (PEL)

8. Clicked on LD Manhattan Plot for PEL

9. Clicked on Variants in High LD for PEL

10. Clicked on LD plot for PEL

## Question-Answers

1. What is the r2, and D’ for the variant in PEL population?

    The r2 for the variant in PEL population is 0.04 and D’ is 0.99.

2. What neighbouring variants are in LD, and which ones are not in LD?

    The variants in LD with rs2708377 are rs267606674, rs267606675, and rs267606676. The variant that is not in LD with rs2708377 is rs267606677.

3. How many variants are in high LD?

    There are two variants in high LD.

4. Which variants are in linkage disequilibrium with rs2708377

    There is no definitive answer to this question as it can vary depending on the population that is being studied. However, some of the variants that have been associated with rs2708377 in previous studies include: rs1051730, rs12562034, and rs11614913.

### Activity 2:

### rs4778138

LD Manhattan plot

![Human_rs4778138.png](attachment:Human_rs4778138.png)

Variants in high LD

![Screenshot%202022-11-05%20161450.png](attachment:Screenshot%202022-11-05%20161450.png)

LD plot

![MNTITQZBRWLLCDIaTcAAAZMQ.png](attachment:MNTITQZBRWLLCDIaTcAAAZMQ.png)

LD table

http://Oct2022.archive.ensembl.org/Homo_sapiens/Export/Output/Location?_format=HTML;db=core;output=ld;pop1=1000GENOMES:phase_3:PEL;r=15:28080674-28100673;v=rs4778138;vdb=variation;vf=105005685

### rs1129038

![Human_rs1129038.png](attachment:Human_rs1129038.png)

![Screenshot%202022-11-05%20163507.png](attachment:Screenshot%202022-11-05%20163507.png)

![Human_1528101713_28121712.png](attachment:Human_1528101713_28121712.png)

http://Oct2022.archive.ensembl.org/Homo_sapiens/Export/Output/Location?_format=HTML;db=core;output=ld;pop1=1000GENOMES:phase_3:PEL;r=15:28101713-28121712;v=rs1129038;vdb=variation;vf=104142096

### rs1667394

![Human_rs1667394.png](attachment:Human_rs1667394.png)

![Screenshot%202022-11-05%20164202.png](attachment:Screenshot%202022-11-05%20164202.png)

![Human_1528275036_28295035.png](attachment:Human_1528275036_28295035.png)

http://Oct2022.archive.ensembl.org/Homo_sapiens/Export/Output/Location?_format=HTML;db=core;output=ld;pop1=1000GENOMES:phase_3:PEL;r=15:28275036-28295035;v=rs1667394;vdb=variation;vf=104265713

### rs11855019

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28090174-28091174;v=rs4778138;vdb=variation;vf=105005685

### rs1800401

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28014407-28015407;v=rs1800401;vdb=variation;vf=104286920

### rs12913823

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:50216894-50217894;v=rs12913823;vdb=variation;vf=106659038

### rs12913832

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28119972-28120972;v=rs12913832;vdb=variation;vf=106659100

### rs4778241

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28093067-28094067;v=rs4778241;vdb=variation;vf=105007137

### rs7495174

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28098592-28099592;v=rs7495174;vdb=variation;vf=105501887

### rs1408799

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=9:12671597-12672597;v=rs1408799;vdb=variation;vf=729237650

### rs1800407

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:27984672-27985672;v=rs1800407;vdb=variation;vf=104287054

### rs4911442

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=20:34766743-34767743;v=rs4911442;vdb=variation;vf=177320227

### rs4911414

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=20:34141138-34142138;v=rs4911414;vdb=variation;vf=177319915

### rs7495174

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28098592-28099592;v=rs7495174;vdb=variation;vf=105501887

### rs916977

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28267718-28268718;v=rs916977;vdb=variation;vf=104045380

### rs6497268

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:28093067-28094067;v=rs4778241;vdb=variation;vf=105007137

### rs2733832

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=9:12704225-12705225;v=rs2733832;vdb=variation;vf=729668678

### rs1800414

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=15:27951391-27952391;v=rs1800414;vdb=variation;vf=104287181

### rs6058017

https://www.ensembl.org/Homo_sapiens/Variation/HighLD?db=core;r=20:34268692-34269692;v=rs6058017;vdb=variation;vf=177772917

This way I've found all the varients accordingly.

Practical Ended.
