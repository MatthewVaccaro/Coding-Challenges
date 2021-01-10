def remove_duplicate_words(s):
    result = []
    for word in s.split(" "):
        if word not in result:
            result.append(word)

    return " ".join(result)

print(remove_duplicate_words(
    'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
