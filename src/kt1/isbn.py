def is_valid(isbn: str) -> bool:
    clean = isbn.replace("-", "")
    if len(clean) != 10:
        return False

    total = 0
    for i in range(9):
        if not clean[i].isdigit():
            return False
        total += int(clean[i]) * (10 - i)

    last = clean[9]
    if last == "X":
        total += 10
    elif last.isdigit():
        total += int(last)
    else:
        return False

    return total % 11 == 0
