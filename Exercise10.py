my_list = [0, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14]

def get_longest_sequence(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
            if result > longest:
                longest = result
                longest_start_index = start_index
        else:
            result = 1
            start_index = i

    longest_sequence = my_list[longest_start_index:longest_start_index + longest]
    return longest, longest_sequence

longest, longest_sequence = get_longest_sequence(my_list)

print(f"The longest consecutive sequence is of length: {longest}")
print(f"The longest consecutive sequence is: {longest_sequence}")