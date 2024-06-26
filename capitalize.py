def capitalize_each_word(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

text = input()
capitalized_text = capitalize_each_word(text)
print(capitalized_text)