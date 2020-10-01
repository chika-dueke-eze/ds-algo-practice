def firstNotRepeatingCharacter(s):
    for letter in s:
        letter_count = s.count(letter)
        if letter_count == 1:
            return letter
        elif letter_count > 2:
            continue
    return '_'
