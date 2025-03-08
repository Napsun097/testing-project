import unittest

def staircase(n, display):
    result = []
    for i in range(1, n + 1):
        # Create the step for the current level
        step = ' ' * (n - i) + display * i
        result.append(step)
    
    # Join the list of strings into the expected multi-line string
    return '\n'.join(result)

class TestStaircase(unittest.TestCase):
    def test_give_4_with_hash_should_return_correct_pattern(self):
        # Arrange
        n = 4
        display = "#"
        expected_output = "   #\n  ##\n ###\n####"  # Properly formatted staircase
        
        # Act
        result = staircase(n, display)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should be:\n{expected_output}, but got:\n{result}')

if __name__ == '__main__':
    unittest.main()
