from Bio.Seq import Seq

sequence = Seq(
    "gcggccatggctgctttctaauaaatctatgcgtactatgttggatactcaattcggccttgcgtgatgggacacccagccactgcttcttggtccgatgtccacaagtctagagaacttaaatgagatcaaaggacgtcaggacccaagagtttccaatatcgcggcgacagatagaataccacaaagttcccctgatcatcgtgacccatactacacccagaataggctcgcatataatttttgcatacttacgggggcccgatgcactaatgcttgatgagagttttacaaccaatctaatagccgggagcattgtaagaattcacctcgaggtagcgtattgactcgcctacagacgagcgtgctccgacgcaaagtttaaaaaagtgaggatgtcttagttcgtaattttcccggtataaatatatgaccaacattgtctttgacagtgtgatcgtccccataaacacaccgggggatcagcgcgttcttctattgctttagccgaaatcgatgcctccgagtagtcgaagcccaccacaccacctgatcggtacagcagggtgcacgcttggtcgagggccccgccatgccccgccgggaccctttgcaacggcctacgatgcgcggccaagcacttctgcaatctaaatttctgcggtcggatgtgacggcaccgtttgtgaaagtgtaactcctatggagccgccaggccgggcatttatcgaattatagttgctcgtgggagggtctcagtcgacagctctaaaacttaaagccgagtacctagcatgcataaggctataagtcaacgtgcgcacctaccacgacctcggatactaccggggcgaaatagttcattcatctgtttttatacaacgcctctgccaagcgtctccctgacagccctacccacgccctgtataattggagcgttgtttactgtttcgccccgtgtcttctgggcgtcccacagtaacgggaatcactgcctuaaaauaatgcttg")

print(sequence.translate())
print()

sequence = str(sequence)

new_sequence = Seq("")
start_codon = False

for i in range(0, len(sequence), 3):
    sub_sequence = (sequence[i:i + 3])
    if sub_sequence == "atg":
        start_codon = True

    if start_codon:
        new_sequence += sub_sequence

    if sub_sequence == "uaa":
        break


print(new_sequence.translate())
