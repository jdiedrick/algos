# Runtime O(n)

import unittest

def checkPermutationDict(firstString, secondString):
    if len(firstString) != len(secondString):
        return False

    first_string_character_count = dict()

    for s in firstString:
        if s in first_string_character_count:
            first_string_character_count[s] += 1
        else:
            first_string_character_count[s] = 1

    second_string_character_count = dict()

    for s in secondString:
        if s in second_string_character_count:
            second_string_character_count[s] += 1
        else:
            second_string_character_count[s] = 1

    for s in secondString:
        if s not in first_string_character_count or first_string_character_count[s] != second_string_character_count[s]:
            return False

    return True

def checkPermutationSet(firstString, secondString):
    if len(firstString) != len(secondString):
        return False

    characters = set()

    for s in firstString:
        characters.add(s)

    second_string_character_count = dict()

    for s in secondString:
        if s in second_string_character_count:
            second_string_character_count[s] += 1
        else:
            second_string_character_count[s] = 1

    for s in secondString:
        if s not in first_string_character_count or first_string_character_count[s] != second_string_character_count[s]:
            return False

    return True


class Test(unittest.TestCase):
    
    def test_different_lengths(self):
        firstString = "jo"
        secondString = "johann"
        self.assertEqual(checkPermutationDict(firstString, secondString), False)
    
    def test_different_lengths(self):
        firstString = "jo  "
        secondString = "oj  "
        self.assertEqual(checkPermutationDict(firstString, secondString), True)
    
    def test_correct_permutation(self):
        firstString = "made"
        secondString = "dame"
        self.assertEqual(checkPermutationDict(firstString, secondString), True)
    
    def test_wrong_permutation(self):
        firstString = "madz"
        secondString = "dame"
        self.assertEqual(checkPermutationDict(firstString, secondString), False)

if __name__ == '__main__':
    unittest.main()
