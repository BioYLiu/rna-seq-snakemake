GENOMES_DIR='/home/cmb-panasas2/skchoudh/genomes'
OUT_DIR = '/staging/as/skchoudh/rna/HuR_results/human/rna_seq_Penalva_L_01182017'
SRC_DIR = '/home/cmb-panasas2/skchoudh/github_projects/clip_seq_pipeline/scripts'
RAWDATA_DIR ='/staging/as/skchoudh/dna/lai_data/Penalva_L_01182017'
GENOME_BUILD = 'hg38'
GENOME_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/fasta/'+ GENOME_BUILD+ '.fa'
STAR_INDEX = GENOMES_DIR + '/' + GENOME_BUILD + '/star_annotated'
GTF = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.annotation.gtf'
GENE_NAMES = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + GENOME_BUILD+'_gene_names_stripped.tsv'
GENE_LENGTHS = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.coding_lengths.tsv'  #+ GENOME_BUILD+'_gene_lengths.tsv'
DESIGN_FILE = OUT_DIR + '/' + 'human_design.txt'
