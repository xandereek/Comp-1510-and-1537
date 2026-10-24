"""
Score words and find the highest-scoring playable word from a letter rack.
"""

from words import WORDS

LETTER_VALUES = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
    "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}


def word_score(word):
    """
    Calculate the total point value of a word.

    :param word: a string representing the word to score
    :return: an integer representing the total point value of the word
    """
    total = 0
    for char in word.upper():
        total += LETTER_VALUES[char]
    return total


def top_words(word_list, count):
    """
    Return the top N highest-scoring words from a word list.

    :param word_list: a list of strings representing candidate words
    :param count: an integer representing the number of top words to return
    :return: a list of strings ordered from highest to lowest score
    """
    scored_tuples = []
    for word in word_list:
        scored_tuples.append((word_score(word), word))

    sorted_tuples = sorted(scored_tuples, reverse=True)

    result = []
    for score, word in sorted_tuples[:count]:
        result.append(word)
    return result


def letter_counts(word):
    """
    Count the frequency of each uppercase letter in a word.

    :param word: a string whose letters will be counted
    :return: a dictionary mapping uppercase letters to their integer counts
    """
    counts = {}
    for char in word.upper():
        counts[char] = counts.get(char, 0) + 1
    return counts


def is_playable(word, rack):
    """
    Determine whether a word can be formed from the letters in a rack.

    :param word: a string representing the target word
    :param rack: a string representing the available letter tiles
    :return: True if the rack has sufficient letters for the word, else False
    """
    word_count = letter_counts(word)
    rack_count = letter_counts(rack)

    for letter in word_count:
        if word_count[letter] > rack_count.get(letter, 0):
            return False
    return True


def shared_letters(word, rack):
    """
    Find the unique uppercase letters shared between a word and a rack.

    :param word: a string representing the target word
    :param rack: a string representing the available letter tiles
    :return: a set of uppercase strings representing common letters
    """
    return set(word.upper()) & set(rack.upper())


def playable_words(rack, word_list):
    """
    Filter a word list to return only words playable from a given rack.

    :param rack: a string representing the available letter tiles
    :param word_list: a list of strings representing candidate words
    :return: a list of strings from word_list that can be played from rack
    """
    valid_words = []
    for word in word_list:
        if is_playable(word, rack):
            valid_words.append(word)
    return valid_words


def best_word(rack, word_list):
    """
    Find the highest-scoring playable word from a word list for a given rack.

    :param rack: a string representing the available letter tiles
    :param word_list: a list of strings representing candidate words
    :return: a string representing the best playable word, or "" if none exist
    """
    valid_words = playable_words(rack, word_list)
    if not valid_words:
        return ""

    highest_word = valid_words[0]
    for word in valid_words:
        if word_score(word) > word_score(highest_word):
            highest_word = word
    return highest_word


def main():
    """
    Drive the word game scoring engine.
    """
    all_words = WORDS

    rack = input("Enter a rack: ")
    print(f"Rack: {rack}")

    highest_word = best_word(rack, all_words)
    print(f"Best word: {highest_word} ({word_score(highest_word)} points)")

    top_five = ", ".join(top_words(all_words, 5))
    print(f"Top 5 words overall: {top_five}")


if __name__ == "__main__":
    main()