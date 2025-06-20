start_id = input('Enter the lab sample ID: ')  # e.g. LAB2025-017
n = int(input("Enter the number of IDs you have to generate: "))

# Extract numeric part and prefix
num_str = start_id.rsplit('-', 1)[1]
num = int(num_str)
prefix = start_id[:-(len(num_str) + 1)]  # everything before the last dash and number

ids = []
for i in range(n):
    new_num = num + i
    new_id = f"{prefix}-{new_num:0{len(num_str)}d}"
    ids.append(new_id)

print(ids)
