import unittest 
from leap_year_tdd import leap_year as ly



class TestLeapYear(unittest.TestCase):
   
    def test_years_divisible_by_4(self):
        self.assertEqual(ly(8), True)
      
   

if __name__ == '__main__': 
	unittest.main()
