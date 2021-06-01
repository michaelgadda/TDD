import unittest 
from leap_year_tdd import leap_year as ly



class TestLeapYear(unittest.TestCase):
   
    def test_years_divisible_by_4(self):
        self.assertEqual(ly(8), True)

    def test_years_divisible_by_100(self):
        self.assertEqual(ly(400), False)
        self.assertEqual(ly(404), True)

     def test_years_divisible_by_100_and_400(self):
        self.assertEqual(ly(400), True)
        self.assertEqual(ly(404), True)
        self.assertEqual(ly(200), False)
   

if __name__ == '__main__': 
	unittest.main()
