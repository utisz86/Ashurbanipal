# Import last text file
data_dictionary = {}
with open("data_base/key_data_8.txt", 'r', newline='') as f:
    for line in f:
        (key, val) = line.strip('\r\n').split('; ')
        data_dictionary[key] = val
# Decrypt file
# Put into
