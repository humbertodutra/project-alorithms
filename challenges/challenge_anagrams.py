def have_same_chars(str1, str2):
    if len(str1) != len(str2):
        return False
    char_counts1 = [0] * 26
    char_counts2 = [0] * 26
    for i in range(len(str1)):
        char_counts1[ord(str1[i]) - ord('a')] += 1
        char_counts2[ord(str2[i]) - ord('a')] += 1
    return char_counts1 == char_counts2


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    a = have_same_chars(first_string.lower(), second_string.lower())
    return (first_string.lower(), second_string.lower(),  a)


