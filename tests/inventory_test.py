import pytest
from kt1.inventory import (
    create_inventory,
    add_items,
    decrement_items,
    remove_item,
    list_inventory,
)


@pytest.mark.task(taskno=1)
def test_create_inventory():
    actual_result: dict[str, int] = create_inventory(
        ["wood", "iron", "iron", "diamond", "diamond"]
    )

    assert actual_result == {"wood": 1, "iron": 2, "diamond": 2}


@pytest.mark.task(taskno=2)
def test_add_one_item():
    actual_result: dict[str, int] = add_items({"wood": 4, "iron": 2}, ["iron", "iron"])

    assert actual_result == {"wood": 4, "iron": 4}


@pytest.mark.task(taskno=2)
def test_add_multiple_items():
    actual_result: dict[str, int] = add_items(
        {"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"]
    )

    assert actual_result == {"wood": 3, "gold": 3, "diamond": 3}


@pytest.mark.task(taskno=2)
def test_add_new_item():
    actual_result: dict[str, int] = add_items(
        {"iron": 1, "diamond": 2}, ["iron", "wood", "wood"]
    )

    assert actual_result == {"iron": 2, "diamond": 2, "wood": 2}


@pytest.mark.task(taskno=2)
def test_add_from_empty_dict():
    actual_result: dict[str, int] = add_items({}, ["iron", "iron", "diamond"])

    assert actual_result == {"iron": 2, "diamond": 1}


@pytest.mark.task(taskno=3)
def test_decrement_items():
    actual_result: dict[str, int] = decrement_items(
        {"iron": 3, "diamond": 4, "gold": 2},
        ["iron", "iron", "diamond", "gold", "gold"],
    )

    assert actual_result == {"iron": 1, "diamond": 3, "gold": 0}


@pytest.mark.task(taskno=3)
def test_not_below_zero():
    actual_result: dict[str, int] = decrement_items(
        {"wood": 2, "iron": 3, "diamond": 1},
        ["wood", "wood", "wood", "iron", "diamond", "diamond"],
    )

    assert actual_result == {"wood": 0, "iron": 2, "diamond": 0}


@pytest.mark.task(taskno=3)
def test_decrement_items_not_in_inventory():
    actual_result: dict[str, int] = decrement_items(
        {"iron": 3, "gold": 2}, ["iron", "wood", "iron", "diamond"]
    )

    assert actual_result == {"iron": 1, "gold": 2}


@pytest.mark.task(taskno=4)
def test_remove_item():
    actual_result: dict[str, int] = remove_item(
        {"iron": 1, "diamond": 2, "gold": 1}, "diamond"
    )

    assert actual_result == {"iron": 1, "gold": 1}


@pytest.mark.task(taskno=4)
def test_remove_item_not_in_inventory():
    actual_result: dict[str, int] = remove_item(
        {"iron": 1, "diamond": 2, "gold": 1}, "wood"
    )

    assert actual_result == {"iron": 1, "gold": 1, "diamond": 2}


@pytest.mark.task(taskno=5)
def test_list_inventory():
    actual_result: dict[str, int] = list_inventory(
        {"coal": 15, "diamond": 3, "wood": 67, "silver": 0}
    )

    assert actual_result == [("coal", 15), ("diamond", 3), ("wood", 67)]
