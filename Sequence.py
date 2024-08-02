from Bio.Seq import Seq

my_sequence = Seq("AGTACACTGGT")

print(my_sequence.count("A"))
print(my_sequence.count("C"))
print(my_sequence.count("G"))
print(my_sequence.count("T"))
print(my_sequence.count("AGT"))
print(my_sequence.count("TGGT"))

print(my_sequence)
print(my_sequence.complement())
print(my_sequence.reverse_complement())



