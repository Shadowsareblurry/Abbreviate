import unittest
import pytest

from kt1.assistant import (
    round_scores,
    above_threshold,
    letter_grades,
    student_ranking,
)


class MakingTheGradeTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_round_scores(self):
        test_data: list[tuple] = [
            tuple(),
            (0.5,),
            (1.5,),
            (90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3),
            (50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0),
        ]

        result_data: list[list[int]] = [
            [],
            [0],
            [2],
            [90, 40, 55, 70, 31, 25, 80, 95, 39, 40],
            [50, 36, 77, 41, 43, 78, 64, 91, 29, 88],
        ]

        for variant, (student_scores, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(
                f"вариация #{variant}", student_scores=student_scores, expected=expected
            ):
                actual_result = round_scores(list(student_scores))
                error_message = (
                    f"Вызов round_scores({list(student_scores)}). "
                    f"После сортировки функция вернула {sorted(actual_result)}, "
                    f"тогда как в тесте ожидался результат {sorted(expected)}. "
                )

                self.assertEqual(
                    sorted(actual_result), sorted(expected), msg=error_message
                )

    @pytest.mark.task(taskno=3)
    def test_above_threshold(self):
        test_data: list[tuple[list[int], int]] = [
            ([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98),
            ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80),
            ([100, 89], 100),
            ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78),
            ([], 80),
        ]

        result_data: list[list[int]] = [[], [88, 91], [100], [88, 91, 78], []]

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(f"вариация #{variant}", params=params, expected=expected):
                actual_result = above_threshold(*params)
                error_message = (
                    f"Вызов above_threshold{params}. "
                    f"Функция вернула {actual_result}, "
                    f"а корректный ответ - это {expected}"
                )

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_letter_grades(self):
        test_data: list[int] = [100, 97, 85, 92, 81]

        result_data: list[list[int]] = [
            [56, 71, 86],
            [55, 69, 83],
            [52, 63, 74],
            [54, 67, 80],
            [51, 61, 71],
        ]

        for variant, (highest, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(f"вариация #{variant}", highest=highest, expected=expected):
                actual_result = letter_grades(highest)
                error_message = (
                    f"Вызов letter_grades({highest}). "
                    f"Функция вернула {actual_result}, "
                    f"тогда как верные границы баллов для перевода - {expected}."
                )

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_student_ranking(self):
        test_data: list[tuple[list[int], list[str]]] = [
            ([82], ["Betty"]),
            ([88, 73], ["Paul", "Ernest"]),
            (
                [100, 98, 92, 86, 70, 68, 67, 60],
                ["Rui", "Betty", "Joci", "Yoshi", "Kora", "Bern", "Jan", "Rose"],
            ),
        ]

        result_data: list[list[str]] = [
            ["1. Betty: 82"],
            ["1. Paul: 88", "2. Ernest: 73"],
            [
                "1. Rui: 100",
                "2. Betty: 98",
                "3. Joci: 92",
                "4. Yoshi: 86",
                "5. Kora: 70",
                "6. Bern: 68",
                "7. Jan: 67",
                "8. Rose: 60",
            ],
        ]

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = student_ranking(*params)
                error_message = (
                    f"Вызов student_ranking{params}. "
                    f"Функция вернула {actual_result}, "
                    f"а правильным ответом было бы {expected}."
                )

                self.assertEqual(actual_result, expected, msg=error_message)
