from Bio.Seq import Seq

my_sequence = Seq("AGTACACTGGTG")
translation_sequence = my_sequence.translate()

print(my_sequence)
print(translation_sequence)