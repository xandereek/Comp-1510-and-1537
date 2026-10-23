text = input("Text: ")

charecters = len(text)
vowels = 0
spaces = 0
for i in text:
    if i.lower() in "aeiou":
        vowels += 1
    elif i == " ":
        spaces += 1

print(f"Charecters: {charecters}")
print(f"Vowels: {vowels}")
print(f"Spaces: {spaces}")