
# Write a function that giving a word calculates the scrabble score based on the dictionary

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(text):
    input_string = text.lower()
    final_score = 0
    for letter in input_string:
        final_score = final_score + score[letter]
    print(final_score)

user_text = raw_input("Give me the scrabble word: ")
scrabble_score(user_text)

# Below working version to use on the website:

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


entry = str(raw_input("What's your word?"))

def scrabble_score(word):
    word = word.lower()
    points = 0
    for char in word:
        points += score[char]
    return points

print scrabble_score(entry)