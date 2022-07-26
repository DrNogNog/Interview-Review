import unittest
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    mid = (low+high) // 2

    guess = list[mid]
    while low <= high:
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
        if guess == item:
            return mid
    return None

my_list = [1, 3, 5, 7, 9]
class TestBinary(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(binary_search(my_list,5), 2)

if __name__ == '__main__':
    unittest.main()