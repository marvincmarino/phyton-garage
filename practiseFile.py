

# reverse string:
# given a input string the code should invert it

def reverse(text):
    inverted_text = ""
    text_len = len(text)
    for i in range(0, text_len):
        inverted_text = inverted_text + text[text_len-i-1] # looping backward
        print "iteration: %i, letter: %s " % (i,inverted_text)
        i += 1
    print(inverted_text)


# user input
text = raw_input("Insert a text you want to revert:")
reverse(text)
