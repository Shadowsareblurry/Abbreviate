import pytest
from kt1.essay import (
    capitalize_title,
    check_sentence_ending,
    clean_up_spacing,
    replace_word_choice,
)


@pytest.mark.task(taskno=1)
def test_capitalize_word():
    assert capitalize_title("canopy") == "Canopy"


@pytest.mark.task(taskno=1)
def test_capitalize_title():
    assert capitalize_title("fish are cold blooded") == "Fish Are Cold Blooded"


@pytest.mark.task(taskno=2)
def test_sentence_ending():
    assert check_sentence_ending("Snails can sleep for 3 years.") == True


@pytest.mark.task(taskno=2)
def test_sentence_ending_without_period():
    assert check_sentence_ending("Fittonia are nice") == False


@pytest.mark.task(taskno=3)
def test_remove_extra_spaces_only_start():
    actual_result = clean_up_spacing("  A rolling stone gathers no moss")
    expected = "A rolling stone gathers no moss"
    assert actual_result == expected


@pytest.mark.task(taskno=3)
def test_remove_extra_spaces():
    actual_result = clean_up_spacing("  Elephants can't jump.  ")
    expected = "Elephants can't jump."
    assert actual_result == expected


@pytest.mark.task(taskno=4)
def test_replace_word_choice():
    actual_result = replace_word_choice("Animals are cool.", "cool", "awesome")
    expected = "Animals are awesome."
    assert actual_result == expected


@pytest.mark.task(taskno=4)
def test_replace_word_not_exist():
    actual_result = replace_word_choice("Animals are cool.", "small", "tiny")
    expected = "Animals are cool."
    assert actual_result == expected
