import unittest 
from fizzbuzz import fizzbuzz as fb



class TestFizzBuzz(unittest.TestCase):
    list = [0]*100
    for i in range(100): 
        list[i] = i+1


    def test_corrrectness(self):
        self.assertEqual(fb(), self.list)
        
   

if __name__ == '__main__': 
	unittest.main()
