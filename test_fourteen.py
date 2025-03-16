from unittest import TestCase
import fourteen

class Taketest(TestCase):
    def test_simple_take(self):
        t = fourteen.take(range(10), 5)
        self.assertEqual(t, [0, 1, 2, 3, 4])

    def test_null_take(self):
        t = fourteen.take(range(10), 0)
        self.assertEqual(t, [])
    
    def test_negative_take(self):
        self.assertRaises(ValueError, lambda: fourteen.take(-3, range(10)))
    
    def test_take_too_much(self):
        t = fourteen.take(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])

class ChunkedTest(TestCase):
    def test_even(self):
        self.assertEqual(list(fourteen.chunked('ABCDEF', 3)), [['A', 'B', 'C'], ['D', 'E', 'F']])
    
    def test_odd(self):
        self.assertEqual(list(fourteen.chunked('ABCDE', 3)), [['A', 'B', 'C'], ['D', 'E']])
    
    def test_none(self):
        self.assertEqual(list(fourteen.chunked('ABCDE', None)), [['A', 'B', 'C', 'D', 'E']])
    
    def test_strict_false(self):
        self.assertEqual(list(fourteen.chunked('ABCDE', 3, strict=False)), [['A', 'B', 'C'], ['D', 'E']])

    def test_strict_true(self):
        def f():
            return list(fourteen.chunked('ABCDE', 3, strict=True))
        self.assertRaisesRegex(ValueError, "chunk is not divisible by n", f)
        self.assertEqual(list(fourteen.chunked('ABCDEF', 3, strict=True)), [['A', 'B', 'C'], ['D', 'E', 'F']])
    
    def test_strict_true_size_none(self):
        def f():
            return list(fourteen.chunked('ABCDE', None, strict=True))
        self.assertRaisesRegex(ValueError, "n cannot be None when strict is True", f)

    
