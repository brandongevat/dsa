import unittest
import array

# Test all function of array implementation of Stack class
class TestArray(unittest.TestCase):
    def test_stack_initialization(self):
        self.assertEqual(array.Stack(5).top, -1)
        self.assertEqual(array.Stack(5).size, 5)
        self.assertEqual(array.Stack(5).arr, [None, None, None, None, None])

    def test_stack_is_empty(self):
        self.assertEqual(array.Stack(5).isEmpty(), True)
        self.assertEqual(array.Stack(0).isEmpty(), True)
    
    def test_stack_push(self):
        stack = array.Stack(5)
        stack.push(1)
        self.assertEqual(stack.arr[0], 1)
        self.assertEqual(stack.top, 0)
        self.assertEqual(stack.arr, [1, None, None, None, None])
        self.assertEqual(stack.size, 5)

    def test_stack_pop(self):
        stack = array.Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.top, 3)
        self.assertEqual(stack.arr, [1, 2, 3, 4, None])

    def test_stack_underflow(self):
        stack = array.Stack(5)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.peek(), None)

    def test_stack_overflow(self):
        stack = array.Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.push(6), None)
        self.assertEqual(stack.top, 4)
        self.assertEqual(stack.arr, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()