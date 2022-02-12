from unittest import TestCase
import dp_hw01


class dp_hw01_Test(TestCase):
    def test_check_all_pairs(self):
        palindromes = [
            'a',
            'bb',
            'abcba',
            'aabbccdccbbaa',
            '',
            '12321',
        ]
        not_palindromes = [
            'not',
            'stillnot',
        ]
        for test_str in palindromes:
            self.assertTrue(dp_hw01.is_palindrome(test_str), test_str)
        for test_str in not_palindromes:
            self.assertFalse(dp_hw01.is_palindrome(test_str), test_str)
