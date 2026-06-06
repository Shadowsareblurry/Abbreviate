def create_inventory(items: list[str]) -> dict[str, int]:
    res = {}
    for item in items:
        if item in res:
            res[item] += 1
        else:
            res[item] = 1
    return res


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    res = inventory.copy()
    for item in items:
        if item in res:
            res[item] += 1
        else:
            res[item] = 1
    return res


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    res = inventory.copy()
    for item in items:
        if item in res:
            res[item] -= 1
            if res[item] < 0:
                res[item] = 0
    return res


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    res = inventory.copy()
    if item in res:
        del res[item]
    return res


def list_inventory(inventory: dict[str, int]):
    res = []
    for k, v in inventory.items():
        if v > 0:
            res.append((k, v))
    res.sort()
    return res
