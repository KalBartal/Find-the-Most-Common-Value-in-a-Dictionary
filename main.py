def find_most_common_value(dictionary):
    freq_dict = {}
    max_freq = 0
    max_val = None
    for key in dictionary:
        if dictionary[key] not in freq_dict:
            freq_dict[dictionary[key]] = 1
        else:
            freq_dict[dictionary[key]] += 1
        if freq_dict[dictionary[key]] > max_freq:
            max_freq = freq_dict[dictionary[key]]
            max_val = dictionary[key]
    return max_val


print(find_most_common_value({'a': 5, 'b': 6, 'c': 7, 'd': 5, 'e': 7}))
