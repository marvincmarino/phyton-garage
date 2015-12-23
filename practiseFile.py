

# reverse string:
# given a input string the code should invert it

def reverser(text):
    inverted_text = []
    text_len = len(text)
    for i in range(text_len, 0):
        for j in range(1, text_len):
            inverted_text.append(text[j])
            i -= 1
            j += 1
    print(inverted_text)


# user input
text = raw_input("Insert a text you want to revert:")
reverser(text)
