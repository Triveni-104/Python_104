seq1 = input('Enter the first DNA seq: ')
seq2 = input('Enter the second DNA seq: ')

if len(seq1) != len(seq2):
    print("Error: Sequences are not of the same length!")
else:
    indices = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            indices.append(i)
    print(indices)
