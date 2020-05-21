from unittest import TestCase
import main


# TODO: negative digits

# 1230.00 -> Una mie două sute treizeci lei 00 bani

class NumberToTextTest(TestCase):
    def test_ones(self):
        self.assert_translations({
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
        })

    def test_tens(self):
        self.assert_translations({
            10: "zece",
            20: "douăzeci",
            30: "treizeci",
            40: "patruzeci",
            50: "cincizeci",
            60: "şaizeci",
            70: "şaptezeci",
            80: "optzeci",
            90: "nouăzeci"
        })

    def test_ten_to_twenty(self):
        self.assert_translations({
            11: "unsprezece",
            12: "douăsprezece",
            13: "treisprezece",
            14: "patrusprezece",
            15: "cincisprezece",
            16: "şaisprezece",
            17: "şaptesprezece",
            18: "optsprezece",
            19: "nouăsprezece",
        })

    def test_twenty_to_thirty(self):
        self.assert_translations({
            21: "douăzeci şi unu",
            22: "douăzeci şi doi",
            23: "douăzeci şi trei",
            24: "douăzeci şi patru",
            25: "douăzeci şi cinci",
            26: "douăzeci şi şase",
            27: "douăzeci şi şapte",
            28: "douăzeci şi opt",
            29: "douăzeci şi nouă",
        })

    def test_forty_to_fifty(self):
        self.assert_translations({
            41: "patruzeci şi unu",
            42: "patruzeci şi doi",
            43: "patruzeci şi trei",
            44: "patruzeci şi patru",
            45: "patruzeci şi cinci",
            46: "patruzeci şi şase",
            47: "patruzeci şi şapte",
            48: "patruzeci şi opt",
            49: "patruzeci şi nouă",
        })

    def test_hundreds(self):
        self.assert_translations({
            100: "o sută",
            200: "două sute",
            300: "trei sute",
            400: "patru sute",
            500: "cinci sute",
            600: "şase sute",
            700: "şapte sute",
            800: "opt sute",
            900: "nouă sute",
        })

    def test_hundred_and_smth(self):
        self.assert_translations({
            134: "o sută treizeci şi patru",
            202: "două sute doi",
            384: "trei sute optzeci şi patru",
            480: "patru sute optzeci",
            527: "cinci sute douăzeci şi şapte",
            664: "şase sute şaizeci şi patru",
            795: "şapte sute nouăzeci şi cinci",
            835: "opt sute treizeci şi cinci",
            996: "nouă sute nouăzeci şi şase",
        })

    def test_thousands(self):
        self.assert_translations({
            1_000: "o mie",
            2_000: "două mii",
            3_000: "trei mii",
            4_000: "patru mii",
            5_000: "cinci mii",
            6_000: "şase mii",
            7_000: "şapte mii",
            8_000: "opt mii",
            9_000: "nouă mii",
        })

    def test_thousands_and_smth(self):
        self.assert_translations({
            1_230: "o mie două sute treizeci",
            1_134: "o mie o sută treizeci şi patru",
            2_202: "două mii două sute doi",
            3_384: "trei mii trei sute optzeci şi patru",
            4_480: "patru mii patru sute optzeci",
            5_527: "cinci mii cinci sute douăzeci şi şapte",
            6_664: "şase mii şase sute şaizeci şi patru",
            7_795: "şapte mii şapte sute nouăzeci şi cinci",
            8_835: "opt mii opt sute treizeci şi cinci",
            9_996: "nouă mii nouă sute nouăzeci şi şase",
        })

    def test_thousands_from_ten_to_twenty(self):
        self.assert_translations({
            11_000: "unsprezece mii",
            12_000: "douăsprezece mii",
            13_000: "treisprezece mii",
            14_000: "patrusprezece mii",
            15_000: "cincisprezece mii",
            16_000: "şaisprezece mii",
            17_000: "şaptesprezece mii",
            18_000: "optsprezece mii",
            19_000: "nouăsprezece mii",
        })

    def test_thousands_from_ten_to_twenty_and_smth(self):
        self.assert_translations({
            11_230: "unsprezece mii două sute treizeci",
            11_134: "unsprezece mii o sută treizeci şi patru",
            12_202: "douăsprezece mii două sute doi",
            13_384: "treisprezece mii trei sute optzeci şi patru",
            14_480: "patrusprezece mii patru sute optzeci",
            15_527: "cincisprezece mii cinci sute douăzeci şi şapte",
            16_664: "şaisprezece mii şase sute şaizeci şi patru",
            17_795: "şaptesprezece mii şapte sute nouăzeci şi cinci",
            18_835: "optsprezece mii opt sute treizeci şi cinci",
            19_996: "nouăsprezece mii nouă sute nouăzeci şi şase",
        })

    def test_thousands_under_million(self):
        self.assert_translations({
            111_230: "o sută unsprezece mii două sute treizeci",
            211_134: "două sute unsprezece mii o sută treizeci şi patru",
            312_202: "trei sute douăsprezece mii două sute doi",
            413_384: "patru sute treisprezece mii trei sute optzeci şi patru",
            514_480: "cinci sute patrusprezece mii patru sute optzeci",
            615_527: "şase sute cincisprezece mii cinci sute douăzeci şi şapte",
            716_664: "şapte sute şaisprezece mii şase sute şaizeci şi patru",
            817_795: "opt sute şaptesprezece mii şapte sute nouăzeci şi cinci",
            918_835: "nouă sute optsprezece mii opt sute treizeci şi cinci",
            119_996: "o sută nouăsprezece mii nouă sute nouăzeci şi şase",
        })

    def test_trillions(self):
        self.assert_translations({
            123_612_120_951_100: "o sută douăzeci şi trei trilioane şase sute douăsprezece miliarde o sută douăzeci "
                                 "milioane nouă sute cincizeci şi unu mii o sută"
        })

    def test_too_big(self):
        self.assert_translations({
            9_123_612_120_951_100: "nouă mii o sută douăzeci şi trei trilioane şase sute douăsprezece miliarde o sută douăzeci "
                                 "milioane nouă sute cincizeci şi unu mii o sută"
        })

    def assert_translations(self, assertions):
        for (digit, string) in assertions.items():
            self.assertEqual(string, main.number_to_text(digit))

    def test_orders(self):
        self.assertOrderForNumbers(main.ORDERS_ONES, [0, 3, 10, 13, 40, 99])
        self.assertOrderForNumbers(main.ORDERS_HUNDREDS, [100, 103, 514, 999])
        self.assertOrderForNumbers(main.ORDERS_THOUSANDS, [1_000, 1_030, 5_140, 999_999])
        self.assertOrderForNumbers(main.ORDERS_MILLIONS, [1_000_000, 1_030_000, 5_140_000, 9_999_999])
        self.assertOrderForNumbers(main.ORDERS_TRILLIONS, [13_592_510_000_002])

    def assertOrderForNumbers(self, order, numbers):
        for number in numbers:
            self.assertEqual(order, main.get_order(number))
