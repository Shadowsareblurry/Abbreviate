import pytest

from kt1.isbn import (
    is_valid,
)


def test_valid_isbn():
    assert is_valid("3-598-21508-8") == True


def test_invalid_isbn_check_digit():
    assert is_valid("3-598-21508-9") == False


def test_valid_isbn_with_a_check_digit_of_10():
    assert is_valid("3-598-21507-X") == True


def test_check_digit_is_a_character_other_than_x():
    assert is_valid("3-598-21507-A") == False


def test_invalid_check_digit_in_isbn_is_not_treated_as_zero():
    assert is_valid("4-598-21507-B") == False


def test_invalid_character_in_isbn_is_not_treated_as_zero():
    assert is_valid("3-598-P1581-X") == False


def test_x_is_only_valid_as_a_check_digit():
    assert is_valid("3-598-2X507-9") == False


def test_only_one_check_digit_is_allowed():
    assert is_valid("3-598-21508-96") == False


def test_x_is_not_substituted_by_the_value_10():
    assert is_valid("3-598-2X507-5") == False


def test_valid_isbn_without_separating_dashes():
    assert is_valid("3598215088") == True


def test_isbn_without_separating_dashes_and_x_as_check_digit():
    assert is_valid("359821507X") == True


def test_isbn_without_check_digit_and_dashes():
    assert is_valid("359821507") == False


def test_too_long_isbn_and_no_dashes():
    assert is_valid("3598215078X") == False


def test_too_short_isbn():
    assert is_valid("00") == False


def test_isbn_without_check_digit():
    assert is_valid("3-598-21507") == False


def test_check_digit_of_x_should_not_be_used_for_0():
    assert is_valid("3-598-21515-X") == False


def test_empty_isbn():
    assert is_valid("") == False


def test_input_is_9_characters():
    assert is_valid("134456729") == False


def test_invalid_characters_are_not_ignored_after_checking_length():
    assert is_valid("3132P34035") == False


def test_invalid_characters_are_not_ignored_before_checking_length():
    assert is_valid("3598P215088") == False


def test_input_is_too_long_but_contains_a_valid_isbn():
    assert is_valid("98245726788") == False
