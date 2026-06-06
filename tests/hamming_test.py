import pytest

from kt1.hamming import (
    distance,
)


def test_empty_strings():
    assert distance("", "") == 0


def test_single_letter_identical_strings():
    assert distance("A", "A") == 0


def test_single_letter_different_strings():
    assert distance("G", "T") == 1


def test_long_identical_strings():
    assert distance("GGACTGAAATCTG", "GGACTGAAATCTG") == 0


def test_long_different_strings():
    assert distance("GGACGGATTCTG", "AGGACGGATTCT") == 9


def test_disallow_first_strand_longer():
    with pytest.raises(ValueError) as err:
        distance("AATG", "AAA")

    assert "Strings must be of equal length." in str(err.value)


def test_disallow_second_strand_longer():
    with pytest.raises(ValueError) as err:
        distance("ATA", "AGTG")

    assert "Strings must be of equal length." in str(err.value)


def test_disallow_empty_first_strand():
    with pytest.raises(ValueError) as err:
        distance("", "G")

    assert "Strings must be of equal length." in str(err.value)


def test_disallow_empty_second_strand():
    with pytest.raises(ValueError) as err:
        distance("G", "")

    assert "Strings must be of equal length." in str(err.value)
