# -*- codeing = utf-8 -*-
# @Time: 3/2/22 10:36 PM
# @Author: YinCY
# @File: SeqIO.py
# @Software: PyCharm

from Bio import SeqIO

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


