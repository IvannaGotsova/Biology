from Bio.Seq import Seq

dna_sequence = Seq("gcggccgctgctttctaaatctatgcgtactaaatgttggatactcaattcggccttgcgtgatgggacacccagccactgcttcttggtccgatgtccacaagtctagagaacttaaatgagatcaaaggacgtcaggacccaagagtttccaatatcgcggcgacagatagaataccacaaagttcccctgatcatcgtgacccatactacacccagaataggctcgcatataatttttgcatacttacgggggcccgatgcactaatgcttgatgagagttttacaaccaatctaatagccgggagcattgtaagaattcacctcgaggtagcgtattgactcgcctacagacgagcgtgctccgacgcaaagtttaaaaaagtgaggatgtcttagttcgtaattttcccggtataaatatatgaccaacattgtctttgacagtgtgatcgtccccataaacacaccgggggatcagcgcgttcttctattgctttagccgaaatcgatgcctccgagtagtcgaagcccaccacaccacctgatcggtacagcagggtgcacgcttggtcgagggccccgccatgccccgccgggaccctttgcaacggcctacgatgcgcggccaagcacttctgcaatctaaatttctgcggtcggatgtgacggcaccgtttgtgaaagtgtaactcctatggagccgccaggccgggcatttatcgaattatagttgctcgtgggagggtctcagtcgacagctctaaaacttaaagccgagtacctagcatgcataaggctataagtcaacgtgcgcacctaccacgacctcggatactaccggggcgaaatagttcattcatctgtttttatacaacgcctctgccaagcgtctccctgacagccctacccacgccctgtataattggagcgttgtttactgtttcgccccgtgtcttctgggcgtcccacagtaacgggaatcactgcctaatgcttgg")

rna_sequence = dna_sequence.transcribe()

protein_sequence = rna_sequence.translate()

print(protein_sequence)