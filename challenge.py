
def convertToCleanSet(input_str):
    clean_str = ''.join(c for c in input_str if c.isalnum() or c == ' ').casefold().split()
    return set(clean_str)

def compareSentences(first, second):
    first_set = convertToCleanSet(first)
    second_set = convertToCleanSet(second)

    common_list = list(first_set.intersection(second_set))
    difference_list = list(first_set.symmetric_difference(second_set))

    return common_list, difference_list

if __name__ == '__main__':
    str1 = 'This is a single sentence!'
    str2 = 'This is another sentence.'
    common, difference = compareSentences(str1, str2)
    print(common)
    print(difference)

