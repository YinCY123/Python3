from Bio.Seq import Seq
from Bio.Seq import MutableSeq

my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
# my_seq[5] = "G"

mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(mutable_seq)
mutable_seq[5] = "G"
print(mutable_seq)

# Note that unlike Seq object, the MutableSeq object's methods like reverse_complement()
# and reverse() act in-suit.

new_seq = Seq(mutable_seq)
print(new_seq)

