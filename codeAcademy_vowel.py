
# removes vowel from a string

def anti_vowel(text):
    original_string = text
    final_string = []
    for i in range(0, len(original_string)):
        letter = original_string[i]
        if letter in "aeiouAEIOU":
            continue
        final_string.append(original_string[i])
        i += 1
    print "".join(final_string)

user_input = str(raw_input("Insert string you wish to remove the vowels: "))
anti_vowel(user_input)