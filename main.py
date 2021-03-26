import re
import unittest


def check_braces(testString):
    cleaned_string = clean_string(testString)
    count = 0
    for s in cleaned_string:
        if s == '{':
            count = count + 1
        else:
            count = count - 1
            if count < 0:
                return False
    if count != 0:
        return False
    else:
        return True


def clean_string(testString):
    # remove all but { and }
    result = re.sub(r'[^{}]', '', testString)
    return result


class TestBracketsMethods(unittest.TestCase):

    def test_clean_string(self):
        self.assertEqual(clean_string("{HelloWorld}"), "{}", 'Not all characters removed')
        self.assertEqual(clean_string("{1234567890}"), "{}", 'Not all characters removed')
        self.assertEqual(clean_string("{!@#$%^&*()_+-=`~<>,.:[]}?/|;)"), "{}", 'Not all characters removed')

    def test_check_braces(self):
        self.assertTrue(check_braces("{}"), 'check_braces method not calculated correctly')
        self.assertFalse(check_braces("}{"), 'check_braces method not calculated correctly')
        self.assertFalse(check_braces("{{{}}}}}"), 'check_braces method not calculated correctly')
        self.assertFalse(check_braces("{{}"), 'check_braces method not calculated correctly')
        self.assertTrue(check_braces(""), 'check_braces method not calculated correctly')
        self.assertFalse(check_braces("{{{{{{{{{{}"), 'check_braces method not calculated correctly')


if __name__ == '__main__':
    unittest.main()
