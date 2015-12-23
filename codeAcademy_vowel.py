
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
    print "".join(final_string) # creates the string by joining the list elements

user_input = str(raw_input("Insert string you wish to remove the vowels: "))
anti_vowel(user_input)

# Below a working version to post on the site:

def anti_vowel(text):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res=[]
    for i in text:
        if i not in vowel:
            res.append(i)
    return ''.join(res)