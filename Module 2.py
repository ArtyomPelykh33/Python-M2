import random
import string
from collections import Counter

# 1. generate a list of random number of dictionaries(from 2 to 10), key should be a letter in lowercase(from 2 to 5 e.g.), value should be a number(from 0 to 100)
random_list_of_dictionaries = [
    {random.choice(string.ascii_lowercase): random.randint(0, 100) for i in range(random.randint(2, 5))}
    for i in range(random.randint(2, 10))
]

print("Original list of random dictionaries:")
print(random_list_of_dictionaries)

# create a Counter to track how many times each key appears across all dictionaries
key_counter = Counter()
for n in random_list_of_dictionaries:
    key_counter.update(n.keys())

print(key_counter)

# 2. create the common dictionary
common_dict = {}
# track the dictionary number with max value for each key
dict_number = 1

for a in random_list_of_dictionaries:
    for key, value in a.items():
        if key in common_dict:
            # if the key already exists, check if the new value is greater
            if value > common_dict[key][0]:
                common_dict[key] = (value, dict_number) # store the max value and dict number
        else:
            # if the key is not exist, add it
            common_dict[key] = (value, dict_number)
    # increment the dictionary number
    dict_number +=1

print(common_dict)
# create the final dictionary with keys renamed if necessary
final_dict = {
    f"{key}_{idx}" if key_counter[key] > 1 else key: value
    for key, (value, idx)  in common_dict.items()
}

print("Final common dictionary:")
print(final_dict)