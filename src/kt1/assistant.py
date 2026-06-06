def round_scores(student_scores: list[float | int]) -> list[int]:
    res = []
    for score in student_scores:
        res.append(round(score))
    return res


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    res = []
    for score in student_scores:
        if score >= threshold:
            res.append(score)
    return res


def letter_grades(highest: int) -> list[int]:
    step = (highest - 40) // 4
    return [41 + step, 41 + 2 * step, 41 + 3 * step]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    res = []
    for i in range(len(student_scores)):
        res.append(f"{i + 1}. {student_names[i]}: {student_scores[i]}")
    return res


