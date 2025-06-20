sample_prefix = int(input('Enter the lab sample ID: '))
sample_format=""
n = int(input("Enter the number of IDs you have to generate: "))
ids = []
for i in range(0,n):
    sample_format=(f"LAB2025-0{sample_prefix+1}")
    ids.append(sample_format)
    sample_prefix+=1

print(ids)
