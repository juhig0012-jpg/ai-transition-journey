import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = [
    "running",
    "studies",
    "better",
    "children"
]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
#By default, NLTK assumes every word is a noun.

#You should specify the part of speech:
print(lemmatizer.lemmatize("running", pos="v"))
print(lemmatizer.lemmatize("ran", pos="v"))
print(lemmatizer.lemmatize("studies", pos="v"))

words = [
    lemmatizer.lemmatize(word, pos='v')
    for word in words
]
print(words)