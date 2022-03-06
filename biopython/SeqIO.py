# -*- codeing = utf-8 -*-
# @Time: 3/2/22 10:36 PM
# @Author: YinCY
# @File: SeqIO.py
# @Software: PyCharm

from Bio import SeqIO
from Bio import Entrez
from Bio import ExPASy
from Bio.SeqUtils.CheckSum import seguid
from io import StringIO
from Bio.SeqIO.FastaIO import SimpleFastaParser

# print(help(SeqIO.parse))
# The Bio.SeqIO.parse function returns an iterator which gives SeqRecord
# objects. Iterators are typically used in a for loop.

# for seq_record in SeqIO.parse("data/ls_orchid.gb", format = "genbank"):
#     print(seq_record.id)
#     print(seq_record.seq)
#     print(len(seq_record))


# identifiers = [seq_record.id for seq_record in SeqIO.parse("data/ls_orchid.gb", format = "genbank")]
# print(identifiers)

# record_iterator = SeqIO.parse("data/ls_orchid.gb", format = "genbank")
# first_record = next(record_iterator)
# print(first_record)

# Parsing sequences from the net
## parsing GenBank
'''
Entrez.email = "yinchunyou@153.com"
with Entrez.efetch(
    db = "nucleotide", rettype = "gb", remote = "text", id = "6273291,6273290,6273289"
) as handle:
    for seq_record in SeqIO.parse(handle, "gb"):
        print("%s %s..." % (seq_record.id, seq_record.description[:50]))
        print("Sequence length %i, %i features, from: %s" % (
            len(seq_record),
            len(seq_record.features),
            seq_record.annotations["source"],))


## Parsing SwissProt
with ExPASy.get_sprot_raw('P31240') as handle:
    seq_record = SeqIO.read(handle, "swiss")

print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])


orchid_dict = SeqIO.to_dict(SeqIO.parse("data/ls_orchid.gb", "genbank"))
# print(len(orchid_dict))
# print(list(orchid_dict.keys()))
# print(list(orchid_dict.values()))
print(orchid_dict["KX609598.1"])

'''

# def get_accession(record):
#     parts = record.id.split("|")
#     try:
#         assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "gb"
#         return parts[3]
#     except AssertionError as error:
#         print(error)
#
# orchid_dict = SeqIO.to_dict(sequences=SeqIO.parse("data/ls_orchid.fasta", "fasta"),
#                             key_function=get_accession)
# print(orchid_dict.keys())

# for record in (SeqIO.parse("data/ls_orchid.gb", "genbank")):
#     print(record.id, seguid(record.seq))


# converting between sequence file formats
# records = SeqIO.parse("data/ls_orchid.gb", "genbank")
# count = SeqIO.write(records, "data/my_example.fasta", "fasta")
# print("Converted %i records" % count)

# count = SeqIO.convert("data/ls_orchid.gb", "genbank", "data/my_example.fasta", "fasta")
# print("Converted %i records" % count)

'''
just by changing the filenames and the format names, this code could be used to convert between 
any file formats available in Biopython.
'''

# records = [rec.reverse_complement(id = "rec_" + rec.id, description = "reverse complement") for rec in SeqIO.parse("data/ls_orchid.fasta", "fasta")]
# print(len(records))
# that would create an in memory list of reverse complement records.

# records = (rec.reverse_complement(id = "rec_" + rec.id, description = "reverse complement") for rec in SeqIO.parse("data/ls_orchid.fasta", "fasta"))
# SeqIO.write(records, "data/rev_complement.fasta", "fasta")


'''
when parsing FASTA files, internally Bio.SeqIO.parse() calls the low-level SimpleFastaParser with
file handle. It iterates over the file handle returning each record as a tuple of two strings, the 
title line (everything after the > character) and the sequence (as a plain string).
'''

count = 0
total_len = 0
with open("data/ls_orchid.fasta") as in_handle:
    for title, seq in SimpleFastaParser(in_handle):
        count += 1
        total_len += len(seq)

print("%i records with total sequence length %i" % (count, total_len))



