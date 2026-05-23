def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        word_count = len(words)

        print(f"Total words in '{filename}': {word_count}")

    except FileNotFoundError:
        print("File not found.")


# Example usage
count_words_in_file("my_diary.txt")