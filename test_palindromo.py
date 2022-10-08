import unittest
import main

class palindromo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(main.palindromo("Neuquén"),True)
        
    def test_2(self):
        self.assertEqual(main.palindromo("Anita lava la tina"),True) 

    def test_3(self):
        self.assertEqual(main.palindromo("A mí me mima"),True) 

    def test_4(self):
        self.assertEqual(main.palindromo("Manzana"),False) 

    def test_5(self):
        self.assertEqual(main.palindromo("El otro día"),False) 

    def test_6(self):
        self.assertEqual(main.palindromo("los osos"),False) 
   

if __name__ == "__main__":
    unittest.main()