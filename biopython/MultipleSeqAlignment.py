# -*- codeing = utf-8 -*-
# @Time: 3/6/22 9:19 PM
# @Author: YinCY
# @File: MultipleSeqAlignment.py
# @Software: PyCharm

from Bio import AlignIO

"""
Note that both Bio.SeqIO and Bio.AlignIO can read and write sequence alignment files. The
appropriate choice will depend largely on what you want to do with the data.

AlignIO.read: turn an alignment file into a single MultipleSeqAlignment object.
AlignIO.parse: iterate over an alignment file as MultipleSeqAlignment objects.
"""

alignment = AlignIO.read("data/PF05356_seed.txt", "stockholm")
# print(alignment)
# print("Alignment length %i" % alignment.get_alignment_length())
# for record in alignment:
#     print("%s -- %s" % (record.seq, record.id))

# for record in alignment:
#     if record.dbxrefs:
#         print("%s %s" %(record.id, record.dbxrefs))

for record in alignment:
    print(record)

