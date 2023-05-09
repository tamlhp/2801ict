# initialize pattern string
def badCharTable(pattern_string):
    n = len(pattern_string)
    bad_char_table = {}

    for index,charater in enumerate(pattern_string):
        if index != n - 1:    
            bad_char_table[charater] = n - index - 1

    bad_char_table['other_character'] = n
    return bad_char_table

# find the character
def find(text,pattern_string):
    bad_char_table = badCharTable(pattern_string)
    m = len(text)
    n = len(pattern_string)
    i = 0 
    res = []

    while i < m - n + 1:
        for index,character in enumerate(reversed(pattern_string)):
            if character != text[i + n - index - 1]:
                if text[i + n - index - 1] in bad_char_table:
                    i += bad_char_table[text[i + n - index -1]]
                else:
                    i += bad_char_table['other_character']
                break

            if index == n - 1:
                res.append(i)
                i += bad_char_table[text[i + n - index -1]]
    # return the index that the pattern appeared in the text
    return res

if __name__ == '__main__':
    print(find('BESS_KNEW_ABOUT_BAOBABS',"BAOBAB"))