dna=input("enter dna string:")
for ch in dna:
    if ch in "ATGC":
        A=dna.count('A')
        T=dna.count('T')
        G=dna.count('G')
        C=dna.count('C')
    else:
        print("INVALID")
print({"A":A,"T":T,"G":G,"C":C})

