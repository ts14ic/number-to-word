ONES = {
    1: "unu",
    2: "doi",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "şase",
    7: "şapte",
    8: "opt",
    9: "nouă",
    0: "zero"
}

TENS = {
    1: "zece",
    2: "douăzeci",
    3: "treizeci",
    4: "patruzeci",
    5: "cincizeci",
    6: "şasezeci",
    7: "şaptezeci",
    8: "optzeci",
    9: "nouăzeci",
}

TEN_TO_TWENTY = {
    11: "unsprezece",
    12: "douăsprezece",
    13: "treisprezece",
    14: "patrusprezece",
    15: "cincisprezece",
    16: "şasesprezece",
    17: "şaptesprezece",
    18: "optsprezece",
    19: "nouăsprezece",
}

HUNDREDS = {
    1: "o sută",
    2: "două sute",
    3: "trei sute",
    4: "patru sute",
    5: "cinci sute",
    6: "şase sute",
    7: "şapte sute",
    8: "opt sute",
    9: "nouă sute",
}

THOUSANDS = {
    1: "o mie",
    2: "două mii",
    3: "trei mii",
    4: "patru mii",
    5: "cinci mii",
    6: "şase mii",
    7: "şapte mii",
    8: "opt mii",
    9: "nouă mii",
}

TEN_TO_TWENTY_THOUSANDS = {
    11: "unsprezece mii",
    12: "douăsprezece mii",
    13: "treisprezece mii",
    14: "patrusprezece mii",
    15: "cincisprezece mii",
    16: "şasesprezece mii",
    17: "şaptesprezece mii",
    18: "optsprezece mii",
    19: "nouăsprezece mii",
}

MILLIONS = {
    1: "un milion",
    2: "două milioane",
    3: "trei milioane",
    4: "patru milioane",
    5: "cinci milioane",
    6: "şase milioane",
    7: "şapte milioane",
    8: "opt milioane",
    9: "nouă milioane",
}


def number_to_text(number: int) -> str:
    if number < 10:
        return ONES[number]
    elif number < 100:
        if 10 < number < 20:
            return TEN_TO_TWENTY[number]
        else:
            tens, ones = divmod(number, 10)
            if ones != 0:
                return TENS[tens] + " şi " + ONES[ones]
            else:
                return TENS[tens]
    elif number < 1_000:
        hundreds, rest = divmod(number, 100)
        if rest != 0:
            return HUNDREDS[hundreds] + " " + number_to_text(rest)
        else:
            return HUNDREDS[hundreds]
    elif number < 10_000:
        thousands, rest = divmod(number, 1_000)
        if rest != 0:
            return THOUSANDS[thousands] + " " + number_to_text(rest)
        else:
            return THOUSANDS[thousands]
    elif number < 1_000_000:
        thousands, rest = divmod(number, 1_000)
        if rest != 0:
            return number_to_text(thousands) + " mii " + number_to_text(rest)
        else:
            return number_to_text(thousands) + " mii"
    return str(number)
