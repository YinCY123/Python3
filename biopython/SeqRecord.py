# -*- codeing = utf-8 -*-
# @Time: 3/2/22 9:06 PM
# @Author: YinCY
# @File: SeqRecord.py
# @Software: PyCharm

'''
Immediately “above” the Seq class is the Sequence Record or SeqRecord class, defined
in the Bio.SeqRecord module. This class allows higher level features such as identifiers
and features (as SeqFeature objects) to be associated with the sequence, and is used
throughout the sequence input/output interface Bio.SeqIO
'''


from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import SeqFeature
from Bio.SeqFeature import SeqFeature, FeatureLocation

'''
# print(help(SeqRecord))
simple_seq = Seq("GATC")
simple_seq_r = SeqRecord(seq=simple_seq)
print(simple_seq_r.id)

simple_seq_r.id = "AC12345"
print(simple_seq_r.id)

simple_seq_r.annotations["evidence"] = "None. I just made it up."
print(simple_seq_r.annotations)

simple_seq_r.letter_annotations["phred_quality"] = [40,44,38,30]
print(simple_seq_r.letter_annotations)


# SeqRecord from fasta
record = SeqIO.read(handle="data/NC_005816.1.fasta", format="fasta")
# print(record)
# print(help(record))
print(record.id)
print(record.name)
print(record.description)
print(record.letter_annotations)
print(record.features)


# SeqRecord from GenBank
record = SeqIO.read(handle="data/NC_005816.gb", format="genbank")
# print(record.seq)
# print(record.dbxrefs)
# print(record.id)
print(record.features)
print(len(record.features))
'''

# SeqFeature
'''
The key idea about each SeqFeature object is to describe a region on a parent sequence,
typically a SeqRecord object. That region is described with a location object, typically 
a range between two positions.

This is an attempt to create a General class to hold Reference type information.

A SeqFeature or location object doesn't directly contain a sequence, instead the location
describes how to get this information from the parent sequence.

SeqRecord comparison is deliberately not implemented. Explicitly compare the attributes of 
interest.
'''

# print(help(SeqFeature))
# start_pos = SeqFeature.AfterPosition(position=5)
# end_pos = SeqFeature.BetweenPosition(position=9, left = 8, right = 9)
# my_location = SeqFeature.FeatureLocation(start = start_pos, end = end_pos)
# print(my_location)
# print(my_location.start)
# print(my_location.end)

'''
seq = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
feature = SeqFeature(location=FeatureLocation(start = 5, end = 18), strand = -1, type = "gene")
feature_seq = feature.extract(seq)
print(feature_seq)
print(help(feature))
# print(feature.location)
# print(feature.type)



record = SeqRecord(seq = Seq("MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD"
                             "GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK"
                             "NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM"
                             "SSAC"),
                   id = "gi|14150838|gb|AAK54648.1|AF376133_1",
                   description = "chalcone synthase [Cucumis sativus]")

print(record.format(format="fasta"))
'''


# This format method takes a single mandatory argument, a lower case string which is supported by
# Bio.SeqIO as an output format

# Slicing a SeqRecord
record = SeqIO.read("data/NC_005816.gb",format="genbank")
print(record)
print(len(record))
print(len(record.features))

subrecord = record[4300:4800]
print(len(subrecord))
print(len(subrecord.features))
print(subrecord.features[0])



