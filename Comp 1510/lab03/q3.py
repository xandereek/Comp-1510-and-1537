# Find and fix the three logic errors.
#
# The program should read the text one character at a time. It should
# count a word when it reaches the word's first character, then
# remember that it is inside the word so it does not count it again.
# A space marks the end of the word. Extra spaces do not add to the count.
#
# Before editing the code, run it twice using these inputs, in order.
# Enter only the text between the quotation marks:
#
#   Test input 1: "red blue"
#   Test input 2: "red   blue sky" (three spaces between red and blue)

text = input("Text: ")
word_count = 0
inside_word = False

for character in text:
    if character == " ":
        inside_word = False
    else:
        if not inside_word:
            word_count += 1
        inside_word = True

print(f"Words: {word_count}")