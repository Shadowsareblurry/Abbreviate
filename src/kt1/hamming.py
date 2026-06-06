def distance(string_1: str, string_2: str) -> int:
    if len(string_1) != len(string_2):
        raise ValueError("Strings must be of equal length.")
    count = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            count += 1
    return count
