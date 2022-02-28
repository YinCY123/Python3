from Bio import SeqFeature

'''
 The key idea about each SeqFeature object is to describe a region on a parent sequence, typically a SeqRecord object.
 That region is described with a location object, typically a range between two positions.
'''


start_pos = SeqFeature.AfterPosition(5)
end_pos = SeqFeature.BetweenPosition(9, left = 8, right = 9)
my_location = SeqFeature.FeatureLocation(start_pos, end_pos)

# print(my_location)
# print(my_location.start)
# print(int(my_location.start))
# print(my_location.end)
# print(int(my_location.end))

exact_location = SeqFeature.FeatureLocation(5, 9)
print(exact_location)





