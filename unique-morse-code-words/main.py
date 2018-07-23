import unittest

morse_translations = {
    'a': ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--.."
}

def encode_morse(s):
    """Encode a string."""
    return ''.join([
        morse_translations[c] for c in s
    ])

def count_unique_morses(words):
    """Count unique encodings."""
    return len({
        encode_morse(word): True for word in words
    })

class TestMorse(unittest.TestCase):
    def test_gin(self):
        """Test that 'gin' gets the right encoding."""
        res = encode_morse('gin')
        self.assertEqual(res, '--...-.')

    def test_gig(self):
        """Test that 'gig' gets the right encoding."""
        res = encode_morse('gig')
        self.assertEqual(res, '--...--.')

    def test_counts(self):
        """Test that blah"""
        cnt = count_unique_morses(["gin", "zen", "gig", "msg"])
        self.assertEqual(cnt, 2)
