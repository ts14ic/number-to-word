from typing import Dict

_ZERO_TO_TWENTY = {
    0: "zero",
    1: "unu",
    2: "doi",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "şase",
    7: "şapte",
    8: "opt",
    9: "nouă",
    10: "zece",
    11: "unsprezece",
    12: "douăsprezece",
    13: "treisprezece",
    14: "patrusprezece",
    15: "cincisprezece",
    16: "şaisprezece",
    17: "şaptesprezece",
    18: "optsprezece",
    19: "nouăsprezece",
}

_TENS = {
    # 1: "zece", // already included in _ZERO_TO_TWENTY
    2: "douăzeci",
    3: "treizeci",
    4: "patruzeci",
    5: "cincizeci",
    6: "şaizeci",
    7: "şaptezeci",
    8: "optzeci",
    9: "nouăzeci",
}

_ORDERS = [
    dict(lowest=0, one="unu", two="doi", many=""),
    dict(lowest=100, one="o sută", two="două sute", many="sute"),
    dict(lowest=1_000, one="o mie", two="două mii", many="mii"),
    dict(lowest=1_000_000, one="un milion", two="două milioane", many="milioane"),
    dict(lowest=1_000_000_000, one="un miliard", two="două miliarde", many="miliarde"),
    dict(lowest=1_000_000_000_000, one="un trilion", two="două trilioane", many="trilioane")
]

ORDERS_ONES = _ORDERS[0]
ORDERS_HUNDREDS = _ORDERS[1]
ORDERS_THOUSANDS = _ORDERS[2]
ORDERS_MILLIONS = _ORDERS[3]
ORDERS_BILLIONS = _ORDERS[4]
ORDERS_TRILLIONS = _ORDERS[5]


def get_order(number: int) -> dict:
    for index, current in enumerate(_ORDERS[:-1]):
        next = _ORDERS[index + 1]
        if current['lowest'] <= number < next['lowest']:
            return current
    return _ORDERS[-1]


def number_to_text(number: int) -> str:
    if number < 20:
        return _ZERO_TO_TWENTY[number]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones != 0:
            return _TENS[tens] + " şi " + _ZERO_TO_TWENTY[ones]
        else:
            return _TENS[tens]
    else:
        order = get_order(number)
        head, rest = divmod(number, order['lowest'])

        if head == 1:
            head = order['one']
        elif head == 2:
            head = order['two']
        else:
            head = number_to_text(head) + " " + order['many']

        if rest != 0:
            return head + " " + number_to_text(rest)
        else:
            return head
