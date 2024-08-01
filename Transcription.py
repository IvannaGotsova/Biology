from Bio.Seq import Seq

my_sequence = Seq("AGTACACTGGT")
transcription_sequence = my_sequence.transcribe()

print(my_sequence)
print(transcription_sequence)

