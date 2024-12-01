# Specify the file name
file_name = "input.txt"

# Initialize empty lists for the two columns
distances_1 = []
distances_2 = []

# Open and read the file
with open(file_name, "r") as file:
    for line in file:
        # Split the line into two parts
        parts = line.strip().split()
        if len(parts) == 2:  # Ensure there are two columns
            distances_1.append(int(parts[0]))  # Add to first list
            distances_2.append(int(parts[1]))  # Add to second list

# sort the two lists
distances_1.sort()
distances_2.sort()

# subtract the two lists taking the absolute value
diffs = [abs(a - b) for a, b in zip(distances_1, distances_2)]

print(sum(diffs))

# for the second part, we need to make a frequency hashset of the second list,
# where the key is the number and the value is the frequency of the number
freq = {}

for i in distances_2:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# we then need to iterate through the first list and multiply the number by the frequency
# in the second list, and add it to the sum variable. we do not skip even if we've already
# seen the same number multiple times in the first list.
# the number could potentially not be in the second list, so we need to check for that, and
# if it's not there, we just skip it.
sum_ = 0
for i in distances_1:
    if i in freq:
        sum_ += i * freq[i]

print(sum_)