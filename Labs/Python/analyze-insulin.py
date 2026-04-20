# 1. Read the raw preproinsulin sequence
with open("preproinsulin-seq.txt", "r") as f:
    raw_data = f.read()

# 2. Clean the data: Keep only lowercase letters (a-z)
# This automatically removes "ORIGIN", numbers, spaces, and "//"
cleaned_insulin = "".join(char for char in raw_data if char.islower())

# Verify the count is exactly 110
print(f"Total cleaned sequence length: {len(cleaned_insulin)}")

# 3. Save the full cleaned sequence
with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(cleaned_insulin)

# 4. Extract fragments using string slicing and save them
# lsinsulin: amino acids 1-24
lsinsulin = cleaned_insulin[0:24]
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin)
print(f"lsinsulin length: {len(lsinsulin)}")

# binsulin: amino acids 25-54
binsulin = cleaned_insulin[24:54]
with open("binsulin-seq-clean.txt", "w") as f:
    f.write(binsulin)
print(f"binsulin length: {len(binsulin)}")

# cinsulin: amino acids 55-89
cinsulin = cleaned_insulin[54:89]
with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin)
print(f"cinsulin length: {len(cinsulin)}")

# ainsulin: amino acids 90-110
ainsulin = cleaned_insulin[89:110]
with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin)
print(f"ainsulin length: {len(ainsulin)}")