def have_same_chars(str1, str2):
    if len(str1) != len(str2):
        return False
    char_counts1 = [0] * 26
    char_counts2 = [0] * 26
    for i in range(len(str1)):
        char_counts1[ord(str1[i]) - ord('a')] += 1
        char_counts2[ord(str2[i]) - ord('a')] += 1
    return char_counts1 == char_counts2


def sort_string(s):
    s = list(s)
    n = len(s)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if s[j] < s[min_index]:
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return ''.join(s)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    a = have_same_chars(first_string.lower(), second_string.lower())
    sortedString1 = sort_string(first_string.lower())
    sortedString2 = sort_string(second_string.lower())
    if (a is True):
        return (first_string.lower(), first_string.lower(),  a)
    else:
        return (sortedString1, sortedString2, a)
