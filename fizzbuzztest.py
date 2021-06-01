import unittest 
from fizzbuzz import fizzbuzz as fb



class TestFizzBuzz(unittest.TestCase):
    list = [0]*100
    for i in range(100): 
        list[i] = i+1


    def test_original_list(self):
        self.assertEqual(fb(None), self.list)
        
    def test_fizz(self):
        self.assertEqual(fb(66), "Fizz")

    def test_buzz(self):
        self.assertEqual(fb(65), "Buzz")    
   

if __name__ == '__main__': 
	unittest.main()
