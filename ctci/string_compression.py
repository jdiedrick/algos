# Runtime O(n)

# Hints #92, #110

import unittest
from collections import OrderedDict
def compress_all(original_string):
    character_count = OrderedDict()
    compressed_string = ""

    for s in original_string:
        if s in character_count:
            character_count[s] += 1
        else:
            character_count[s] = 1

    for key, value in character_count.items():
        compressed_string += key
        compressed_string += str(value)

    if len(compressed_string) > len(original_string):
        return original_string
    
    return compressed_string

def compress(original_string):
    compressed_string = ""
    current_character = ""
    current_count = 0

    for i, s in enumerate(original_string):
        if s == current_character:
            current_count += 1
        else:
            compressed_string += current_character + str(current_count)
            current_character = s
            current_count = 1
    compressed_string += current_character + str(current_count) # return the last one you have

    if len(compressed_string) > len(original_string):
        return original_string

    return compressed_string[1:]

def compress_again(original_string):
    compressed_string = ""
    current_character = ""
    current_count = 0

    for i, s in enumerate(original_string):
        current_count += 1
        if (i + 1 >= len(original_string)) or s != original_string[i+1]: # s can also be original_string[i]
            compressed_string += s
            compressed_string += str(current_count)
            current_count = 0

    if len(compressed_string) > len(original_string):
        return original_string

    return compressed_string

class Test(unittest.TestCase):
    
    def test_compress_all(self):
        string = "aabcccccaaa"
        self.assertEqual(compress_all(string), "a5b1c5")

    def test_compress(self):
        string = "aabcccccaaa"
        self.assertEqual(compress(string), "a2b1c5a3")

    def test_compress_again(self):
        string = "aabcccccaaa"
        self.assertEqual(compress_again(string), "a2b1c5a3")

if __name__ == '__main__':
    unittest.main()
