sentence = "Hello World! this is a test"
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)