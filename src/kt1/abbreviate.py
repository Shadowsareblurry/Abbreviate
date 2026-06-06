def abbreviate(phrase: str) -> str:
    clean = phrase.replace("-", " ")
    words = clean.split()
    res = ""
    for word in words:
        for char in word:
            if char.isalpha():
                res += char.upper()
                break
    return res
