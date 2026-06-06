def decode(encoded_string: str) -> str:
    res = ""
    count_str = ""
    for char in encoded_string:
        if char.isdigit():
            count_str += char
        else:
            if count_str:
                res += char * int(count_str)
                count_str = ""
            else:
                res += char
    return res


def encode(initial_string: str) -> str:
    if not initial_string:
        return ""
    res = ""
    count = 1
    for i in range(1, len(initial_string)):
        if initial_string[i] == initial_string[i - 1]:
            count += 1
        else:
            if count > 1:
                res += str(count) + initial_string[i - 1]
            else:
                res += initial_string[i - 1]
            count = 1
    if count > 1:
        res += str(count) + initial_string[-1]
    else:
        res += initial_string[-1]
    return res
