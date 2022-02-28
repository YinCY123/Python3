from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


'''
simple_seq = Seq("GATC")
simple_seq_r = SeqRecord(simple_seq)
simple_seq_r.id = "AC12345"
simple_seq_r.description = "make up sequence I wish I could write a paper about"
print(simple_seq_r)
simple_seq_r.annotations["evidence"] = "None. I just made it up."
print(simple_seq_r.annotations)

# per-letter-annotation
simple_seq_r.letter_annotations["phred_quality"] = [40, 40, 38, 30]
print(simple_seq_r.letter_annotations)


# SeqRecord objects from FASTA files
record = SeqIO.read("data/NC_005816.fasta", format="fasta")
print(record, end = "\n\n")

print(record.id)
print(record.name)
print(record.description)
print(record.seq)

print(record.dbxrefs) # a list
print(record.annotations) # a dictionary
print(record.letter_annotations) # a dictionary
print(record.features) # a list
'''

from Bio import SeqIO
record = SeqIO.read("data/NC_005816.gb", "genbank")
# print(record)
# print(type(record))
# print(record.id)
# print(record.name)
# print(record.description)
# print(record.annotations)
# print(len(record.annotations))
# print(record.features)





