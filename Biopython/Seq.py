from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC

# the Seq object is read-only, like normal python string

'''
for seq_record in SeqIO.parse("data/ls_orchid.fasta", format="fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))



for seq_record in SeqIO.parse(handle="data/ls_orchid.gbk", format="genbank"):
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record))


my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print("%i -- %s"%(index, letter))

print(end = "\n")
print(len(my_seq))

# ono-overlapping count like python string
a = "AAAA".count("AA")
print(a)

b = Seq("AAAA").count("AA")
print(b)


# calculate GC content
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(GC(my_seq))

print(100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq))


# Slicing a sequence
my_seq = Seq("GATCGATGGgcCTATATAGGATCGAAAATCGC")
print(my_seq[4:12])

print(my_seq)
print(my_seq[::-1])

print(str(my_seq))

log1 = "GGCCTAT" in my_seq
log2 = "GGCCTAT" in my_seq.upper()
print(log1)
print(log2)

print(my_seq.complement())
print(my_seq.reverse_complement())


fasta_format_string = "Name\n%s\n"%my_seq
print(fasta_format_string)


# concatenating or adding sequences
protein_seq = Seq("EVRNAK")
dna_seq = Seq("ACTG")
seq = protein_seq + dna_seq
print(seq)
print(dna_seq.lower())
print(dna_seq.upper())


list_of_seq = [Seq("ACTG"), Seq("AACC"), Seq("GGTT")]
concatenated = Seq("")
for s in list_of_seq:
    concatenated += s

print(concatenated)


contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
spacer = Seq("N"*10)
con = spacer.join(contigs)
print(con, end="\n\n")

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
messenger_rna = coding_dna.transcribe()
origin_coding_dna = messenger_rna.back_transcribe()
protein_seq_rna = messenger_rna.translate()
protein_seq_dna = coding_dna.translate()
print(coding_dna)
print(messenger_rna)
print(origin_coding_dna)
print(protein_seq_rna)
print(protein_seq_dna)

print(coding_dna.translate(table="Vertebrate Mitochondrial"))
print(coding_dna.translate(table=2))
print(coding_dna.translate(table="Vertebrate Mitochondrial", to_stop=True))
# specify the stop symbol
print(coding_dna.translate(table = 2, stop_symbol="@"))


gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
           "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
           "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
           "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
           "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")

# in bacterial genetic code GTG is a valid start codon
print(gene.translate(table = "Bacterial", cds=True))



from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]
print(standard_table, end = "\n\n")
print(mito_table)

print(mito_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table)


# Comparing Seq Object
from Bio.Seq import Seq
seq1 = Seq("ACGT")
print("ACGT" == seq1)

'''

from Bio.Seq import Seq
unknown_seq = Seq(None, length=10)
# print(unlnown_seq)
print(len(unknown_seq))
# print(unknown_seq)





