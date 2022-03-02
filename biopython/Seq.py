# -*- codeing = utf-8 -*-
# @Time: 3/2/22 8:22 PM
# @Author: YinCY
# @File: Seq.py
# @Software: PyCharm

'''
Biological sequences are the central object in Bioinformatics.
'''

from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.Data import CodonTable
from Bio.Seq import MutableSeq

'''
my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print("%i -- %s"%(index, letter))

print(len(my_seq))
print(my_seq[0])
print(my_seq[1])
print(my_seq[2])

# non-overlaping count
print("AAAA".count("AA"))


my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq.count("G"))
print(GC(my_seq))
print(100 * float(my_seq.count("G") + my_seq.count("C"))/len(my_seq))


# Slicing sequence
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq[4:12])
print(my_seq[0::3])
print(my_seq[1::3])
print(my_seq[2::3])

# reverse an sequence
print(my_seq[::-1])

# formatting a sequence
fasta_format_string = "\n>Name \n%s\n" % my_seq
print(fasta_format_string)

# concatenating
protein_seq = Seq("EVRNAK")
dna_seq = Seq("ACGT")
print(protein_seq + dna_seq)


contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
spacer = Seq("N"*10)
print(spacer.join(contigs))


# changing case
dna_seq = Seq("acgtACGT")
print(dna_seq)
print(dna_seq.upper())
print(dna_seq.lower())


my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq.complement())
print(my_seq.reverse_complement())

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
template_dna = coding_dna.reverse_complement()
messenger_rna = coding_dna.transcribe()
# protein_seq = coding_dna.translate(table = 2)
# protein_seq = coding_dna.translate(table = "Vertebrate Mitochondrial")
# protein_seq = coding_dna.translate(table = "Vertebrate Mitochondrial", to_stop=True)
protein_seq = coding_dna.translate(table = "Vertebrate Mitochondrial", stop_symbol="@")
print(template_dna)
print(messenger_rna)
print(protein_seq)


gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
           "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
           "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
           "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
           "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")
print(gene.translate())
print(gene.translate(table = "Bacterial", cds = True))


standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(standard_table)
print(mito_table)

print(mito_table.start_codons)
print(mito_table.stop_codons)

# comparing Seq objects
seq1 = Seq("ACGT")
print("ACGT" == seq1)


# Sequence with unknown sequence contents
unknown_seq = Seq(None, length = 10)
# print(unknown_seq)
print(len(unknown_seq))


# MutableSeq
# all the method applied to mutable seq are at in-situ
my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
# my_seq[4] = "G"

mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(mutable_seq)
mutable_seq[4] = "G"
print(mutable_seq)

mutable_seq.remove("T")
print(mutable_seq)

mutable_seq.reverse()
print(mutable_seq)

'''




