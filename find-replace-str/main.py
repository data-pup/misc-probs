import unittest

def generate_chunks(input_str, index, source, target, next_index):
    input_chunk = input_str[index:index + len(source)]
    if input_chunk == source:
        chunk_start = index + len(source)
        new_chunk = input_str[chunk_start:next_index]
        return "".join([target, new_chunk])
    else:
        return input_str[index:next_index]

def replace_str(input_str, indexes, sources, targets):
    next_indexes = indexes[1:] + [len(input_str)]
    return "".join([
        generate_chunks(input_str, index, source, target, next_index)
        for (index, source, target, next_index)
        in zip(indexes, sources, targets, next_indexes)
    ])

class TestReplace(unittest.TestCase):
    def test_example_1(self):
        input_str = "abcd"
        indexes = [0, 2]
        sources = ["a", "cd"]
        targets = ["eee", "ffff"]
        expected = "eeebffff"
        self.assertEqual(replace_str(input_str, indexes, sources, targets), expected)

    def test_example_2(self):
        input_str = "abcd"
        indexes = [0, 2]
        sources = ["ab", "ec"]
        targets = ["eee", "ffff"]
        expected = "eeecd"
        self.assertEqual(replace_str(input_str, indexes, sources, targets), expected)