import unittest
from typing import List, Tuple

class StringCompressor:
    @staticmethod
    def compress(s: str) -> str:
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if not all(c.islower() for c in s):
            raise ValueError("Input must contain only lowercase letters")
        if not s:
            return ""
            
        result = []
        current_char = s[0]
        count = 1
        
        for next_char in s[1:]:
            if next_char == current_char:
                count += 1
            else:
                result.append(f"{current_char}{count}")
                current_char = next_char
                count = 1
                
        result.append(f"{current_char}{count}")
        return "".join(result)
    
    @staticmethod
    def decompress(s: str) -> str:
        if not s:
            return ""
            
        import re
        if not re.match(r'^([a-z][1-9][0-9]*)+$', s):
            raise ValueError("Invalid format. Expected format: 'a2b3c1'")
            
        result = []
        matches = re.findall(r'([a-z])([1-9][0-9]*)', s)
        
        for char, count in matches:
            count = int(count)
            result.append(char * count)
            
        return "".join(result)

class TestStringCompressor(unittest.TestCase):
    def setUp(self):
        self.compressor = StringCompressor()
        
    def test_basic_compression(self):
        """Test basic compression cases"""
        test_cases = [
            ("aaabb", "a3b2"),
            ("abc", "a1b1c1"),
            ("aaa", "a3"),
            ("a", "a1"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(self.compressor.compress(input_str), expected)
                
    def test_empty_string(self):
        """Test empty string handling"""
        self.assertEqual(self.compressor.compress(""), "")
        self.assertEqual(self.compressor.decompress(""), "")
        
    def test_invalid_input_compression(self):
        """Test invalid inputs for compression"""
        invalid_inputs = [
            ("ABC", ValueError),  # uppercase letters
            ("123", ValueError),  # numbers
            ("aa bb", ValueError),  # spaces
            (123, TypeError),  # non-string
            (None, TypeError),  # None
        ]
        for input_val, expected_error in invalid_inputs:
            with self.subTest(input_val=input_val):
                with self.assertRaises(expected_error):
                    self.compressor.compress(input_val)
                    
    def test_invalid_input_decompression(self):
        """Test invalid inputs for decompression"""
        invalid_inputs = [
            "a0b2",     # zero count
            "abc",      # missing numbers
            "a-1b2",    # negative count
            "A1b2",     # uppercase
            "a1b2c",    # incomplete format
        ]
        for input_val in invalid_inputs:
            with self.subTest(input_val=input_val):
                with self.assertRaises(ValueError):
                    self.compressor.decompress(input_val)
                    
    def test_roundtrip(self):
        """Test compression followed by decompression returns original string"""
        test_strings = [
            "aaabb",
            "abc",
            "aaa",
            "a",
            "",
            "abcdefg",
            "aabbccddeeff",
        ]
        for test_str in test_strings:
            with self.subTest(test_str=test_str):
                compressed = self.compressor.compress(test_str)
                decompressed = self.compressor.decompress(compressed)
                self.assertEqual(test_str, decompressed)
                
    def test_long_sequences(self):
        """Test strings with long repeated sequences"""
        self.assertEqual(self.compressor.compress("a" * 100), "a100")
        self.assertEqual(self.compressor.decompress("a100"), "a" * 100)

if __name__ == '__main__':
    unittest.main(verbosity=2)
